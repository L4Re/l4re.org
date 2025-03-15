Performance overview
********************

IPC and Syscall Performance
===========================

With L4Re being a microkernel-based system, some of you are interested in the
IPC and syscall performance of L4Re. IPC is a base-level communication
mechanisms that allows to exchange a limited amount of payload data between two
threads. The fastest IPC is between two threads running in the same address
space (task) on the same CPU core. A syscall is also IPC but only communicates
with the kernel.

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
| amd64 / x86_64  | Intel N100     | 173/622/5431 [#1]_ | 392/1395/5871 [#1]_ | 64/190/1481 [#1]_  | Img [#3]_    |
+-----------------+----------------+--------------------+---------------------+--------------------+              |
| amd64 / x86_64  | Intel Xeon     | 511/649/5431 [#1]_ | 934/1128/5871 [#1]_ | 222/160/1481 [#1]_ |              |
|                 | Platinum 8352S |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| Raspberry Pi 5  | Arm Cortex-A76 | 247                | 384                 | 138                |  Img [#2]_   |
| 64bit - EL1     |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| Raspberry Pi 5  | Arm Cortex-A76 | 300                | 401                 | 202                | Img [#2]_    |
| 64bit - EL2     |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| NXP S32G2 64bit | Arm Cortex-A53 | 562                | 691                 | 230                |              |
| - EL1           |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+
| NXP S32G2 64bit | Arm Cortex-A53 | 661                | 770                 | 228                |              |
| - EL2           |                |                    |                     |                    |              |
+-----------------+----------------+--------------------+---------------------+--------------------+--------------+

.. [#1] Values reflect the PMC's fixed-function counters 2 (TSC without halt) /
   1 (clocks unhalted) / 0 (instructions retired)
.. [#2] Convert to raw image for rpi5 firmware boot:
   ``dd if=l4re_ipcbench_rpi5-elX.uimage of=l4re.raw bs=64 skip=1``
.. [#3] You can boot the image directly in GRUB2:
   ``multiboot2 (http,l4re.org)/download/ipcbench/amd64/l4re_ipcbench.elf32``
