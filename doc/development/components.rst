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

.. image:: ../images/sqrbot-jr-1.png

Then pick the template ``LSST EUPs Package``

.. image:: ../images/sqrbot-jr-2.png

Fill out the following fields:

name
  The name of the package in the form of ``ts_{csc_name}``

Github Organization
  Choose ``lsst-ts``

Copyright
  Choose ``AURA``

Flavor
  Choose ``DDS Python``

.. image:: ../images/sqrbot-jr-3.png

Alternatively, you can also use the `template kit tool <https://github.com/lsst/templates>`_ provided by DM.
Once you have created the repository with its initial commit (either with sqrbot-jr or manually with the template kit), you need to set it up to follow our :ref:`workflow <procedures/releases:TSSW Git Workflow>`.

- First you need to create a ``develop`` branch from ``main`` and push it to the repository.
- Open the repository in GitHub and select the "Settings" tab at the top.
- Go to "Branches"
- On the "Default branch", click on "switch to another branch" and select develop instead of main.
- On "Branch protection rules", click on "Add rule".
- On "Branch name pattern" type "develop".
- On "Protect matching branches" select;

  - Require pull request reviews before merging
  - Include administrators

- At the bottom of the page select "Create"

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

The Component has most of this information defined in the Main CSC table on `ts_xml <https://ts-xml.lsst.io>`_.
