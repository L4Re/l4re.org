.. _contributing:

Contributing to L4Re
********************

.. toctree::
   :hidden:

   styleguide.md

We welcome contributions to the L4Re project. However, to incorporate your
contribution we are required to have a signed Contributor License Agreement
(CLA) from you on file. The CLA certifies:

1. That you have the rights to give us the contribution and
2. That you give us the rights to use your contribution.

Please sign the `Contributor License Agreement
<https://www.kernkonzept.com/CLA>`_ and email it to
**licensing@kernkonzept.com**, or send the original to Kernkonzept GmbH,
Buchenstr. 16b, 01097 Dresden, Germany.

If you feel it is too cumbersome to go through the whole CLA process for
trivial contributions such as typo fixes, then please create an issue and we
will fix it for you.

In order to maintain the high quality of the codebase we review each patch
before it is submitted to our private master branch. We will continue to act as
gatekeepers for pushing patches into the public repositories. That means that
each contribution will be reviewed by Kernkonzept internally, before it gets
merged to our private master branch and eventually gets published into the
public repositories. Note that this can take quite a while as we may depend on
external funding to do the work.

If you seek to make a large or involving change please open an issue up front
and start discussing the details with us.

Submitting patches
==================

This guide contains a collection of suggestions for a person or company not
familiar with our development process to help getting your contribution
accepted.

Describe your changes
---------------------

Describe the problem your patch is solving. If your patch fixes a
known bug, refer to that issue by number or URL. After describing the problem,
describe in technical detail what you are actually doing to fix it.

Separate your changes
---------------------

Separate each logical change into a separate patch that can be verified by our
reviewers. Solve one problem per patch.

If you divide a change into a series of patches, take special care to ensure
that the project builds and runs properly after each single patch of the series
is applied.

If one patch depends on another patch simply note **"this patch depends on
patch X"** in the patch description.

Style-check your changes
------------------------

Check your patch for basic style violations. See our :ref:`contrib-styleguide`
for guidance.

Respond to review comments
--------------------------

Most contributions will almost certainly receive review comments. Please
respond to those comments to show that you care about you contribution.
