######
Python
######

.. note::
    This guide is under development and is likely to change.

.. contents::
    :local:

Style
=====

Python has many recommendations for writing python code.
One of the primary sources of truth regarding styling is the Python Enhancement Proposal number 8 (PEP-8) which codifies the standard Python style guide.
The Telescope and Site Software Team will endeavor to follow this guide except in cases regarding salobj do_methods which inherit from SAL naming conventions.
As these are recommendations, any function or method names should follow consistent patterns, but is not enforced by python itself.
If a convention on an LSST stack package is to use lowerCamelCase then endeavor to follow that convention.
If working with a package that uses underscore_separation then one should follow that convention.
However, try to avoid mixing the two in order to improve readability except in the aforementioned exceptions regarding SAL compatibility.

PEP-8
-----

Here are key excerpts from PEP-8 which is linked `here <https://www.python.org/dev/peps/pep-0008/>`__ in its entirety.
This document deals with pretty much everything regarding python code and so this document will endeavor to highlight relevant points.

-  spaces instead of tabs for indentation

   -  four spaces per indentation

-  Class names are UpperCamelCase

-  method, function names and attributes are lower_underscore case.

-  One import per line except for from module import lines

-  The import order should be

   #. standard library

   #. third party imports

   #. application specific imports

-  module and package names should be lowercase and strive to be one
   word.

There are many tools that have been written to help ensure these standards are met.
Current recommendation is to use flake8 to ensure compatiblity with DM packages.
The goal is not perfection or total compliance, it is strive for consistency and readablity.
So any small deviations or things like SAL naming conventions will be noted and dealt with accordingly.

DM-Integration
--------------

Since several of our software products work with the LSST stack, those
packages must comply DM’s software `standards for
python <https://developer.lsst.io/python/style.html#pep-8-is-the-baseline-coding-style>`__.
As a result, the TSSW team shall endeavor to follow these DM exceptions
to PEP-8 compliance which are listed below for convenience.

Exceptions to PEP-8(`compliance with DM code <https://developer.lsst.io/python/style.html#exceptions-to-pep-8>`__)
   -  E133 The closing bracket is missing indention.

   -  E226 Missing whitespace around operator

   -  E228 missing whitespace around modulo operator

   -  Lines can be at maximum 110 characters

   -  W504 line break after binary operator

   -  N802

   -  N803

   -  N806

If a tool such as flake8 is used then one should configured it to use these exceptions in accordance with this guide.
An example configuration file is shown below.

.. code-block:: python
    :caption: setup.cfg

    [flake8]
        max-line-length = 110
        ignore = E133, E226, E228, N802, N803, N806
        exclude =
          bin,
          doc,
          **/*/__init__.py,
          **/*/version.py,
          tests/.tests


Docstring
---------

We will be using Numpydoc as our guide as outlined by the python
documentation standard. The current version of the guide is linked
`here <https://numpydoc.readthedocs.io/en/latest/format.html>`__.

Version Handling
----------------

Suggested Tools
   -  setuptools-scm
        An extension for setuptools that sets version based on git commit and tag metadata.

Python Development Packaging
============================

In the Python ecosystem, there are two kinds of packages, development
and distribution.
This section will focus on development packages, as
distribution is outside of the scope for this document.
Here are some options for dealing with these kinds of packages.
The current recommendation is to use pip packaging for vanilla python and any packages that integrate with LSST stack
will use :index:`EUPS` as per DM standards.

PIP
---

This is the defacto standard for python packages. Packages are created
using the setup.py format which uses setuptools as the backend device.
This is the default way for python packages to be installed. Setuptools
can handle python c extensions and other such steps. PIP uses warehouse
as its public distribution server but there are self-hosted options.

Conda
-----

This is an alternative package system that was designed for scientific python use.
Essentially meant to make installing complex python libraries like scipy, astropy and nltk easier to install on
different OSs.
It can build more than python packages and has a distribution mechanism in place.
It has a public option for allowing anyone to install its packages.
It also has private repos available to organizations that cost money.
Cost is unclear.
Conda also has a self-hosted enterprise version which also costs money but price is unknown.
It essentially can distribute any tool that can be installed and setup using shell commands(build tools included).
Conda documentation is located `here <https://conda.io/docs/>`__.

-  Could be used to handle EUPS packages underneath the conda
   environment.


.. index::
    single:EUPS

EUPs
----

This is the packaging system used by LSST’s DM and forms the backend to
the stack,which has a design philosophy that uses environment modules to
build packages.
Each package is built using an scons-lsst recipe which
allows for flexibility regarding packages that are polylingual.
Several of TSSW’s packages have stipulations which require the use of :index:`EUPS`.
DM’s documentation on the subject is located `here <https://developer.lsst.io/stack/eups-tutorial.html>`__.
The :index:`EUPS` source code is located `here <https://github.com/RobertLuptonTheGood/eups>`__.
That link also includes installation instructions outside of the LSST stack.

Unit Testing
============

Python has many unit test frameworks.
The current recommendation is to use pytest as that fits with current standards regarding
integration with Data Management’s software architecture.

Pytest
------

Pytest is our unit test framework of choice because it fits with DM’s
requirements by offering a choice between the unittest built-in library
and the new pytest syntax.
Essentially pytest is both a wrapper and extension of the built-in library and so is fairly flexible as a result.
You can find the documentation `here <https://docs.pytest.org/en/latest/>`__.

Mocking
-------

.. glossary::
   Mocking
      Mocking in unit tests are important for simulating logic that is unable
      to be inherently tested by software logic such as hardware and other
      such things.
      Mocking is the idea that when an object is created that is
      necessary for the application to function, it should be replaced by an
      object that merely returns a value or result.
      For example, a device that
      is connected to a serial port would be mocked by creating a mocked
      serial object that returns the expected output in a given scenario.
      Python3 has a mock object library built in and ready to use.
      That documentation is located `here <https://docs.python.org/3.6/library/unittest.mock.html>`__.
      For integration with Pytest, we can use an extension pytest-mock.
      Its documentation is located `here <https://github.com/pytest-dev/pytest-mock/blob/master/README.rst>`__.
      This extension just makes mocks easier to handle in the pytest-framework.

Documentation
=============

Python documentation generation uses
`Sphinx <http://www.sphinx-doc.org/en/master/>`__ and therefore any
source code documentation is recommended to use Sphinx. Sphinx uses
`ReST <http://docutils.sourceforge.net/rst.html>`__ as its markup
language of choice. Sphinx can also use markdown with an extension. Team
documentation uses confluence wiki as a major source of team documents.
For readmes, markdown is supported by github natively, although ReST and
asciidoc are supported as well. One recommendation is to include class
diagrams based on the python source code. There are tools to help
bolster this process but are not listed here yet.

Continuous Integration with Jenkins
===================================

Our Jenkins server(currently managed by LSST-SQRE) is located at https://ts-ci.lsst.codes.
So far, our python jobs have primarily been running unit tests that have been hopefully written.
For working with CI using python, we have an example file located
`here <https://github.com/lsst-ts/ts_tcs_ofcPython/blob/develop/Jenkinsfile>`__.
Jenkins can handle pulling docker images from dockerhub and is useful
for unit testing(and building) our applications.
Jenkins can also build docker images and upload them to dockerhub with the appropriate
credentials. 
Our deployment process will be outlined at a later time.

Suggested Tools
===============

The following are some tools that should or can be used for python
development.

Misc
   -  `Jenkins <https://jenkins.io/doc/>`__ - mandatory

   -  `flake8 <http://flake8.pycqa.org/en/latest/>`__ - mandatory with
      DM exceptions

   -  `pydocstyle <http://www.pydocstyle.org/en/latest/>`__ - checks
      compliance with docstrings

   -  `salobj <http://staff.washington.edu/rowen/ts_salobj/ts_salobj/index.html>`__
      - The default library for python CSC development

   -  third party packages - usually beneficial

   -  `LSST Stack <https://pipelines.lsst.io/>`__ - Primarily for
      Scheduler and WEP

Suggested IDEs & text editors
   -  `pycharm <https://www.jetbrains.com/pycharm/>`__

   -  `wing <https://wingware.com/>`__

   -  `pydev <http://www.pydev.org/>`__

   -  `vim <https://www.vim.org/>`__

   -  `nano <https://www.nano-editor.org/>`__

   -  `emacs <https://www.gnu.org/software/emacs/>`__

   -  `atom <https://atom.io/>`__

   -  `visual studio code <https://code.visualstudio.com/>`__

   -  `visual studio <https://visualstudio.microsoft.com/>`__