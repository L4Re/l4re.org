Detailed Introduction
*********************

L4Re is an operating system and a hypervisor as it runs both L4Re
applications and virtual machines.

It is built on a small kernel -- a microkernel -- and a user-level
infrastructure composed out of small components with distinct functions (see
:doc:`services <services/index>`). Please refer to
:doc:`architecture_concepts/index` to learn about the underlying concepts.

We call it **L4Re Operating System Framework** as it provides the building
blocks to construct tailored systems for specific use-cases.

The L4Re Operating System Framework:

* supports many hardware platforms,
* runs on Arm, MIPS, RISC-V, and x86 architectures
* is open-source software

The functionality features:

* A C library with pthreads support and shared libraries
* *libstdc++*, fully-featured C++ standard library
* C, C++, Ada and Rust (work in progress) environments
* Client/Server and communication frameworks
* Virtual file-system infrastructure
* Drivers, such as UART, NVMe, AHCI, network
* Scriptable program and system management using Lua
* Virtual machines and Hypervisor
* Platform and device management, including ACPI, PCIe, device tree
* Input/output multiplexing, including graphics

L4Re's :doc:`buildsystem/index` utilises `GNU Make
<https://www.gnu.org/software/make/>`_ to provide high customizability for the
user when it comes to choosing compilers and target platforms to cross-compile
for.


.. toctree::
   :hidden:

   architecture_concepts/index
   services/index
   libraries/index
   buildsystem/index
