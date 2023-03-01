Release Process
===============

Timeframe
---------

Our timeframe for deploying cycle upgrades to the summit is on an approximately bimonthly basis.
We have a repository called `ts_cycle_build <https://github.com/lsst-ts/ts_cycle_build>`_, which builds the deployable artifacts for each software component.
The nomenclature for the version of a cycle is determined by a cycle number which is incremented depending on if a core component version is updated (such as ts_sal, ts_xml and etc.) and a revision number which is incremented if any non core component is updated.
The cycle can be revised at any time post cycle release.

The Cycle Build uses a custom release process as documented on `ts-cycle-build.lsst.io <https://ts-cycle-build.lsst.io>`_.

The timeframe for release will be defined per application, by the Developer(s) and Product Owner(s), and should part of the high-level lsst.io site.

This timeframe should be tied to the Sprint process, such that a Release coincides with the end of Sprint.
However, not every Sprint must be a release, and as such, a Release can span multiple Sprints.

The timeframe can take many forms.
It can be a regularly scheduled duration (quarterly, monthly, weekly, etc) or based on some event-based metrics.
For example, after some number of features are complete or simply based on a schedule of milestones.
Whatever form this takes, it will be defined on the High-level lsst.io site for each application.

TSSW Git Workflow
-----------------

Our team uses a modified gitflow workflow.
The main difference is that most of the repositories do not use the Release branch and instead choose to merge to main from develop directly.
This is because most of our repositories only have one or two developers working on them at a time and releases are usually coordinated so that no one can accidently commit changes to a release.
Some of our larger repositories such as ts_xml and ts_sal which have a larger number of developers working on them, use the Release branch.

See `Gitflow Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_ for the detailed description of the standard workflow and process.

Main Branch
^^^^^^^^^^^
The main branch is for production ready code only.
It should contain only merge commits from the development and hotfix branches.
As it is considered production ready for summit use, this branch should always be stable and deployable.

.. note::
  We need to decide how to implement a cohesive strategy for tagging our code.
  We have several strategies out in the wild.

Release Branch (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^
The release branch is an optional branch in our process.
It is used by the major components in order to protect from untested code changes being merged to the develop branch unintended for release.
This is because we have multiple developers working on these components or that changes are foundational to the viablity of the other components that changes need to be verified.

Develop Branch
^^^^^^^^^^^^^^
The develop branch is the trunk that stores the code that is ready for the next release.
We consider this code to be a release candidate ready as necessary where the CI is passing but not always stable.

Ticket Branch
^^^^^^^^^^^^^
Ticket branches are where main development efforts are done.
They are branched from the develop branch.
They are merged upon successful CI build and an approving review.

HotFix Branch
^^^^^^^^^^^^^
HotFix branches are branched from main when a critical bug is discovered during production use.

Release workflow
^^^^^^^^^^^^^^^^
Package releases start by tagging a release using an annotated git tag as described in :ref:`Versioning`.
Packages are then built using the Continuous Integration process.
For our python CSCs, we use a conda package mechanism with SAL libraries in RPM packages.
For non Python based CSCs, we have different package mechanisms.

Once the packages are tagged and built, the version numbers are updated on the Cycle Build which leads to the docker deployment images being built and pushed to our Nexus docker registry.
The images are then passed to ArgoCD which deploys the images to the summit kubernetes cluster.
