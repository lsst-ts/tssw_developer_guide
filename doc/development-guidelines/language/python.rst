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


Version History
===============

In the past a `version_history.rst` or similar file was maintained manually for each project by each sofware developer.
For projects where multiple developers are involved this often led to either merge conflicts, version conflicts or both.
TSSW therefore aims to migrate all projects to `towncrier` which should be added as a :ref:`pre-commit` hook.
After adding the towncrier pre-commit hook, copy the following README.rst file into the `doc/news` directory.

.. literalinclude:: README.rst.example
   :language: rst
   :caption: README.rst

After that you can add news fragments following the format instructions in the README.rst file.
News fragments can be added manually using any text editor or IDE.
It is also possible to create a news fragment using the towncrier command in a shell.
The command to create a news fragment is

.. prompt:: bash
    towncrier create -c "<News fragment message.>>" DM-XXXXX.<fragment type>.rst

The fragment types are explained in the README.rst file.
The command will take care of adding and increment numbering of the files if multiple news fragments of the same type are added for the same ticket.

.. note::
   Using towncrier from the command line requires the towncrier conda package to be installed.

Once all code changes for a new version have been made, the version history file can be updated using towncrier as follows:

   * Merge all branches that contribute to the new version into `develop`.
   * Merge `develop` into `main`.
   * Issue the following towncrier command:

     .. prompt:: bash
        
        towncrier build --version=vX.Y.Z

     See :ref:`Versioning` for a description of the versioning scheme used by TSSW.
   * Commit the changes to `main` using a descriptive commit message like `Update the version history.`.
   * Tag that commit *using the same version as used in the `towncrier build` command*.
   * Push the changes to GitHub.
   * Open a PR on `main` and request a review.
   * Once the PR has been approved, merge `main` into `develop`.

.. note::
   Some projects are configured to automatically delete the HEAD branch when a PR is merged.
   This means that the `main` branch is deleted when `main` is merged into `develop`.
   In that case simply restore the `main` branch and all is well.

.. note::
   The first time that a PR for `main` is opened, it will contain all commits from `develop`.
   Subsequent PRs will only have the latest commits.
