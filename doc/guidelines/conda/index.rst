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

Locally test the recipe by running the following command

.. prompt:: bash

    docker run -e {config_repo}=/path/to/config/repo \\
        -v /path/to/your/repos:/home/saluser/develop \\
        -it ts-dockerhub.lsst.org/conda_package_builder

Then run the following inside of the container.

.. prompt:: bash

    cd path/to/conda/recipe
    conda build --variants "{salobj_version: '', idl_version: ''}" --prefix-length 100 .

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
  It can be ``linux-64`` or ``noarch``.
  It may be omitted and defaults to ``linux-64``.
  When specifying ``noarch`` in the conda recipe, this argument *must* be set to ``noarch``.

.. literalinclude:: ./Jenkinsfile.conda.template
    :caption: Jenkinsfile.conda

Adding the Job
==============

Add the job by creating a new item on the Jenkins server and selecting Multibranch Pipeline.

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
