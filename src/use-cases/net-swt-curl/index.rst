.. _use-case-net:

Networking with curl
********************

There are several options for providing network functionality on L4Re.

Basically two variants exists with respect to where a driver for a network
device can be placed.

One way is using an existing system, such as Linux, running it in a VM and
using Virtio-net to expose networking to outside of the VM. Using an
existing system, for example, Linux, gives further plenty of networking
features, such as firewalls and routing capabilities, and also plenty of
drivers for many, if not all, devices. A downside is that a
whole operating system and VM is required for this option, even if it can
be specifically customized for purpose of handling networking only.

A driver running in an L4Re application. This driver can either be ported
from some other environment or operating system, or written from scratch.
Eventually such a driver needs to interact with with the software
components that use it. Use could be in-process, i.e. an application has a
specific network driver built-in and thus directly talks to the network
device. Or the driver offers its services to other components in the
system through a shared memory interface. For network, Virtio-net is a
common and established interface.

In L4Re, there's a virtual network switch that also has support to integrate
device drivers. Thus the virtual network switch can be seen as a network
device driver with multiple Virtio-net interfaces, or a virtual network
switch where one port is not Virtio but a physical network device.


Running the network switch with the ixl drivers
-----------------------------------------------

The virtual network switch has support for the ``ixl`` network drivers.
Please refer to `the ixl drivers <https://github.com/l4re/ixl>`_ for
details, such as supported network devices.

The application using the network is the famous ``curl``. To work with the
driver via virtio-net, it needs a networking stack. We use ``lwIP``, which
has also been brought to L4Re with appropriate connectors for virtio-net.

Building ixl and virtio-net-switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The switch has a compile-time configuration that needs to be enabled such
that the functionality for network device drivers is included. Please have
the ``ixl`` package cloned to ``l4/pkg/ixl`` and the ``CONFIG_VNS_IXL``
enabled option in the L4Re configuration.


Building curl
^^^^^^^^^^^^^

Please have
`curl <https://github.com/l4re/curl>`_,
`zstd <https://github.com/l4re/zstd>`_,
and `LwIP <https://github.com/l4re/lwip>`_
cloned to ``l4/pkg/curl``, ``l4/pkg/zstd`` and ``l4/pkg/lwip`` respectively,
next to the standard L4Re packages.

Compile everything.


Starting the network switch and curl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following ned script starts the network switch together with curl,
downloading a web page.

.. sourcecode:: lua
   :linenos:

   -- vim:ft=lua

   local L4 = require("L4");
   local ld = L4.default_loader;

   local vbus_eth  = ld:new_channel();

   ld:start(
       {
           caps = {
               sigma0   = L4.Env.sigma0;
               icu      = L4.Env.icu;
               iommu    = L4.Env.iommu;
               ethdevs  = vbus_eth:svr();
           },
       },
       "rom/io rom/ixl.vbus"
   );

   local vswitch = ld:new_channel();

   ld:start(
       { caps = { vbus = vbus_eth, svr = vswitch:svr(); }, },
       "rom/l4vio_switch");

   ld:start(
      { caps = { virtnet = vswitch:create(0), etc = L4.Env.rom }, },
      "rom/curl -s http://ftp.de.debian.org/debian/",
      { IFCONFIG_IP4_vn0="dhcp" });


Please find a possible ixl.vbus `here <https://github.com/L4Re/ixl/blob/main/assets/ixl.vbus>`_.

A ``resolv.conf`` file also needs to be supplied with the following content::

   nameserver 10.0.2.3

