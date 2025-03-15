Console multiplexer - cons
**************************

.. admonition:: Under Construction
   :class: note

   This part of the website is being worked on. Please refer to `the doxygen
   documentation <https://l4re.org/doc/l4re_servers_cons.html>`_ for
   information about this topic.

.. todo::

   - Stretch goal: Write content
   - Stretch goal: Examples on how to use it with ned?

``cons`` is the interactive console multiplexer for the L4Re operating system.
It allows to multiplex console output from different clients.  The output of
all clients is buffered and it allows to switch between them to redirect input.

Multiplexers and Frontends
==========================

``cons`` is able to connect multiple clients with multiple in/output servers.

Clients are handled by a *multiplexer*. Each multiplexer publishes a server
capability that allows to create new client connections. The default
multiplexer is normally known under the ``cons`` capability.

Actual in/output is handled by separate frontends. From the point-of-view of
cons, a frontend consists of an IPC channel to a server that speaks an
appropriate server protocol. By default the ``L4.Env.log`` capability is used.

For clients, ``cons`` implements the :l4re:`L4::Vcon` and the Virtio console interface.
The supported frontends is limited to :l4re:`L4::Vcon` only.


