###################
Documentation Guide
###################

This topic outlines writing and creating TSSW documentation.

RST Guide
=========

Use :doc:`DM's Restructured Text Style Guide <dm_developer_guide:restructuredtext/style>` for reference.

Doc Folder Template
===================
`cookiecutter_tssw_csc_doc <https://github.com/lsst-ts/cookiecutter_tssw_csc_doc>`_ is a template meant to help start working on documentation for CSCs.
The following steps will explain how to use it.

.. prompt:: bash

    pip install cookiecutter # Install cookiecutter in the virtual environment of the development docker image
    cd {csc_root_folder} # change directory into your csc folder
    cookiecutter https://github.com/lsst-ts/cookiecutter_tssw_csc_doc
    doc [doc]: # The name of the folder where the documentation goes, this option should only be changed if the standard folder name is changed.
    csc_name [Barracuda]: # the name of the CSC, affects things like api generation, xml badge location
    csc_repo_name [ts_barracuda]: # The name of the repo should include ``ts_`` or ``dm_``, affects things like the badges for JIRA, GitHub and Jenkins

Once those three questions are answered then a brand new doc folder will be added to the CSC.
Inside of the files, there are comments that explain how to fill out each section in detail.

Publishing lsst.io Site
=======================

This functionality is included in the DevelopPipeline for the Jenkins Shared Library.
