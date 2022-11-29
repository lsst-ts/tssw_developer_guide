Unit Testing
============
Whenever and wherever possible, unit tests should be run for any releasable application.
Unit tests should exist in a tests/ directory within the application git repository.
Explanations for the setup, installation and execution of the unit tests should be in the README file, also within the application git repo.
TSSW currently uses GitHub to host our code repositories, and GitHub presents the README file on the landing page of the repo, and therefore is an excellent location to provide this type of instruction.

As an example, please reference the `ts_xml <https://github.com/lsst-ts/ts_xml>`_ repo and its unit tests.

Finally, integration with the `TSSW Continuous Integration environment <https://tssw-ci.lsst.org/>`_ provides an opportunity to regularly run the unit tests.

The build and release process is fully documented in

.. todo::

  Link to build/release document section
