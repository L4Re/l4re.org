Troubleshooting
***************


Building the microkernel and L4Re user-level is a procedure complex enough
to offer many opportunities for things to go wrong. Here are the most common
issues and their causes:

Recovering from ham sync errors
===============================

If ham sync is terminated early using Ctrl-C or encounters network errors such
as the following an incomplete manifest may have been synced.

.. sourcecode:: shell

    mk: fatal: The remote end hung up unexpectedly
    mk: fatal: early EOF
    mk: fatal: index-pack failed

It is usually best to start again with an empty directory. Alternatively, it
may be possible to selectively force sync some packages listed in
.ham/manifest.xml:

.. sourcecode:: shell

    $ ham sync --force-local-update <manifest package name>

If network issues are suspected try:

.. sourcecode:: shell

    $ ham sync --max-connections=1

Missing top-level make file
===========================

If the ham sync operation was incomplete the *mk* package may be missing. In
this case it's best to restart ham sync from an empty directory. Running *make*
in the top-level directory results in this error indicating the top-level
Makefile is missing:

.. sourcecode:: shell

    make: *** No targets specified and no makefile found.  Stop.

Missing multilib
================

If you get the following error when creating a build directory on a 64-bit
host, make sure that multilib (or libraries supplementing it, e.g.
glibc-devel.i686 on Fedora) are installed:

.. sourcecode:: shell

    /usr/include/linux/errno.h:1:23: fatal error: asm/errno.h: No such file or directory
    #include <asm/errno.h>
                          ^
    compilation terminated.

Forgetting to set the architecture during *make config* before cross-compilation
================================================================================

If you forget to set the respective architecture during the configuration step
before cross-compilation, you may get failures that look like:

.. sourcecode:: shell

    arm-linux-gnueabihf-gcc: error: unrecognized command line option ‘-m32’
    Makefile:372: recipe for target 'Makeconf.bid.local-internal-names' failed
    make[5]: *** [Makeconf.bid.local-internal-names] Error 1

