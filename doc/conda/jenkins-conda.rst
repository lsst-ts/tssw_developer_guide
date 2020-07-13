=================
Conda Jenkinsfile
=================

The purpose of this document is to make a how-to for having a conda package build on CI.
This document includes templates for accomplishing this goal.
The first step is to create a conda recipe for a CSC.
The :doc:`conda development guide <conda>` will be helpful.
A template for doing so has been included on this page.

Change the ``csc-name`` so that it becomes the name of the csc.
Another thing is to change requirements so that they match the CSC's.
Keep in mind that the test requirements need to include test framework dependencies.

.. literalinclude:: meta.yaml.template
    :language: yaml+jinja

The next step is to create ``Jenkinsfile.conda`` file.
A template has been included below.
Replace ``csc_name`` with the name of the package/csc.
Replace ``csc_config_repo`` with one of the configuration repos.

.. literalinclude:: Jenkinsfile.conda.template
