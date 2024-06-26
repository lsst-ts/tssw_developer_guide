.. _Jenkinsfile:

Jenkinsfile
===========

* Make a Jenkinsfile using the template below.

.. literalinclude:: ./Jenkinsfile.template

This uses the Jenkins shared library with the following parameters

:name: This is the package name of the csc (use an underscore).
:module_name: This is the namespace path for the package i.e. lsst.ts.csc.
:idl_names: This is an array of IDL file names for building the package.
:build_all_idl: This will build all of the IDL files if true.
:extra-packages: An array of strings in the form of "organization/repo_name" to clone and build that are not already included in the develop environment image.
:kickoff_jobs: An array of strings of the names of the Jenkins jobs to kickoff before the build is declared done.
:slack_build_channel: Specify the name of a slack channel on LSSTC slack to which Jenkins will send job reports, e.g. ``aos-builds``.
:has_doc_site: Does this package have a doc site? If false, skips the ``build and upload documentation`` stage on the CI.
:use_pyside6: Use PySide6 for QT development instead of PySide2?
:require_git_lfs: Does this repository require downloading large data files from git-lfs?
:require_scons: Does this repository require scons to move files in a ``bin.src`` folder to ``bin`` and append them to ``PATH``?

.. literalinclude:: ./Jenkinsfile.example

.. literalinclude:: ./Jenkinsfile.example2

.. note::
    The Jenkins shared library does not use pip to install packages and any dependencies not included in the develop environment must request to be added to the ts-develop conda package.
    You can file a JIRA ticket to make this happen.

* Look through the parameters and make the changes.
* Push your changes.
* Visit https://tssw-ci.lsst.org/view/LSST_TandS/job/LSST_Telescope-and-Site/ and push the ``Scan Organization Now`` button, or wait for Jenkins to notice the new Jenkinsfile.

.. image:: /images/jenkins-scan-organization-now.png
