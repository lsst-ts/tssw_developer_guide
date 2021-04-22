##############################
Reporting Work for XML Release
##############################

.. contents::
    :local:

Current Release Tickets
=======================
The individual XML releases are defined as release artifacts on the Releases page from the `CAP <https://jira.lsstcorp.org/projects/CAP>`_ project page.

.. image:: /images/CAP_Project.png

Clicking on the boat icon takes you to the list of releases that are currently available.
The filters (Released, Unreleased and Archived) can be used to look at specific categories of all releases.

.. image:: /images/CAP_Releases.png

Clicking on one of the version names will take you to the status page of that release.
From here you can see progress and the number of tickets in the various lifecycle stages.

.. image:: /images/Release_Status.png

To see the list of tickets in the release, click on the "Issues in version" listing in the ticket status tabs.
Now one can see the tickets that are assigned to this release.

.. image:: /images/Issues_in_Version.png

Now one can determine if a CAP ticket is available to link work tickets into or one needs to be created before linking work tickets.
If you see a potential CAP to use for linking, make sure you read the description and ask questions of the reporter if r necessary to determine if it's the right place for your work.
Just sticking tickets in random locations is not acceptable.
If there is no description on the ticket, please publicly shame the reporter on the #se-software-interact Slack channel to have one written. Make sure to reference the offending ticket.

Creating a CAP Ticket
=====================
If you determine that no current CAP ticket suits your needs, please create one.
You can make it generic so that others might be able to use it to link work, just make sure you have a description that describes your intention for the ticket.
While the ticket creation is a standard process, the one thing to remember is to assign the release artifact during ticket creation.
The "Fix Version/s" field is part of standard ticket types (not Epic) and has a dropdown that shows all releases, both unreleased and released.
Please pick the appropriate unreleased version for the ticket.

.. image:: /images/Create_Ticket.png

Linking Work to a CAP Ticket
============================
If you have found a ticket to use or have created a new one, the work tickets you have in other Jira projects need to be linked to it.
Open the ticket and look for a "Issue Links" section.
If it does not have one, use the "More" dropdown to add one.

.. image:: /images/New_Issue_Links.png

If a ticket already has an "Issue Links" section, you can use the "+" to add a new link.

.. image:: /images/Existing_Issue_Links.png

Please use the "relates to" link qualifier unless you understand what the other ones mean.

Source
======
https://confluence.lsstcorp.org/display/LSSTCOM/Work+Reporting+for+XML+Releases