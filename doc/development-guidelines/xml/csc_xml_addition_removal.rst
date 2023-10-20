
.. _adding_or_removing_a_csc_from_the_xml_interface:

###############################################
Adding or Removing a CSC from the XML Interface
###############################################

The following document lays out the procedure for adding or removing a CSC from the XML interface.
There are also instructions on the workflow to update an version of OpenSplice.

Add/Rename a CSC
================
#. A subsystem representative must announce the intention to add a new or rename an existing CSC at the weekly CAP meeting.
#. A new CAP Jira ticket must be created.
   Using established CAP tickets is not permitted
#. The Summary for the ticket must start with the following text: (ADD) if adding or (RENAME) if renaming.
#. The ticket must contain the following label: add_csc if adding or rename_csc if renaming
#. The ticket must be tied to the XML version where the new or renamed CSC will be added.
#. Work on the new CSC proceeds as normal

Remove a CSC
============
#. A subsystem representative must announce the intention to remove an existing CSC at the weekly CAP meeting.
#. A new CAP Jira ticket must be created.
   Using established CAP tickets is not permitted.
#. The Summary for the ticket must start with the following text: (REMOVE)
#. The ticket must contain the following label: remove_csc
#. The ticket must be tied to the XML version where the CSC will be removed.
#. Work on removing the CSC proceeds as normal

Changing the OpenSplice Version
===============================
#. A subsystem representative must announce the intention to update the openSplice version at the weekly CAP meeting.
#. A new CAP Jira ticket must be created.
   Using established CAP tickets is not permitted.
#. The Summary for the ticket must start with the following text (UPDATE OPENSPLICE)
#. The ticket must be tied to opensplice version that we are updating to.
#. Work on updating openSplice proceeds as normal.

Before Release Procedure
========================
Before it is time to perform the XML release, the XML Work Coordinator and Build/Release Coordinator must meet to review the release tickets.
This will ensure that added or removed CSCs will be properly addressed heading into the build process.
