Xilinx / AMD Zynq-MP
********************


Building
========

Build an image for the ZynqMP as follows::

  $ make uimage E=hello PT=zynqmp


Booting with u-boot
===================


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
