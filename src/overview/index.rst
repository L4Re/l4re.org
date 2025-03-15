L4Re Overview
*************

L4Re is an operating system framework that allows you to build custom operating
system and hypervisor solutions. The project is maintained by `Kernkonzept
<https://www.kernkonzept.com>`_.

The L4Re Operating System Framework provides the building blocks for creating
custom operating systems with real-time, security, safety and virtualization
features. Common deployments are the L4Re Hypervisor and L4Re Micro Hypervisor
that form the base for a feature-rich virtualization platform for hosting
workloads of general-purpose, real-time, security and safety kinds.

.. figure:: systemarchitektur.png
   :align: center

   L4Re's system architecture

You can get an overview of the architectural design choices of L4Re at :doc:`architecture`.

.. todo::

   - Stretch goal: add content for "Small TCB"
   - Stretch goal: add content for "Modular"

Systems using L4Re are built out of fit-to-purpose components that are
composed as needed for a specific use-case. Components and dependencies down
to the microkernel are small, providing small application-specific trusted
computing bases (TCBs). This architecture gives a good base for evaluating
the correct working of a composed system and thus fits well with use-cases
where the need for security and safety is paramount.

Whether it is implementing crucial functionality or isolating different kind
of work-loads and domains, L4Re can support many use-cases in different
domains and industries, such as automotive, avionics, communication
infrastructure and devices, defense, robotics, medicine, IoT, and many more.

Refer to :doc:`usecases` for examples of domain-specific use-cases.

.. todo::

   - Stretch goal: add information about License

.. toctree::
   :hidden:

   architecture
   usecases
