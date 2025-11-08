Running the pre-built Images
############################

l4re.org hosts `pre-built images <https://l4re.org/download/snapshots/pre-built-images/>`_ for various
architectures, targets, configurations and file formats.

For the ``arm-v7`` and ``arm64`` architectures, the images are available for
several targets, indicated in the filename.

Please use the file format usable for your target.

Using QEMU
----------

A set of images is also generated for QEMU. Download the ELF image variant
and use ``l4image`` to launch it:

.. sourcecode:: shell

    $ wget https://l4re.org/download/snapshots/pre-built-images/l4image
    $ chmod +x l4image
    $ wget https://l4re.org/download/snapshots/pre-built-images/arm64/l4re_vm-multi-p2p_arm_virt.elf
    $ ./l4image -i l4re_vm-multi-p2p_arm_virt.elf launch

    L4 Bootstrapper
      Compiled with: GCC (15.2.0)
      Bootstrap build info:  2025-09-28 13:00:34 CEST+0200
      L4Image creation info: 2025-09-28 13:01:07 CEST+0200
      L4Image sequence info: #18
      RAM: 0000000040000000 - 000000007fffffff: 1024.0 MiB
      Total RAM: 1024.0 MiB
      Scanning fiasco -serial_esc
      Scanning sigma0
      Scanning moe rom/vm-multi-p2p.cfg
      Moving up to 13 modules behind 41100000
      Using 'modaddr 0x1000000' in modules.list might prevent moving modules.
      moving module 12 { 42183000-421d7a77 } -> { 4226a000-422bea77 } [338.6 KiB]
      moving module 11 { 4205f000-42182d6b } -> { 42146000-42269d6b } [1.1 MiB]
      moving module 10 { 41362000-4205ee01 } -> { 41449000-42145e01 } [12.9 MiB]
      moving module 09 { 41361000-413618ef } -> { 41448000-414488ef } [2.2 KiB]
      moving module 08 { 4122a000-41360887 } -> { 41311000-41447887 } [1.2 MiB]
      moving module 07 { 411ea000-41229d27 } -> { 412d1000-41310d27 } [255.2 KiB]
      moving module 06 { 4119c000-411e98d7 } -> { 41283000-412d08d7 } [310.2 KiB]
      moving module 05 { 4110b000-4119bf9f } -> { 411f2000-41282f9f } [579.9 KiB]
      moving module 04 { 410e3000-4110a77f } -> { 411ca000-411f177f } [157.8 KiB]
      moving module 03 { 410e2000-410e254c } -> { 411c9000-411c954c } [1.3 KiB]
      moving module 02 { 410a6000-410e102f } -> { 4118d000-411c802f } [236.0 KiB]
      moving module 01 { 4109f000-410a5b37 } -> { 41186000-4118cb37 } [26.8 KiB]
      moving module 00 { 41019000-4109eb97 } -> { 41100000-41185b97 } [534.8 KiB]
      Loading fiasco
      found node 0 kernel info page (via ELF) at 0x40004000
      Loading sigma0 (offset +0x40099000)
      Loading moe (offset +0x400a4000)
      found node 0 kernel options (via ELF) at 0x40005000
      Sigma0 config    node: 0   ip:0000000040099864
      Roottask config  node: 0   ip:00000000400aa424
    Regions of list 'regions'
        [ 40001000,  40098fff] { 608.0 KiB} Kern   fiasco
        [ 40099000,  400a347f] {  41.1 KiB} Sigma0 sigma0
        [ 400a4000,  400e553f] { 261.3 KiB} Root   moe
        [ 40f00000,  40ffffff] {1024.0 KiB} Root   dtb
        [ 411c9000,  422bea77] {  16.9 MiB} Root   Module
        [ 422bf000,  422bffff] {   4.0 KiB} Root   mbi_rt
      Starting kernel fiasco at 400010c0

    Welcome to the L4Re Microkernel!
    L4Re Microkernel on arm-64
    Rev: unknown compiled with gcc 15.2.0 for QEMU Virtual Platform
    Build: #1 Sun Sep 28 12:50:42 CEST 2025

    Hello from Startup::stage2
    Reserved 62 MiB as kernel memory.
    GICv2
    GIC: Number of IRQs available at this GIC: 288
    Detecting PSCI ...
    Detected PSCI v1.1
    PSCI: CPU_SUSPEND format original v0.2, does not support OS-initiated mode
    PSCI: TOS: Not present or not required.
    FPU: Initialize
    ARM generic timer: freq=62500000 interval=62500 cnt=5678956
    SERIAL ESC: allocated IRQ 33 for serial uart
    Not using serial hack in slow timer handler.
    Cache config: ON
    CPU0: ID_PFR[01]:  00000222 00000000 ID_[DA]FR0: 10305106 00000000
          ID_MMFR[04]: 00001124 00000000 00000000 00000000
    Calibrating timer loop...
    Timer calibration done.
    MDB: use page size: 32
    MDB: use page size: 30
    MDB: use page size: 21
    MDB: use page size: 12
    CPU2 booted (same IDs as CPU0).
    CPU1 booted (same IDs as CPU0).
    SIGMA0: Hello!
      KIP @ 40004000
      allocated 4 KiB for maintenance structures
    SIGMA0: Dump of all resource maps
    RAM:------------------------
    [0:RWX:40000000;40000fff]
    [4:RWX:400a4000;400e5fff]
    [0:RWX:400e6000;40efffff]
    [4:---:40f00000;40ffffff]
    [0:RWX:41000000;411c8fff]
    [4:RWX:411c9000;422bffff]
    [0:RWX:422c0000;7c1fffff]
    IOMEM:----------------------
    [0:RW-:0;3fffffff]
    [0:RW-:80000000;ffffffffffffffff]
    MOE: Hello world
    MOE: found 943.1 MiB RAM in the area 40000000..7c200000
    MOE: allocated 962.0 KiB for the page array @0x400e9000
    MOE: virtual user address space [0-ffffffffff]
    MOE: cmdline: moe rom/vm-multi-p2p.cfg
    MOE: rom name space cap -> [C:103000]
    MOE: rwfs name space cap -> [C:105000]
      ROMFS: [411c9000-411c954d] [C:107000] vm-multi-p2p.cfg
      ROMFS: [411ca000-411f1780] [C:109000] l4re
      ROMFS: [411f2000-41282fa0] [C:10b000] ned
      ROMFS: [41283000-412d08d8] [C:10d000] cons
      ROMFS: [412d1000-41310d28] [C:10f000] l4vio_net_p2p
      ROMFS: [41311000-41447888] [C:111000] uvmm
      ROMFS: [41448000-414488f0] [C:113000] virt.dtb
      ROMFS: [41449000-42145e02] [C:115000] linux
      ROMFS: [42146000-42269d6c] [C:117000] ramdisk.cpio.gz
      ROMFS: [4226a000-422bea78] [C:119000] backtracer
      ROMFS: [40f00000-41000000] [C:11b000] .fdt
    MOE: Starting: rom/ned rom/vm-multi-p2p.cfg
    MOE: loading 'rom/ned'
    Ned says: Hi World!
    Ned: loading file: 'rom/vm-multi-p2p.cfg'
    Console Server
    cons> 
    Created vcon channel: p2p [421010]
    cons> 
    p2p     | Hello from l4vio_net_p2p
    p2p     | Max number of buffers in virtqueue: 256

    Created vcon channel: vm-1 [422010]
    cons> 
    Created vcon channel: vm-2 [423010]
    cons> 
    vm-1    | VMM: Created VCPU 0 @ 17000
    vm-1    | VMM[GIC]: create ARM GICv2
    vm-2    | VMM: Created VCPU 0 @ 17000
    vm-2    | VMM[GIC]: create ARM GICv2
    ...

