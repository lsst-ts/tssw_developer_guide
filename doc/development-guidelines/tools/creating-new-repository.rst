
.. _creating_a_new_repository:

#########
Sqrbot-jr
#########

The simplest way to create a new repository is to use sqrbot-jr on slack.
Upon request, the bot can create new repositories in the lsstts GitHub organization with the standard template, for a given type of product.

To do this, open the slack desktop or web app.
Go to the bottom of the left hand panel and find the "App" section.
Click on the "+" sign, search for sqrbot-jr and start a chat with it.
Send a message with "create project" to the bot and slack and follow the prompts to have the repository automatically created and setup for you.

.. image:: /images/sqrbot-jr-1.png

Then pick the template ``LSST EUPs Package``

.. image:: /images/sqrbot-jr-2.png

Fill out the following fields:

name
  The name of the package in the form of ``ts_{csc_name}``

Github Organization
  Choose ``lsst-ts``

Copyright
  Choose ``AURA``

Flavor
  Choose ``DDS Python``

.. image:: /images/sqrbot-jr-3.png

Alternatively, you can also use the `template kit tool <https://github.com/lsst/templates>`_ provided by DM.
Once you have created the repository with its initial commit (either with sqrbot-jr or manually with the template kit), you need to set it up to follow our :ref:`workflow <development_workflow>`.

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
