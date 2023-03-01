.. _Jenkinsfile:

Jenkinsfile
===========

* Make a Jenkinsfile using the template below.

.. literalinclude:: ./Jenkinsfile.template

This uses the Jenkins shared library with the following parameters

:name: This is the package name of the csc.
:idl_name: This is the IDL name used to generate the IDL files.
:module_name: This is the namespace path for the package i.e. lsst.ts.csc.
:required_idl: This is an array of IDL file names required beyond the CSC IDL files for building the package.
:build_all_idl: This will build all of the IDL files if true.
:extra-packages: An array of strings in the form of "organization/repo_name/branch" to clone and build that are not already included in the develop environment image.

.. note::
    The Jenkins shared library does not use pip to install packages and any dependencies not included in the develop environment must request to be added to the ts-develop conda package.
    You can file a JIRA ticket to make this happen.

* Look through the parameters and make the changes.
* Push your changes.
* Visit https://tssw-ci.lsst.org/view/LSST_TandS/job/LSST_Telescope-and-Site/ and push the ``Scan Organization Now`` button, or wait for Jenkins to notice the new Jenkinsfile.

.. image:: /images/jenkins-scan-organization-now.png
