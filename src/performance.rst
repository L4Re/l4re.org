Performance Overview
********************

IPC, Context-Switch and Syscall Performance
===========================================

With L4Re being a microkernel-based system and hypervisor, some of you are
interested in the IPC and syscall performance of L4Re as well as the
performance of context switches. IPC is a base-level communication
mechanisms that allows to exchange a limited amount of payload data between
two threads. Context switching is switching from one executing thread to
another, which sending a message is exactly doing.
The fastest IPC is between two threads running in the same
address space (task) on the same CPU core (`Intra`). `Inter` is IPC between
two address spaces. A syscall is also an IPC but only communicates with the
kernel.

The following table provides IPC performance numbers for a single IPC on
various popular platforms. To perform the measurement, the L4Re microkernel has
been configured in its performance configuration ``CONFIG_PERFORMANCE=y``,
i.e., without assertions.

The source code of the benchmark program can be found `here
<https://github.com/l4re/ipcbench/>`_. The images used to measure those are
linked in the table below.

Numbers are measured with the performance counters. On Arm, the cycle counter
is used. On x86, the fixed-function counters are used.

+-----------------+----------------+------------------------------------------+--------------------+--------------+
| Platform        | Processor      | IPC (in CPU cycles)                      | Syscall            | Image        |
|                 |                +--------------------+---------------------+                    |              |
|                 |                | Intra              | Inter               |                    |              |
+=================+================+====================+=====================+====================+==============+
| Raspberry Pi 5  | Arm Cortex-A76 | 247                | 384                 | 138                | Img [#1]_    |
| 64bit - EL1     |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| Raspberry Pi 5  | Arm Cortex-A76 | 300                | 401                 | 202                | Img [#1]_    |
| 64bit - EL2     |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| NXP S32G2 64bit | Arm Cortex-A53 | 562                | 691                 | 230                |              |
| - EL1           |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| NXP S32G2 64bit | Arm Cortex-A53 | 661                | 770                 | 228                |              |
| - EL2           |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| Ampere Altra (32| Arm Neoverse-N1| 298                | 440                 | 148                |              |
| Cores) 64bit -  |                |                    |                     |                    |              |
| EL2             |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| amd64 / x86_64  | Intel N100     | 173/622/543 [#2]_  | 392/1395/587 [#2]_  | 64/190/148 [#2]_   | Img [#3]_    |
+-----------------+----------------+--------------------+---------------------+--------------------+              |
| amd64 / x86_64  | Intel Xeon     | 511/649/543 [#2]_  | 934/1128/587 [#2]_  | 222/160/148 [#2]_  |              |
|                 | Platinum 8352S |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+

.. [#1] Convert to raw image for rpi5 firmware boot:
   ``dd if=l4re_ipcbench_rpi5-elX.uimage of=l4re.raw bs=64 skip=1``
.. [#2] Values reflect the PMC's fixed-function counters 2 (TSC without halt) /
   1 (clocks unhalted) / 0 (instructions retired)
.. [#3] You can boot the image directly in GRUB2:
   ``multiboot2 (http,l4re.org)/download/ipcbench/amd64/l4re_ipcbench.elf32``
