.. _Python:

######
Python
######

.. note::
    This guide is under development and is likely to change.

:python version: 3.12
:last-updated: |today|

The team uses the following files to configure, setup and install our python packages.
This guide assumes a repo created with the Templates project or using the sqr-bot jr create a repo functionality.

.. literalinclude:: pyproject.toml.example
   :caption: pyproject.toml
   :language: toml

.. note::
   The `tool.setuptools_scm` section is mandatory and needs to be empty.

.. warning::
   We need to update the following files in order to make the version module appear correctly.
   The below files provide a working template for python 3.11 and python 3.12 and the updated setuptools_scm arguments.
   The __init__.py needs to be changed in order to avoid an import error during installation.

.. literalinclude:: setup.py.example
   :language: python
   :caption: setup.py

.. note::
   Replace `${CSC}` with the CSC pyton module name, e.g. `watcher` or `ess/csc`.

.. literalinclude:: __init__.py.example
   :language: python
   :caption: __init__.py


Style Guide
===========

The team uses the following tools to enforce the style guide.

:black: An opinionated autoformatter.
:isort: An opinionated import sorter.
:flake8: A style checker with many different plugins to enforce different rules.
:check-yaml: Checks yaml files for proper format.
:check-xml: Checks xml files for proper format.
:mypy: Performs type checking on the code (optional).

There are several other optional style guide tools as well.
This is enforced by a tool called :ref:`pre-commit`.
