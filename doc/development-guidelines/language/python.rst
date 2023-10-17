.. _Python:

######
Python
######

.. note::
    This guide is under development and is likely to change.

:python version: 3.11
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

There are several other optional style guide tools as well.
This is enforced by a tool called :ref:`pre-commit`.
