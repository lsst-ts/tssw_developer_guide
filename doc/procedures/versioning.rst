Versioning
==========

Package versioning should use Semantic Versioning `<https://semver.org/>`_.
Exceptions (e.g. see the cycle build) should be well documented in the package and may require an RFC ticket.

Tagging a version has the following rules:

  * ticket branches can be tagged with ``vX.Y.Z.alpha.N`` or ``vX.Y.Z.beta.N`` tags
  * The develop branch can be tagged with ``vX.Y.Z.rc.N``
    If your code is using ts_xml develop branch then the CSC release must be tagged here.
  * Main branch is reserved for main tags: ``vX.Y.Z``
    Any releases tagged from here must be compatible with the current released version of ts_xml.

Where X, Y and Z are major, minor and point/hotfix respectively.

* Use `Annotated tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_ on the main branch

  * The Annotation is a meaningful text description of the release
