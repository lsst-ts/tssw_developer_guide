.. _documentation-guide:

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

Conf.py
=======
The conf.py file is a Sphinx configuration file that contains information on Sphinx should build the site as well as any extensions that should be loaded. 
You can find the template conf.py at https://github.com/lsst-ts/cookiecutter_tssw_csc_doc/blob/90c866162936f4d31d5fb1e1684e17a75128765d/%7B%7Bcookiecutter.doc%7D%7D/conf.py.
Documenteer is a tool that provides pre-made Sphinx configurations for 3 different purposes that SQRE provides the project.

1. pipelines
2. guide
3. technote

It also provides several project extensions for the RSP packages.
All documentation is available at https://documenteer.lsst.io.

..
    Remove with DM-44045.

The template does not yet provide compatibility with documenteer 1.0 and above.
See the :ref:`development-guidelines/documentation-guide:Documenteer configuration` section for how to accomplish this.

Publishing lsst.io Site
=======================

This functionality is included in the DevelopPipeline for the Jenkins Shared Library.

Documenteer Configuration
=========================

..
    Remove with DM-44045.

.. note:: The following section is for older doc folders to move the new system provided by documenteer 1.0 and above.
    In the future, this section will be removed once the doc template is updated.

Create a documenteer.toml file using https://documenteer.lsst.io/guides/toml-reference.html as reference material.
A basic documenteer.toml example is provided below.

.. literalinclude:: ./documenteer.toml.example

You also need to change first line in conf.py to import from the guide config with

.. code:: python

    from documenteer.conf.guide import *

