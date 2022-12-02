Development Workflow
====================

The Sprint in which these tasks are placed is defined :ref:`here <procedures/jira:Sprints>`.

Please refer to the TSSW JIRA Workflow diagram above.

Initial/Triage
--------------

* Create a Task, Bug or improvement Jira ticket.
* The initial assignee should triage the ticket.

  * Ensure it is assigned correctly (Assignee, Component , etc)

    * Ensure the ticket is assigned to an actual, currently employed at LSST, person.
    * Each ticket is assigned a JIRA Epic.
    * A label with the name of the component should be added to the ticket.
    * Each ticket is assigned a component that begins with ``ts_``


  * Ensure the Priority is set correctly (Ticket should not have the "Undefined" priority).
  * A Sprint can be chosen at creation (preferably by the person doing the work for this ticket).
    Otherwise the ticket is automatically placed in the Backlog.
    If the ticket is in Backlog, once the sprint is known, the ticket should be updated with the current sprint.
  * The urgent label is reserved for work that impacts nighttime activities at the summit and should be given the utmost priority.

* Once work begins, move the ticket to In Progress

In Progress
-----------

* Create the ticket branch in the git repos
  The branch should be named ``tickets/DM-12345``, where ``DM-12345`` is the ticket number assigned by Jira.
  Once the ticket is pushed to GitHub it is automatically linked to the JIRA component ticket.

  * No active development is ever done on the Main or Develop branches.

* Write the code.
* Write the unit tests.
* Update documentation
* When complete, move to In Review.

  * Complete meaning:

    * Add a link of the PR to the ticket.
    * Unit tests exist, have been successfully run and results have been added to the ticket or PR.
    * Add a link to the generated documentation site.

In Review
---------

* Once the code is complete and all unit tests are passing, initiate a pull request on the develop branch and assign it to the Reviewer(s).
* The Reviewer ensures

  * Code is complete and understandable.
  * CI is passing.
  * Documentation is done, including a reference to the lsst.io site
  * All requirements, as defined in the ticket description, are met.

* If issues are found

  * Update Jira with issue

    * Comments on GitHub PR are preferred instead of in the Jira ticket.

  * Sends back to developer

    * If conflicts arise during the review process, developers should reach out to the Scrum Master and/or the Software Architect to seek a conflict resolution.
      If a resolution can't be found the issue can be escalated further to the Product Owner and the Software Manager.

* If no issues are found

  * The Reviewer approves the PR and moves the Jira ticket to Reviewed with approval/minor changes requested.

Reviewed
--------

* The Developer has a chance to apply minor changes and merges the pull-request.
* The Developer moves the ticket to Done.

Done
----

* The ticket is complete.

  * Feature was successfully implemented.
  * Feature was invalid; proper explanation provided.
  * Ticket was already fixed; proper explanation provided.
