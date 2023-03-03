.. _development-workflow:

####################
Development Workflow
####################

The most common workflow adopted by TSSW is as follows:

* All development happens on :ref:`ticket branches<development-workflow-ticket-branch>`.
* Ticket branches are merged to the :ref:`develop branch<development-workflow-develop-branch>` through a PR in github.
* When ready to release a new feature, develop is merged to the :ref:`main branch<development-workflow-main-branch>` and the main branch receives a release tag (see :ref:`development-workflow-release-process`).

Some repositories, such as ts_xml and ts_sal, use the Release branch and follow the `Gitflow Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_.

There are also some repositories that do not have a :ref:`develop branch <development-workflow-develop-branch>`, and PRs are done directly to the :ref:`main branch <development-workflow-main-branch>`.
All the documentation repositories follow this simplified workflow, as well as the `cycle build <https://ts-cycle-build.lsst.io>`_.

The following sequence of commands is the recommended way to execute the regular development workflow with git.

.. prompt:: bash

    # Synchronize your local develop branch
    git fetch --all
    git checkout develop
    git pull 

    # Checkout a ticket branch and setup upstream
    git checkout -b tickets/DM-12345
    git push --set-upstream origin tickets/DM-12345

From this point onwards you can make changes to your code and commit them to your local branch.
While developing, you can commit the intermediary stages and push them to git with:

.. prompt:: bash

    git commit <files to commit> -m "Commit message."
    git push

At this stage you don't necessarily need to keep your commits organized, but keep in mind that you will be asked to organize them before you merge your PR.

Once you are done will all your changes, make sure you update the version history of your package.
While reviewing the PR, avoid doing force-pushes to the repo as they make it hard for the reviewer to follow up on the changes.

Once the review has converged, it is a good time to reorganize your commits.
There are several different strategies for doing this, which are beyond the scope of this document.
`This article <https://render.com/blog/git-organized-a-better-git-flow>`_ provides good insight into a strategy to reorganize commits.

If you are working on a package with a high influx of contributions (e.g. ts_externalscripts and ts_standardscripts or one of the documentation packages), it may happen that someone else will merge a PR while your PR is still in progress.
When this happens, you should rebase your branch into develop to make sure you capture the latest changes merged to the repository and also to keep the branch history well organized.
Most repositories are configured to prevent PRs from being merged if they are not synchronized with the target branch.

In most cases this can be easily done with the following commands:

.. _develop-workflow-rebase-to-develop:
.. prompt:: bash

    git fetch --all
    git rebase origin/develop
    git push --force

.. _warning:

    After rebasing you will most likely have to force push your changes.
    This operation can be destructive, so make sure you are in the correct branch and that the rebase worked as expected (e.g. your changes are preserved).
    If you are unsure, create a backup branch and do not hesitate in asking for help.

Finally, see :ref:`development-workflow-additional-git-information` for more git-related information.

.. _development-workflow-develop-branch:

Develop Branch
--------------
The develop branch is the trunk that stores the code that is ready for the next release.
We consider this code to be a release candidate ready as necessary where the CI is passing but not always stable.

.. _development-workflow-ticket-branch:

Ticket Branch
-------------
Ticket branches are where main development efforts are done.
They are branched from the develop branch.
They are merged upon successful CI build and an approving pull request review.

.. _development-workflow-main-branch:

Main Branch
-----------
The main branch is for production ready code only.
It should contain only merge commits from the development and hotfix branches.
As it is considered production ready for summit use, this branch should always be stable and deployable.

Release Branch (Optional)
-------------------------
The release branch is an optional branch in our process.
It is used by the major components in order to protect from untested code changes being merged to the develop branch unintended for release.
This is because we have multiple developers working on these components or that changes are foundational to the viability of the other components that changes need to be verified.

HotFix Branch
-------------
HotFix branches are branched from main when a critical bug is discovered during production use.

Release workflow
----------------
Package releases start by tagging a release using an annotated git tag as described in :ref:`Versioning`, see :ref:`development-workflow-release-process`.
Packages are then built using the Continuous Integration process.
For our Python CSCs, we use a conda package mechanism with SAL libraries in RPM packages.
For non Python based CSCs, we have different package mechanisms.

Once the packages are tagged and built, the version numbers are updated on the Cycle Build which leads to the docker deployment images being built and pushed to our Nexus docker registry.
The images are then passed to ArgoCD which deploys the images to the summit kubernetes cluster.

.. _development-workflow-review-etiquete: 

PR Review
=========

We recommend following the `DM Code Review guidelines <https://developer.lsst.io/work/flow.html#code-review-discussion>`_ when reviewing PRs.

.. _development-workflow-release-process:

Release Process
===============

In most cases (see :ref:`development-workflow`), releasing a new version of a package consists in merging the develop branch into main and adding a :ref:`release <Versioning>` tag to the main branch.

This can be done in the command line with the following sequence of commands:

.. prompt:: bash

    git fetch --all
    git checkout develop
    git pull 
    git checkout main
    git pull 
    git merge develop --no-ff
    git push
    git tag -a vX.Y.Z  -m "Release vX.Y.Z message." # <- Replace X.Y.Z with the release numbers
    git push --tags


When doing a release it is recommended to use annotated tags (the ``-a`` in the ``git add`` command above) and add a release message.
If you want to include a multiline message you may skip the ``-m`` option which will cause git to open a text editor (``vi`` by default) where you can type the release message.

.. note:: Most packages have a "version history" file in their doc directory and you can copy and paste the message there into the text editor.

Time-frame
----------

Our time-frame for deploying cycle upgrades to the summit is on an approximately bimonthly basis.
We have a repository called `ts_cycle_build <https://github.com/lsst-ts/ts_cycle_build>`_, which builds the deployable artifacts for each software component.
The nomenclature for the version of a cycle is determined by a cycle number which is incremented depending on if a core component version is updated (such as ts_sal, ts_xml and etc.) and a revision number which is incremented if any non core component is updated.
The cycle can be revised at any time post cycle release.

The Cycle Build uses a custom release process as documented on `ts-cycle-build.lsst.io <https://ts-cycle-build.lsst.io>`_.

The time-frame for release will be defined per application, by the Developer(s) and Product Owner(s), and should part of the high-level lsst.io site.

This time-frame should be tied to the Sprint process, such that a Release coincides with the end of Sprint.
However, not every Sprint must be a release, and as such, a Release can span multiple Sprints.

The time-frame can take many forms.
It can be a regularly scheduled duration (quarterly, monthly, weekly, etc) or based on some event-based metrics.
For example, after some number of features are complete or simply based on a schedule of milestones.
Whatever form this takes, it will be defined on the High-level lsst.io site for each application.

.. _development-workflow-additional-git-information:

Additional Git Information
==========================

This session gather some additional information in dealing with git repositories while contributing to TSSW.

* Never merge develop (or any other branch) into your ticket branch as a way to synchronize branches.

  In general you should avoid merging different branches altogether.
  The only "merge" we expect to see in the development workflow is of ticket branches into develop.
  
  If you need to catch changes done in develop, use :ref:`rebase instead <develop-workflow-rebase-to-develop>`.

* If you are working on the same branch in more than one place or working in the same branch with more than one contributors, make sure you synchronize branches properly.

  One common mistake in this situation is to make some changes in the remote, than make some local changes without synchronizing, than trying to commit and push and 

  The following graph shows a git repository where the local branch (tickets/DM-38162) is 2 commits behind the remote branch (origin/tickets/DM-38162).

  .. image:: /images/git-example-1.png

  Then if the developer did local changes without pulling the remote first, this is what the repository will look like:

  .. image:: /images/git-example-2.png

  If they now try to push that to git, they will receive an error message:

  .. prompt:: bash $,# auto

    $ git push
    To github.com:lsst-ts/ts_cycle_build.git
    ! [rejected]        tickets/DM-38162 -> tickets/DM-38162 (non-fast-forward)
    error: failed to push some refs to 'github.com:lsst-ts/ts_cycle_build.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
  
  Note that git recommends pulling the changes before pushing.
  But if you try to pull it with the default command you get the following error:

  .. prompt:: bash $,# auto

    $ git pull
    hint: You have divergent branches and need to specify how to reconcile them.
    hint: You can do so by running one of the following commands sometime before
    hint: your next pull:
    hint:
    hint:   git config pull.rebase false  # merge
    hint:   git config pull.rebase true   # rebase
    hint:   git config pull.ff only       # fast-forward only
    hint:
    hint: You can replace "git config" with "git config --global" to set a default
    hint: preference for all repositories. You can also pass --rebase, --no-rebase,
    hint: or --ff-only on the command line to override the configured default per
    hint: invocation.
    fatal: Need to specify how to reconcile divergent branches.
  
  Basically git doesn't know how to merge the two divergent branches, and offers two strategies; rebase or fast-forward.
  The best option in this case is to use rebase, which gives the following git history graph:

  .. prompt:: bash

    git pull --rebase

  .. image:: /images/git-example-4.png
    
  If you try to fast-forward the changes you will end up with a strange git history that looks like this:

  .. image:: /images/git-example-3.png

  Note that rebasing may lead to conflicts if the same parts were modified in the different commits.
  If this happens you have to resolve the conflicts (most IDEs have good support for this) before continuing.
