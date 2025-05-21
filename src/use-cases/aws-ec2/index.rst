.. _use-case-aws:

L4Re on AWS EC2
***************

This page describes how to run L4Re on AWS EC2. EC2 instances boot via UEFI,
thus L4Re images have to be UEFI accordingly.

In your finished L4Re build, in your build tree, for x86-64, generate a UEFI
image like this::

  $ make efiimage E=hello

For arm64, use the SBSA platform and generate a UEFI image like this::

  $ make efiimage E=hello PT=arm_sbsa

On x86-64 the resulting image is called ``bootx64.efi`` and on arm64 it is
called ``bootaa64.efi``, and can be found in the ``images`` folder of your
build directory.


EC2 Instance Types
------------------

First, we need to select an instance type in EC2. In general the instance
type can be any, however, there is an important detail to consider. As of
this writing, EC2 does not support nested virtualization that would be
required to run a hypervisor within an instance which is a VM itself.
However, EC2 also offers "metal" instances which do not run EC2's hypervisor
but offer the whole machine to the user. With "metal" instances a user's
hypervisor can be run.

Thus, if virtualization shall be used with L4Re, a "metal" instance is
required. In a VM-instance, L4Re will only work in a non-hypervisor
configuration.

Booting on EC2
--------------

The generated EFI image of L4Re can be booted as any other OS kernel from
within the AMI, with GRUB or directly from UEFI.

Network Booting
^^^^^^^^^^^^^^^

EC2 also offers network booting which is useful when working with L4Re and
needing to regenerate the image often.

For this, iPXE is used as a boot loader which is able to download an image
via network and launch it.

To use it on EC2, please refer to the iPXE's EC2 site at
https://ipxe.org/howto/ec2 to configure your instance accordingly by picking
the right AMI for your architecture choice and EC2 region.

As described on the iPXE page, the "user state" of an instance needs to have
an iPXE script like this, for arm64::

   #!ipxe
   kernel http://l4re.org/download/snapshots/pre-built-images/arm64/l4re_vm-multi-p2p_sbsa.efi
   boot

This example uses the "vm-multi-p2p" image from the pre-built image
selection which uses virtualization and thus requires a "metal" Graviton
instance.

For x86-64 the approach is similar.

Interacting with the Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Head over to the "EC2 serial console" to interact with the instances,
especially for seeing the output of it.

Stopping an Instance
^^^^^^^^^^^^^^^^^^^^

For stopping the instance, ensure to issue a "Force stop instance" to really
shut down the instance.

Device pass-through
-------------------

With the help of io you can create virtual system busses (vbus for short),
restricting access to a subset of the system's hardware. These vbusses can
then be passed to L4Re applications, like uvmm (a guest) or nvme-drv (nvme
driver). L4Re applications, like the nvme-drv, can then in turn provide a
more nuanced access to these devices, e.g. only one partition.

The details, such as PCI IDs, might differ between arm64 and x86_64. The
following example was tested on the arm64 arm_sbsa platform.

Configuring io
^^^^^^^^^^^^^^

Io uses the scripting language Lua for its configuration. Within an io
configuration you can dynamically define which devices will be assigned to
which virtual system bus.

The following example detects NVMe devices and Network devices using their
respective PCI IDs.

.. code-block:: lua

   -- match returns matched devices as an array
   local ami_device = Io.system_bus():match("PCI/VEN_1D0F&DEV_0061")
   local ena_devices = Io.system_bus():match("PCI/VEN_1D0F&DEV_EC20")
   local nvme_devices = Io.system_bus():match("PCI/VEN_1D0F&DEV_0065")

   -- Create one vbus with all storage devices for nvme driver...
   Io.add_vbusses
   {
     storage = Io.Vi.System_bus(function ()
       Property.num_msis = 512;

       PCI0 = Io.Vi.PCI_bus(function ()
           ami = wrap(ami_device);
           nvme = wrap(nvme_devices);
       end);
     end);
   };

   -- and create a vbus for one guest with two network devices
   Io.add_vbusses {
     guest1 = Io.Vi.System_bus(function()
       Property.num_msis = 512;

       PCI0 = Io.Vi.PCI_bus(function ()
           network0 = wrap(ena_devices[0])
           network1 = wrap(ena_devices[1])
       end);
     end);
   };

Starting io from ned
^^^^^^^^^^^^^^^^^^^^

Using ned we can then start IO with this configuration. For each vbus
defined in the io config, a corresponding IPC gate needs to be created of
which we pass the server cap to io on start.

.. code-block:: lua

   -- Platform ctrl (Can be passed to guest so that shutdowns/reboots are
   -- passed through to host)
   local platform_ctl = L4.default_loader:new_channel();

   -- Storage vbus
   local vbus_storage = L4.default_loader:new_channel();
   -- Guest vbus
   local vbus_guest1 = L4.default_loader:new_channel();

   -- Start io
   L4.default_loader:start({
       scheduler = vmm.new_sched(0x40,0x2),
       log = { "io", "red" },
       caps = {
         sigma0 = L4.cast(L4.Proto.Factory, L4.Env.sigma0):create(L4.Proto.Sigma0);
         icu    = L4.Env.icu;
         iommu  = L4.Env.iommu;
         jdb    = L4.Env.jdb;

         -- Server side of platform_ctl cap, so IO responds to requests on it.
         platform_ctl = platform_ctl:svr();

         -- Server side of the storage vbus cap, nvme-driver uses this for
         -- access to storage hardware
         storage = vbus_storage:svr();

         -- Server side of guest1 cap, to pass to uvmm directly
         guest1 = vbus_guest1:svr();
       },
   }, "rom/io rom/config.io");

Nuanced storage access using nvme-drv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The storage vbus from our previous example contains the AMI NVME device and
several other configured NVMe devices. In order to not give access to all
of them to one guest we can use the nvme-drv to create seperate virtio
devices giving access to specific partitions and/or EC2 volumes.

.. code-block:: lua

   local nvme = L4.default_loader:new_channel();
   vmm.loader:start({
       scheduler = vmm.new_sched(0x40,0x2),
       log = { "nvme", "blue" },
       caps = {
         -- access to nvme devices via IO
         vbus = vbus_storage,
         -- endpoint for creating virtio devices
         svr = nvme:svr(),
         jdb = L4.Env.jdb,
       },
   }, "rom/nvme-drv");

   -- device parameter can be a Partition UUID (not FS UUID) or ...
   local nvme_part1 = nvme:create(0, "ds-max=5", "device=2FD29D59-FAFB-463E-8C4D-47B2931FA605");
   -- ... an EC2 volume id followed by an nvme namespace id (usually n1)
   local nvme_vol1 = nvme:create(0, "ds-max=5", "device=vol00489f52aed3a6549:n1");

Pass vbusses to uvmm
^^^^^^^^^^^^^^^^^^^^

After creating the vbusses and virtio devices these can be passed to
the corresponding guests. For this we can use the vmm.lua library provided
as part of the uvmm package.

.. code-block:: lua

  vmm.start_vm{
    -- Other settings...

    -- Vbus
    vbus = vbus_guest1,

    ext_caps = {
      disk = nvme_vol1;
    },
  };

Be aware: For each virtio device passed to a guest a corresponding
virtio-proxy node needs to exist in the device tree given to uvmm. This
node also chooses the name of the capability which has to be specified
here. The default arm64 device tree comes with one such node::

   virtio_net@10000 {
       compatible = "virtio,mmio";
       reg = <0x10000 0x200>;
       interrupt-parent = <&gic>;
       interrupts = <0 123 4>;
       l4vmm,vdev = "proxy";
       l4vmm,virtiocap = "net";
   };

Using cloud-init in guests
^^^^^^^^^^^^^^^^^^^^^^^^^^

While running as part of a guest uvmm cloud-init might not detect the
presence of the EC2 environment and thus might give up. To tell cloud-init
it is within an EC2 environment, you can append the following to your Linux
kernel boot parameter: ``cc:{'datasource_list':['Ec2']}``
