.. _Python:

######
Python
######

.. note::
    This guide is under development and is likely to change.

:python version: 3.10
:last-updated: |today|

The team uses the following files to configure, setup and install our python packages.
This guide assumes a repo created with the Templates project or using the sqr-bot jr create a repo functionality.

.. literalinclude:: pyproject.toml.example
   :caption: pyproject.toml
   :language: toml

.. literalinclude:: setup.py.example
   :language: python
   :caption: setup.py

Style Guide
===========

The team uses the following tools to enforce the style guide.

:black: An opinionated autoformatter.
:isort: An opinionated import sorter.
:flake8: A style checker with many different plugins to enforce different rules.
:check-yaml: Checks yaml files for proper format.
:check-xml: Checks xml files for proper format.
:mypy: Performs type checking on the code (optional).

This is enforced by a tool called ``pre-commit``.

Additional Information
======================

*  See :ref:`Jenkinsfile` for information on how to setup the CI job for your packages.
   This job is usually used to test PRs and are triggered by pushes to the github repo.
*  See :ref:`Conda-Jenkinsfile` for information on how to setup the CI conda job for your packages.
   This job is used to build conda packages.
   They are triggered daily by the build system and automatically when tags are pushed to the github repo.
*  See :ref:`documentation-guide` for information on how to write and publish package documentation.
*  See :ref:`Versioning` for information on how to version your packages.
*  See :ref:`reporting-xml-release-work` for information on how to update CSCs interfaces.
* See :ref:`pre-commit` for more information on the pre-commit tool.
