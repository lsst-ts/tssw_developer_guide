.. _Versioning:

Versioning
==========

Package versioning should use Semantic Versioning `<https://semver.org/>`_.
Exceptions (e.g. see the cycle build) should be well documented in the package and may require an RFC ticket.

Tagging a version has the following rules:

  * Ticket branches can be tagged with ``vX.Y.Z-alpha.N`` or ``vX.Y.Z-beta.N``
  * The develop branch can be tagged with ``vX.Y.Z-rc.N``
    If your code is using ts_xml develop branch then the CSC release must be tagged here.
  * Main branch is reserved for main tags: ``vX.Y.Z``
    Any releases tagged from here must be compatible with the current released version of ts_xml.

Where X, Y and Z are major, minor and point/hotfix respectively.

* Use `Annotated tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_ on the main branch

  * The Annotation is a meaningful text description of the release

* For the ts_config_* projects, no ``-`` should be used but instead a ``.``.

  * Ticket branches can be tagged with ``vX.Y.Z.alpha.N`` or ``vX.Y.Z.beta.N``
    In the `cycle.env` file of `ts_cycle_build <https://ts-cycle-build.lsst.io/>`_ the tag needs to be referred to as ``X.Y.ZaN`` or ``X.Y.ZbN``.
  * The develop branch can be tagged with ``vX.Y.Z.rc.N``
    In the `cycle.env` file of `ts_cycle_build <https://ts-cycle-build.lsst.io/>`_ the tag needs to be referred to as ``X.Y.ZrcN`` or ``X.Y.ZrcN``.

.. tab-set::

  .. tab-item:: Tag alpha

    Tag alpha on ticket branches.
    This is for developing new features or bug fixes for deploying in environments.

    .. prompt:: bash

      git tag vX.Y.Z-alpha.N
      git push origin vX.Y.Z-alpha.N

    Note that there is no need to annotate alpha tags.

  .. tab-item:: Tag beta

    Tag beta on ticket branches.
    This is meant for new features or bug fixes that have finished development but are still not quite finished.

    .. prompt:: bash

      git tag vX.Y.Z-beta.N
      git push origin vX.Y.Z-beta.N

    Note that there is no need to annotate beta tags.

  .. tab-item:: Tag release candidate

    Tag release candidates on develop branch.
    This is for software that has new XML that has not been released or for bigger changes that require further testing.
    This branch is considered to be always ready to deploy which means passing unit tests.

    .. prompt:: bash

      git tag vX.Y.Z-rc.N --annotate -m "Add release message here."
      git push origin vX.Y.Z-rc.N

    Release candidate tags should be annotated.

  .. tab-item:: Tag release

    Tag releases on main branch.
    This is for software that's ready to be deployed on production.

    .. prompt:: bash

      git tag -a vX.Y.Z --annotate -m "Add release message here."
      git push origin vX.Y.Z

    Release tags should be annotated.
