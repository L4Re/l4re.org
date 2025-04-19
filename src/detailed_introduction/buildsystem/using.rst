Using the Build System
======================

L4Re uses `make` for building all artifacts of the system.

While it is always safe and good to just issue ``make`` from the root directory of
your build tree, this takes longer than needed if not building everything is
needed. For example, this is the case if you are working on a specific
package.

There are a couple of options to only build what is of interest.

Build specific packages only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can build a specific package only, including its dependencies, like
this from the root of your build tree::

    build-root-dir$ make pkg/l4re-core/moe

This builds moe including all of moe's dependencies only.

If you just want to build a package, not considering its dependencies, just do::

    build-root-dir$ make -C pkg/l4re-core/moe

In fact that works with any directory.

This is useful if you are working on a specific package and just want to
recompile this specific code.

The build system also has a shortcut for building multiple directories at
once like with make's ``-C``. For example, if you are working on library and
need to build the library as well as the program using the library, you can
do::

    build-root-dir$ make S=pkg/mylib/lib/src:pkg/myprog

This will just build those two directories. 

Building from the source tree
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you build from the source tree, you need to specify the root of the
object tree, do this with ``O=``::

   source-tree$ make O=/path/to/obj-tree

Build Anywhere
^^^^^^^^^^^^^^

The L4Re build system has Makefiles everywhere, so you can also build
everywhere, from both the source tree as well as object tree. The build
system will descent to sub-directories.


Parallel Building
^^^^^^^^^^^^^^^^^

``make`` uses the ``-j`` parameter with a number of parallelism it should
use. So using ``make -j8`` is a good choice if you happen to have an 8 core
machine.

To have a sorted build output but still benefit from parallel builds at
least, parallel building can be enabled within directories with ``PL=``.
Call ``make`` without ``-j`` like this::

    $ make PL=8
