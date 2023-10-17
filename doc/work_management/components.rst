###################
Component Resources
###################

* In this context, a component is a logical grouping of code. A CSC (Configurable SAL Component) or a set of hardware testing code can be considered an component.
  A component may consist of many applications (i.e. CSC created from the LabVIEW component template).
* Internal Libraries, tools and similar items will NOT be considered components.
  However, they should have documentation that outlines their functionality.
  Components using this functionality should be linked to the CSC's documentation site.
* Requirements & Schedule of the component is determined by the :term:`Product Owner` & the Component Developer.
  These two must work in tandem to determine what the resulting component shall be.
  There is a :ref:`bi-weekly sprint planning meeting <Jira_Workflow>` to help facilitate this process.
* Each application should have an unrestricted, high-level lsst.io site that defines and/or contains:

  * Release roadmap
  * Developer & User Guide/Manuals
  * Dependencies
  * Reverse chronological order of releases, linked to Detailed Release Notes
  * Github repository link
  * Jenkins build project
  * Link to Jira issues

* These pages should be stored under a TBD hierarchy.
* Detailed Release Notes should be part of the documentation site as well.

  * Create a page for the next release as soon as work begins

    * Keep up-to-date as development progresses.

  * As part of release announcement, make this page public.

* A template has been produced for the format above which every application should follow.

Component Roles
###############

Each Component should have the following roles occupied

.. glossary::

  CAM/Stakeholder
    customer or user base for component

  Product Owner
    Product owner definition here: `TSS Product Owner <https://confluence.lsstcorp.org/display/LTS/TSS+Product+Owner>`__.

  Lead Developer
    Main developer for the component

  Backup Developer
    developer to take over if the Lead Developer wins the lottery and runs away.

  SW Manager
    Personnel who can decide resolution, if there is conflict with the four roles above.

The Component has most of this information defined in the Main CSC table on `ts_xml <https://ts-xml.lsst.io>`__.
