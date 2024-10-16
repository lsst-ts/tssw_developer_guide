.. _Conda:

#####
Conda
#####

The purpose of this document is to make a how-to for having a conda package build on Jenkins.
This document includes templates for accomplishing this goal.
The first step is to create a conda recipe for a CSC.
A template for doing so has been included on this page.


Creating the Recipe
===================

Create a ``conda`` folder inside the root directory CSC repository.
Then copy the contents of the meta.yaml template into a :file:`meta.yaml` file inside of the ``conda`` folder.
Change the ``csc-name`` so that it becomes the name of the csc.
Another thing is to add requirements so that they match the CSC's.
Keep in mind that the test requirements need to include test framework dependencies.
It is suggested to sort dependencies as that increases readability of the recipe.
To find the configuration repo, look for the :meth:`get_config_pkg` in the CSC class.

.. literalinclude:: ./meta.yaml.template
    :language: yaml+jinja
    :caption: meta.yaml

Locally test the recipe in the develop-env:develop image by using the following

.. prompt:: bash

    unsetup ts_config_{package} # this is required otherwise the EV will not picked up correctly by conda build
    cd path/to/package/root
    TS_CONFIG_PACKAGE_DIR=~/saluser/repos/ts_config_package conda build --variants "{salobj_version: '', idl_version: ''}" --no-long-test-prefix .

Creating the Jenkinsfile
========================

Once that is passing, move onto creating the ``Jenkinsfile.conda`` file.
A template has been included below.
It takes the following arguments

:configuration_repo: A list of configuration repos, can be empty, one or many.
:package_name: The name of the package.
:module_namespace: This is the namespace location for the module, for the coverage extension.
:arch:

  This is the architecture of the conda package to create.
  It can be ``linux-64``, ``aarch64`` or ``noarch``.
  It may be omitted and defaults to ``linux-64``.
  When specifying ``noarch`` in the conda recipe, this argument *must* be set to ``noarch``.

:upload_dev:

  This specifies if dev packages should be uploaded to the conda repo or not.
  It defaults to ``false`` which means that the dev packages will not be uploaded.
  This is in line with the TSSW conda policy.
  In some cases where a package represents a library that other packages may use, like ts-tcpip and ts-utils, it should be set to ``true``.

.. literalinclude:: ./Jenkinsfile.conda.template
    :caption: Jenkinsfile.conda

Adding the Job
==============

Add the job by creating a new item on the Jenkins server and selecting Multibranch Pipeline.

The Daily Workflows assume that Conda packaging jobs follow a very specific naming convention. The name should begin with a meaningful string, usually the package name, with NO special character. The rest of the job name should just be the string ``_conda_package``, i.e.

``<PackageName>_conda_package``

This ensures the job is displyed in the ``Conda Jobs`` view in Jenkins, as well included in the Daily Workflows, once the broker job is updated to add this new Conda packaging build. Simply make a request to the build engineer to get the job added properly.

.. image:: /images/jenkins-conda-adding-the-job-0.png

In ``Branch Sources`` click the github source selection and type in the path of the repo into the ``Respository HTTPS URL``.

.. image:: /images/jenkins-conda-adding-the-job-1.png

Then in the behaviors subsection click the ``add`` button and find the ``Custom GitHub Notification Context`` behavior.

.. image:: /images/jenkins-conda-adding-the-job-2.png

Check the ``Apply Suffix`` box and in the label field add ``/conda`` to the end of the value.

Then in ``Build strategies`` click the ``add`` button and find the ``Tags`` strategies and leave the default values.

.. image:: /images/jenkins-conda-adding-the-job-3.png

Then in ``Build Configuration`` add ``.conda`` to the ``Script Path`` field.

.. image:: /images/jenkins-conda-adding-the-job-4.png

Then click ``Apply`` and ``Save``.


.. warning::
    If your job has a build strategy for regular branches, remove it as these jobs are not yet ready to be run on PR or branches.
