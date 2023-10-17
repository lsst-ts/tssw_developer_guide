.. TSSW Developer Guide documentation main file, created by
   sphinx-quickstart on Tue Apr  2 20:55:52 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###########################################
Telescope and Site Software Developer Guide
###########################################

This page contains general procedures and guidelines adopted by the Telescope and Site Software (TSSW) team.
It serves as reference for the work done during construction, and future operations, of the Vera Rubin Observatory control software.

.. toctree::
  :glob:
  :maxdepth: 1
  :hidden:

  team/index
  work_management/index
  development-guidelines/index

Team
####

Basic information about the TSSW team and our culture.

- :ref:`onboarding_checklist`
- :ref:`culture_and_standards`

Communications
##############

TSSW adopts the same communications channels and procedures as Data Management (DM).
For more information see `DM Communications`_ Guidelines.

.. _DM Communications: https://developer.lsst.io/#part-communications

Work Management
###############

How work is coordinated and executed by TSSW.

- :ref:`Jira_Workflow`
- :ref:`development_workflow`

Development Guides
##################

For the most part TSSW follow `DM code style guidelines`_.
We highly recommend reviewing these guidelines before contributing to TSSW repositories.

.. _DM code style guidelines: https://developer.lsst.io/coding/intro.html

Following are a few guidelines particular to TSSW software:

- Create a new repository with :ref:`creating_a_new_repository`.
- :ref:`Python` is the language used most broadly by TSSW.
- :ref:`pre-commit` is a tool used to help guarantee style, formatting, etc consistency across the project.
- :ref:`reporting-xml-release-work` describes how to update CSCs interfaces.
- :ref:`developing-cscs-with-docker`.
- :ref:`Conda` is the official package management system used to distribute TSSW software.
- :ref:`Jenkinsfile` contains information on how to setup the CI job for your packages.
- :ref:`documentation-guide` contains information on how to write and publish package documentation.
- :ref:`Versioning` describes how to version your packages.
- :ref:`adding_or_removing_a_csc_from_the_xml_interface` describes how to add new components to the observatory control system.
- :ref:`XML-version-history` describes how to handle versioning of the control system interfaces.
