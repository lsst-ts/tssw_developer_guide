.. TSSW Developer Guide documentation master file, created by
   sphinx-quickstart on Tue Apr  2 20:55:52 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

********************
TSSW Developer Guide
********************


.. important::

    The following guide is not approved nor authorized by anyone.
    It only serves as a proposal for guidelines.


Additional Resources
====================

:doc:`jira`

`TSS Product Owner <https://confluence.lsstcorp.org/display/LTS/TSS+Product+Owner>`_

`TSS Jira Guidelines <https://confluence.lsstcorp.org/display/LTS/Jira>`_

`Gitflow Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_

.. todo::

    Add image of new workflow.

Component Resources
===================

* In this context, a component is a logical grouping of code. A CSC (Configurable SAL Component) or a set of hardware testing code can be considered an component.
  A component may consist of many applications (i.e. CSC created from the LabVIEW component template).
* Internal Libraries, tools and similar items will NOT be considered components.
  However, they should have documentation that outlines their functionality.
  Components using this functionality should link to the CSC's documentation site.
* Requirements & Schedule of the component is determined by the :term:`Product Owner` & the Component Developer.
  These two must work in tandem to determine what the resulting component shall be.
  There is a :ref:`bi-weekly sprint planning meeting <jira:Sprints>` to help facilitate this process.
* Each application should have an unrestricted, high-level lsst.io site that defines and/or contains:
  
  * Release roadmap
  * User Guide/Manuals
  * Dependencies
  * Reverse chronological order of releases, linked to Detailed Release Notes
  * Github repository link
  * Jenkins build project
  * Link to Jira Component

* These pages should be stored under a TBD hierarchy.
* Detailed Release Notes should be part of the documentation site as well.

  * Create a page for the next release as soon as work begins

    * Keep up-to-date as development progresses.

  * As part of release announcement, make this page public.

* A template will be produced for the format above which every application should follow.

Jira workflow
=============

.. todo::

    Update to current Jira workflow

The Sprint in which these tasks are placed is defined :ref:`here <jira:Sprints>`.

Please refer to the TSSW JIRA Workflow diagram above.

* Initial/Triage
  
  * Create the Task, Bug or Improvement.
  * The intital assignee houd triage the ticket.

    * Ensure it is assigned correctly (Assignee, Component , etc)
    
      * Ensure the ticket is assigned to an actual, currently employed at LSST, person.
      * Each ticket is assigned a JIRA Component.
        If an Assignee is not designated, the JIRA Component will determine the assignee.
    
        * The component to assignee designation can be found `here <https://jira.lsstcorp.org/projects/TSS?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page>`_.

    * Ensure the Priority is set correctly (Ticket should not have the "Undefined" priority).
    * A Sprint can be chosen at creation (preferably by the person doing the work for this ticket).
      Otherwise the ticket is automatically placed in the Backlog.
      If the ticket is in Backlog, once the sprint is known, the ticket should be updated with the current sprint.
  
  * Once work begins, move the ticket to In Progress

* In Progress

  * Create the feature branch in the git repo and link the branch to the JIRA component.

    * No active development is ever done on the Master or Develop branches.
    
  * Document the requirements (via Requirements Template)
  * Write the code.
  * Write the unit tests.
  * Update release Notes & pertinent doc strings
  * When complete, move to In Review.

    * Complete meaning:

      * Add a link of the commit to the ticket.
      * Unit tests exist, have been successfully run and results have been added to the ticket or commit.
      * Add a link to the completed release notes

* In Review

  * Once the code is complete and all unit tests are passing, intitate a pull request on the develop branch and assign it to the Reviewer(s).
  * The Reviewer ensures

    * Code is complete and understandable.
    * Unit tests are passing.
    * Documentation is done, including a reference to the lsst.io site
    * All Requirements, as defined in the ticket Description, are met.

  * If findings occur

    * Updates Jira with findings 
    * Sends back to developer

  * If no findings occur

    * Moves Jira ticket to review complete with approval/minor changes.

* Reviewed

  * The Developer then merges the pull-request (see Merge Process, below).
  * Moves ticket to Resolved.

* Resolved

  * This is the purview of QA.
  * QA does another spot review, to ensure the requirements are spelled out and properly met, all documentation is provided and the unit tests are passsing.
  * This is also when QA works on the higher level tests (Functional, Integration, etc).
  * Once this is Complete, QA moves to Closed.

* Closed

  * The ticket is complete.

    * Feature was successfully implemented.
    * Feature was de-scoped; proper explanation provided.
    * Ticket was not implemented for some othe reason; proper explanation provided.

Versioning
==========

* Version format:

  * "vX.Y.Z", where
  
    * v, for Version and is in lower case
    * X major release
    * Y minor release
    * Z point or hotfix release

  * Proposed definitions for Major, Minor and Point/Hotfix: https://semver.org/

* Use `Annotated tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_ on the master branch

  * The Annotation is a meaningful text description of the release

Release Process
===============

Timeframe
---------

The timeframe for release will be defined per application, by the Developer(s) and Product Owner(s), and should part of the High-level lsst.io site.

This timeframe should be tied to the Sprint process, such that a Release coincides with the end of Sprint.
However, not every Sprint must be a release, and as such, a Release can span multiple Sprints.

The timeframe can take many forms.
It can be a regularly scheduled duration (quarterly, monthly, weekly, etc) or based on some event-based metrics.
For example, after some number of features are complete or simply based on a schedule of milestones.
Whatever form this takes, it will be defined on the High-level lsst.io site for each application.

Gitflow Workflow
----------------

See `Gitflow Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_ for the detailed description of the workflow and process.

* Master branch

  * This branch is for Releases ONLY.

    * Should only have merge commits and only from Release branches or HotFix branches.
    * NO active development should take place here.

  * Each release should be tagged with the appropriate version.
  * Should always be stable and deployable.
  * Release workflow:

    * Once Developer team and Product Owners decide the Application is ready for a Release, the Developer creates the Release branch and notifies QA.
    * QA runs tests on the Release branch.

      * if Issues found:

        * team decides if the fix is necessary or not.

      * once the Product Owner, Developers and QA feel the Application is ready for release:

        * Developer cuts the Release by merging to Master and creating the version tag.
        * QA does another set of testing, after the merge, on the Release.

* Develop branch

  * This is the main trunk for the code.

    * Should only have merge commits, from Feature and Release branches.

  * NO active development should take place here.

* Feature branch

  * Branched from develop.
  * Where active development occurs
  * When Feature is complete, merge to develop.

    * All requirements are met.
    * Unit tests are complete and passing.
    * pull request approved, can then merge to develop

* HotFix branch

  * Branched from Master.
  * Only for necessary, emergency fixes to already released version.
  * Merged to Master and Develop when complete.

* Release branch

  * Branched from Develop.
  * No active development.
  * Only bug fixes and documentation commits allowed.
  * Merge to Master and Develop.

Merge Process
=============

To Merge, or Not to Merge, should you Squash and Rebase or just Merge, that is the question.

This is a style and preference decision, and one that will be made by the Developer team and the Product Owner.
The choice will be defined on the Application's high-level lsst.io site.

For reference, see `Git-Branching-Rebasing <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>`_.

Building Applications
=====================

`Jenkins <https://ts-ci.lsst.codes/>`_ is the chosen Continuous Integration platform.
Each application should have a build project in Jenkins.
These applications should then have a dedicated build server.

Each build should run the unit tests. 
If the unit tests pass, the application should generate the deployable package and feed into the deployment system.
Puppet is the Deployment application. 
See `Puppet Server Installation <https://confluence.lsstcorp.org/display/~avillalo/Puppet+Server+Installation>`_ and https://puppet.com/ for more information.

The packaging system is still being investigated, but is leaning towards using RPMs, in general.
For pure Python only applications, setuptools is a fine solution.
LabVIEW may require another solution as well.
This area is quite flexible, as the only real constraint is that it must be compatible with Puppet.

Managing Dependencies
=====================

This is an open question.

* Should we use `git-submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules?>`_

  * This might be an exellent solution for ts_sal and ts_xml

* Should we choose a configuration management tool to handle this?

  * Puppet may have some capabilities here.
  * RPMs might also address this issue.

Python
======

A proposal specific to python development can be seen here: `TSSW Python Proposal Guide <https://confluence.lsstcorp.org/display/~ecoughlin/TSSW+Python+Proposal+Guide>`_

Component Team Structure (this needs a better heading?)
=======================================================

Each Component should have the following roles occupied

.. glossary::

  CAM/Stakeholder 
    customer or user base for component

  Product Owner 
    Product owner defintion here: `TSS Product Owner <https://confluence.lsstcorp.org/display/LTS/TSS+Product+Owner>`_

  Lead Developer 
    Main developer for the component 

  Backup Developer 
    developer to take over if the Lead Developer wins the lottery and runs away.

  SW Manager 
    Personnel who can decide resolution, if there is conflict with the four roles above.


Sources
=======

* Adapted from https://confluence.lsstcorp.org/display/LTS/TSS+Developer+Guide+-+Draft
* https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow