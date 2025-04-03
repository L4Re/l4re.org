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
