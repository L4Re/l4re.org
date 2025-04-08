.. _bsp:

BSP and hardware support
************************

.. todo::

   - Write more content
   - The list is not really long. Are there more we could add?

L4Re supports many SoCs and boards. The following list is a collection of
informations for specific boards and setups. Usually, if the SoC is
supported, any other board based on the same SoC should be usable too.


Device Tree, ACPI, UEFI, and standalone Targets
-----------------------------------------------

L4Re BSPs use hardware information as provided by the platform.

x86 targets use ACPI. RISC-V uses SBI and device-tree.

Arm targets can be standalone, use device tree or ACPI. While some older
targets do not use device-trees and encode platform information themselves,
newer ones will use the platform's device tree. We also target to convert
standalone BSPs to device-tree ones as we come across them.

The Arm SBSA BSP uses ACPI and works on all SBSA-compliant platforms.

There is also a BSP porting guide to enable new platforms for L4Re: :doc:`porting-guide`


BSPs
----

.. toctree::
   :maxdepth: 1

   porting-guide.rst
   rpi.rst
   s32g.rst
   zynqmp.rst
