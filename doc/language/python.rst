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

.. literalinclude:: setup.cfg.example
   :caption: setup.cfg

.. include:: /conda/jenkins-conda.rst

###########
Style Guide
###########

.. literalinclude:: .pre-commit-config.yaml.example
   :caption: .pre-commit-config.yaml

.. note::
   The team is looking into tools to attempt to automate updates and configuration of ``pre-commit``.
   However the search is not done yet.

The team uses the following tools to enforce the style guide.

:black: An opionated autoformatter.
:isort: An opionated import sorter.
:flake8: A style checker with many different plugins to enforce different rules.
:check-yaml: Checks yaml files for proper format.
:mypy: Performs type checking on the code (optional).

This is enforced by a tool called ``pre-commit``.

.. include:: /development/jenkinsfile.rst


.. include:: /documentation-guide.rst

.. include:: /procedures/versioning.rst

.. include:: /procedures/reporting-xml-release-work.rst
