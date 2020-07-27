=================
Conda Jenkinsfile
=================

The purpose of this document is to make a how-to for having a conda package build on CI.
This document includes templates for accomplishing this goal.
The first step is to create a conda recipe for a CSC.
The :doc:`conda development guide <conda>` will be helpful.
A template for doing so has been included on this page.

Change the ``csc-name`` so that it becomes the name of the csc.
Another thing is to change requirements so that they match the CSC's.
Keep in mind that the test requirements need to include test framework dependencies.
Also to find the configuration repo, look for the :meth:`get_config_pkg` in the CSC class.

.. literalinclude:: meta.yaml.template
    :language: yaml+jinja

Locally test the recipe by running the following command ``docker run -e {config_repo}=/path/to/config/repo -v /path/to/your/repos:/home/saluser/develop -it lsstts/conda_package_builder``
Then run the following inside of the container.

.. prompt:: bash

    source ~/miniconda3/bin/activate
    source $OSPL_HOME/release.com
    cd path/to/conda/recipe
    conda-build --prefix-length 100 .

Once that is passing, move onto creating the Jenkinsfile.

The next step is to create ``Jenkinsfile.conda`` file.
A template has been included below.
Replace ``csc_name`` with the name of the package/csc.
Replace ``csc_config_repo`` with one of the configuration repos.

.. literalinclude:: Jenkinsfile.conda.template
