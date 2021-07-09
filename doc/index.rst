.. TSSW Developer Guide documentation master file, created by
   sphinx-quickstart on Tue Apr  2 20:55:52 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

####################
TSSW Developer Guide
####################

`TSS Organization and Management Document <https://docushare.lsst.org/docushare/dsweb/Get/LTS-928/LTS-928%20V1.pdf>`_

Pages
=====

.. toctree::
  :glob:
  :maxdepth: 1

  *
  procedures/index
  conda/index
  docker/index
  deployment/index
  language/index
  development/index

Additional Resources
====================

`TSS Product Owner <https://confluence.lsstcorp.org/display/LTS/TSS+Product+Owner>`_

`Gitflow Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_

.. image:: /images/JiraWorkflow.png


Related Sites
=============

* `ts_xml <https://ts-xml.lsst.io>`_

Component Resources
===================

* In this context, a component is a logical grouping of code. A CSC (Configurable SAL Component) or a set of hardware testing code can be considered an component.
  A component may consist of many applications (i.e. CSC created from the LabVIEW component template).
* Internal Libraries, tools and similar items will NOT be considered components.
  However, they should have documentation that outlines their functionality.
  Components using this functionality should be linked to the CSC's documentation site.
* Requirements & Schedule of the component is determined by the :term:`Product Owner` & the Component Developer.
  These two must work in tandem to determine what the resulting component shall be.
  There is a :ref:`bi-weekly sprint planning meeting <procedures/jira:Sprints>` to help facilitate this process.
* Each application should have an unrestricted, high-level lsst.io site that defines and/or contains:
  
  * Release roadmap
  * Developer & User Guide/Manuals
  * Dependencies
  * Reverse chronological order of releases, linked to Detailed Release Notes
  * Github repository link
  * Jenkins build project
  * Link to Jira issues

* These pages should be stored under a TBD hierarchy.
* Detailed Release Notes should be part of the documentation site as well.

  * Create a page for the next release as soon as work begins

    * Keep up-to-date as development progresses.

  * As part of release announcement, make this page public.

* A template has been produced for the format above which every application should follow.

Creating a New Repository
-------------------------

The simplest way to create a new repository is to use sqrbot-jr on slack.
Upon request, the bot can create new repositories in the lsstts GitHub organization with the standard template, for a given type of product.

To do this, open the slack desktop or web app.
Go to the bottom of the left hand panel and find the "App" section.
Click on the "+" sign, search for sqrbot-jr and start a chat with it.
Send a message with "create project" to the bot and slack and follow the prompts to have the repository automatically created and setup for you.

.. image:: images/sqrbot-jr-1.png

Then pick the template ``LSST EUPs Package``

.. image:: images/sqrbot-jr-2.png

Fill out the following fields:

name
  The name of the package in the form of ``ts_{csc_name}``

Github Organization
  Choose ``lsst-ts``

Copyright
  Choose ``AURA``

Flavor
  Choose ``DDS Python``

.. image:: images/sqrbot-jr-3.png

Alternatively, you can also use the `template kit tool <https://github.com/lsst/templates>`_ provided by DM.
Once you have created the repository with its initial commit (either with sqrbot-jr or manually with the template kit), you need to set it up to follow our :ref:`workflow <index:Gitflow Workflow>`.

- First you need to create a ``develop`` branch from ``master`` and push it to the repository.
- Open the repository in GitHub and select the "Settings" tab at the top.
- Go to "Branches"
- On the "Default branch", click on "switch to another branch" and select develop instead of master.
- On "Branch protection rules", click on "Add rule".
- On "Branch name pattern" type "develop".
- On "Protect matching branches" select;
  
  - Require pull request reviews before merging
  - Include administrators

- At the bottom of the page select "Create"


Jira workflow
=============

The Sprint in which these tasks are placed is defined :ref:`here <procedures/jira:Sprints>`.

Please refer to the TSSW JIRA Workflow diagram above.

Initial/Triage
--------------
  
* Create a Task, Bug or improvement Jira ticket.
* The initial assignee should triage the ticket.

  * Ensure it is assigned correctly (Assignee, Component , etc)
  
    * Ensure the ticket is assigned to an actual, currently employed at LSST, person.
    * Each ticket is assigned a JIRA Epic.
    * A label with the name of the component should be added to the ticket.
    * Each ticket is assigned a component that begins with ``ts_``


  * Ensure the Priority is set correctly (Ticket should not have the "Undefined" priority).
  * A Sprint can be chosen at creation (preferably by the person doing the work for this ticket).
    Otherwise the ticket is automatically placed in the Backlog.
    If the ticket is in Backlog, once the sprint is known, the ticket should be updated with the current sprint.
  * The urgent label is reserved for work that impacts nighttime activities at the summit and should be given the utmost priority.

* Once work begins, move the ticket to In Progress

In Progress
-----------

* Create the ticket branch in the git repos
  The branch should be named ``tickets/DM-12345``, where ``DM-12345 is the ticket number assigned by Jira.
  Once the ticket is pushed to GitHub it is automatically linked to the JIRA component ticket.

  * No active development is ever done on the Master or Develop branches.
  
* Write the code.
* Write the unit tests.
* Update documentation
* When complete, move to In Review.

  * Complete meaning:

    * Add a link of the PR to the ticket.
    * Unit tests exist, have been successfully run and results have been added to the ticket or PR.
    * Add a link to the generated documentation site

In Review
---------

* Once the code is complete and all unit tests are passing, initiate a pull request on the develop branch and assign it to the Reviewer(s).
* The Reviewer ensures

  * Code is complete and understandable.
  * CI is passing.
  * Documentation is done, including a reference to the lsst.io site
  * All requirements, as defined in the ticket description, are met.

* If issues are found

  * Update Jira with issue

    * Comments on GitHub PR are considered acceptable as well

  * Sends back to developer

* If no issues are found

  * Moves Jira ticket to review complete with approval/minor changes.

Reviewed
--------

* The Developer then merges the pull-request.
* Moves ticket to Done.

Done
----

* The ticket is complete.

  * Feature was successfully implemented.
  * Feature was invalid; proper explanation provided.
  * Ticket was already fixed; proper explanation provided.


Release Process
===============

Timeframe
---------

.. todo:: Update with information about the cycle_build

The timeframe for release will be defined per application, by the Developer(s) and Product Owner(s), and should part of the high-level lsst.io site.

This timeframe should be tied to the Sprint process, such that a Release coincides with the end of Sprint.
However, not every Sprint must be a release, and as such, a Release can span multiple Sprints.

The timeframe can take many forms.
It can be a regularly scheduled duration (quarterly, monthly, weekly, etc) or based on some event-based metrics.
For example, after some number of features are complete or simply based on a schedule of milestones.
Whatever form this takes, it will be defined on the High-level lsst.io site for each application.

Gitflow Workflow
----------------

See `Gitflow Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_ for the detailed description of the workflow and process.

**Master branch**

* This branch is for Releases **ONLY**.

  * Should only have merge commits and only from Develop and HotFix branches.
  * NO active development should take place here.

* Each release should be :ref:`tagged <index:Versioning>` with the appropriate version.
* Should always be stable and deployable.

**Release workflow:**

* Once Developer team and Product Owners decide the Application is ready for a Release.
* QA runs tests on the master branch.

  * if Issues found:

    * team decides if the fix is necessary or not.

    * once the Product Owner, Developers and QA feel the Application is ready for release:

      * Developer cuts the Release by merging to Master and creating the version tag.
        When merging develop to master we recommend using ``--no-ff``, which disables "fast forwarding".
        This will create a new commit in the master branch with all the changes in develop.
      * QA does another set of testing, after the merge, on the Release artifact.

**Develop branch**

  * This is the main trunk for the code.
  * The develop branch is the default branch for any software repository.
    * The only exception is documentation repos where master/main is the default.

  * The branch is protected and only PRs approved by a reviewer are allowed to be merged and if applicable passing CI from the PR build
    * Private repositories are exempted because we use GitHub's free tier which does not offer branch protections for private repos.
  * Should only have merge commits, from Feature branches.
  * NO active development should take place here.

**Ticket branch**

* Branched from develop.
* Where active development occurs
* When work is complete, merge to develop.

  * All requirements are met.
  * Unit tests are complete and passing.
  * pull request approved, can then merge to develop

**HotFix branch**

* Branched from Master.
* Only for necessary, emergency fixes to already released version.
* Merged to Master and Develop when complete.

Versioning
==========

Tagging a version has the following rules:

  * ticket branches can be tagged with ``vX.Y.Z.alpha.N`` or ``vX.Y.Z.beta.N`` tags
  * The develop branch can be tagged with ``vX.Y.Z.rc.N``
    If your code is using ts_xml develop branch then the CSC release must be tagged here.
  * Master branch is reserved for main tags: ``vX.Y.Z``
    Any releases tagged from here must be compatible with the current released version of ts_xml.

Where X, Y and Z are major, minor and point/hotfix respectively.

  * Proposed definitions for Major, Minor and Point/Hotfix: https://semver.org/

* Use `Annotated tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_ on the master branch

  * The Annotation is a meaningful text description of the release

To merge and tag a release using ``git`` at the command line:
  * Checkout ``master`` and merge ``develop``.
    ``git checkout master``
    ``git merge --no-ff develop``

  * Tag the release.
    ``git tag -a vX.Y.Z -m "Some message about the release."``

  * Push the changes and tags.
    ``git push``
    ``git push origin --tags``

Building Applications
=====================

`Jenkins <https://tssw-ci.lsst.org/>`_ is the chosen Continuous Integration platform.
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

Component Roles
===============

Each Component should have the following roles occupied

.. glossary::

  CAM/Stakeholder 
    customer or user base for component

  Product Owner 
    Product owner definition here: `TSS Product Owner <https://confluence.lsstcorp.org/display/LTS/TSS+Product+Owner>`_

  Lead Developer 
    Main developer for the component 

  Backup Developer 
    developer to take over if the Lead Developer wins the lottery and runs away.

  SW Manager 
    Personnel who can decide resolution, if there is conflict with the four roles above.

The Component has most of this information defined in the Master CSC table on `ts_xml <https://ts-xml.lsst.io>`_.


Sources
=======

* Adapted from https://confluence.lsstcorp.org/display/LTS/TSS+Developer+Guide+-+Draft
* https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
