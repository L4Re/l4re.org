Xilinx / AMD Zynq-MP
********************


Building
========

Build an image for the ZynqMP as follows::

  $ make uimage E=hello PT=zynqmp


Booting with u-boot
===================

The ZynqMP is available in different configurations with different versions
of firmware software on it. We show different possibilities here.

Via network::

  # dhcp
  # tftpboot 0x0ffffc0 /path/on/your/tftp/server/bootstrap.uimage
  # bootm 0x0ffffc0 


When stored on MMC, via uimage::

  # fatload mmc 0 0x0ffffc0 bootstrap.uimage
  # bootm 0x0ffffc0 


Using raw-images is also possible::

  # fatload mmc 0 0x1000000 bootstrap.raw
  # go 0x1000000

Depending on the u-boot version it might also be necessary to load a device
tree file (``dtb``) when using the ``bootm`` command. For example::

  # fatload mmc 0 0x0ffffc0 bootstrap.uimage
  # fatload mmc 0 0x0fe0000 zynqmp.dtb
  # bootm 0x0ffffc0 - 0x0fe0000

Please check the u-boot configuration of your specific device for a good
load address for the device tree. Loading a FIT image might also be
worthwhile (``itb``).
