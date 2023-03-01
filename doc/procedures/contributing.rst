#########################
Contributing to This Site
#########################

This page describes how to contribute to this site.

This guide is open source licensed under `Creative Commons Attribution 4.0 International <https://creativecommons.org/licenses/by/4.0/legalcode>`_ and `located on github <https://github.com/lsst-ts/tssw_developer_guide>`_.

It is written in RST format and built with sphinx.
It uses `documenteer <https://documenteer.lsst.io>`_ as its build tool chain.
This guide assumes use of the develop-env container.
In order to build the documentation locally, use the following command ``package-docs build``.
If making an improvement or fixing an issue, then file a ticket according to the :doc:`/procedures/jira` procedure.
Then use the :doc:`documentation guide </guidelines/documentation-guide>` as a starting point for writing your content.

This site is meant for documenting information that is considered pertinent to a Telescope and Site Software Developer.
This information could also be helpful for those outside of that team as well.
This documentation is divided into folders which contain big ideas.
Each folder contains a page on a given topic.

* Conda
  
  * Contains topics on how the team uses the conda package manager as part of the build and deployment cycle

* Deployment
  
  * Topics about deployment of software

* Development
  
  * Topics about development tutorials and procedures

* Docker
  
  * Topics about docker tutorials

* Language
  
  * Guides for each programming language that the team uses

* Procedures
  
  * General procedures for the team that fall outside of the other categories

This documentation uses the Project/DM standard writing style guide which is a modified `Google Developer Style Guide <https://developers.google.com/style/>`_ with the modifications listed in :doc:`dm_developer_guide:user-docs/lsst-specific-content-style-guide`
