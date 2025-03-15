Detailed Introduction
*********************

The L4Re Operating System Framework consists of a small kernel -- a microkernel
-- and a user-level infrastructure that includes basic :doc:`services
<services/index>` such as program loading and memory management up to virtual
machine handling. L4Re also provides the environment for applications through
:doc:`libraries <libraries/index>` containing process-local and cross-process
functionality. Go to :doc:`architecture_concepts/index` to learn about the
underlying concepts.

L4Re's :doc:`buildsystem/index` utilises `Gnu Make
<https://www.gnu.org/software/make/>`_ to provide high customizability for the
user when it comes to choosing compilers and target platforms to cross-compile
for.

The L4Re Operating System Framework is:

* multi-platform and multi-architecture, including x86, ARM, MIPS, and RISC-V
* modular
* open-source
* virtualization-aware and flexible by providing multiple virtualization options

:doc:`libraries/index`, process-local and cross-process
functionality:

* C library with pthreads and shared libraries
* libstdc++, fully featured STL
* Virtual file-system infrastructure
* C and C++ environment
* Client/Server and communication frameworks

:doc:`services/index`:

* Scriptable program and system management
* Input/Output drivers
* Virtual machines and Hypervisor
* Platform and device management, including ACPI and PCIe
* Input/output multiplexing, including graphics


.. toctree::
   :hidden:

   architecture_concepts/index
   services/index
   libraries/index
   buildsystem/index
