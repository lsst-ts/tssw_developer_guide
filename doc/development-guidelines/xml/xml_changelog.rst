.. _XML-version-history:

###################
XML Version History
###################

It is the policy of this Project to document each set of changes to the `ts_xml repository <https://github.com/lsst-ts/ts_xml>`_
in the `version-history.rst <https://github.com/lsst-ts/ts_xml/develop/doc/version-history.rst>`_ file.

The `Changelog checker <https://github.com/marketplace/actions/changelog-checker>`_ GitHub Actions task was added to enforce that
this file is updated with each Pull Request (PR).

The format for the changes should be an unordered list with the following hierarchy:

#. Additions and removal of CSCs.
#. Various high-level changes **NOT** related to interface updates. 
#. The last first-order entry should be the **Interface updates** list item, which contains another unordered list of each CSC changed in the release.
#. Each CSC entry should contain an unordered list of each change made to the CSC. This should include, but is not limited to:

   * Additions and removal of topics.
   * Additions and removal of attributes.
   * Updates to attributes.

.. note::
   Large sweeping changes should be summarized, not itemized.

What follows is a template for each version entry in the version-history.rst file:

.. code-block:: 

  vX.Y.Z
  ------
  * Added <XYZ> CSCs.
  * Removed <ABC> CSCs.
  * Examples of high-level changes: unit test changes, non-CSC specific XML interface changes, XML schema changes, etc.
  * Interface updates.
    * <CSC_X>
      * Change1
      * Change2
    * <CSC_Y>
      * Change1
      * Change2

This is a guideline for the entry format, but it is not strictly enforced. A CSC with a single interface change could be done all on one line:

.. code-block::

  * <CSC_Z>: Change1

It is the responsibility of the PR reviewer to ensure the version-history entry is present and includes a sufficient summary of the changes.
