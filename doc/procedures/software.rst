#####################
Software Installation
#####################

This page outlines the file-system metadata for software produced for the Rubin Observatory by the Telescope and Site Software team.
This documents the results from :jira:`RFC-735`.

* Any executables produced for the Rubin Observatory and related software should be placed into the ``/rubin`` directory under a ``{subsystem}`` sub-directory.
* The ``rubin`` directory and all sub-contents should be owned by ``saluser:saluser`` on the file-system.
* The saluser group should have read/write permissions on these files as well.
* The user and group id for ``saluser`` should be 73006 on the file-system as well.
