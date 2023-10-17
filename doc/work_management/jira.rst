.. _Jira_Workflow:

#############
Jira Workflow
#############

.. _Sprints:

Sprints
=======

* Sprints are two weeks long.
* Before each sprint begins (or after the previous sprint), the product owner and the developer will meet to decide what the tasks will be for each sprint.
* Load Sprint tasks on the Monday that starts the Sprint.
* Resolve tasks as soon as possible.
* On the Friday that ends a sprint.

    * Notify Sprint Lead of any tasks that won't be resolved.
    * Notify Sprint Lead why the task won't be resolved.
    * Notify Sprint Lead of time frame work is expected to be resolved.

* Keep commitment to approximately 8 story points (2 weeks).

    * Each sprint assumes 2 story points for meetings and other administrative tasks.


Daily Stand
===========

:Sprint Lead-Scrum Master: Wouter Van Reeven.

* Meetings are in the DKist Conference Room at 10 AM Tucson time M-F except on holidays.

    .. note:: Given the current situation, stand up has now become BlueJeans only for the foreseeable future.

* There is a Blue Jeans connection and that number is located in the tssw_scrum channel as a pinned message.
* Show up on time.
* if you are unable to attend, email/message the Sprint Lead to let them know.

    * For vacations, training, conferences etc, send status update on the last day of work prior to the event.
    * Do not send updates during the event.

* Each person gives current status for around one minute.

    * Update any task that gone to Review or Resolved.
    * Update team on current task in progress.
    * Update team on any issues/roadblocks/concerns for the current task.

* Save detailed information for Parking Lot time.
* After everyone has given status, the Scrum master will ask if anyone wants any parking lot.

Parking Lot
===========

* Begins immediately after the Stand-up meeting.
* Speak with team members that can help with an issue, or are interested in the task.
* Move lengthy conversations to a different room and/or time.

Task Process
============

.. _note:

    Do not create Epics.
    That is the responsibility of the Manager.

* Task creation:

    * Keep task size between 1 and 5 story points.
    
        * If task is a fixed length (i.e. training/conferences/etc.) create one task (see task creation above).
        * Fixed length tasks can be larger than 5 Story Points.

    * If added during a Sprint in progress, notify Sprint Lead if this is out of scope work for the current Sprint.
    * if work is to be completed during the current Epic's time frame, link to the Epic.

        * If not, notify Sprint Lead that a new epic is needed.

    * Required fields to create a task.

        Project:
            Data Management(DM).
        
        Issue Type:
            Task.

        Summary:
            Quick description of the work to be accomplished.

        Assignee:
            Click the Assign to me link.

        Description field:
            * Overview of what the task is to accomplish.
            * List any prerequisites for the task to start or complete.
            * List any Unit tests, if any, for a reviewer to run.

        Story Points:
            Size of task (1-5 SP per task).

        Epic Link:
            Link to the current epic.
            Epic also determines appropriate WBS number to charge on timesheet.

        Team:
            Telescope and Site.

        * Feel free to use any of the other fields, though they are not required.

* Daily task updates:

    * Use the Comment field.
    * Update daily with progress.
    * Update with thoughts to try or test.
    * Update with success/failure when it is tried.
    * Update with any delays in resolving the task.
    * Updated by Reviewers with any findings, or for pass.

* Story Points:

    * Do not change the Story Point size, complete the task as normal.

Task Workflow
-------------

The following diagram shows the TSSW JIRA task workflow.

.. image:: /images/JiraWorkflow.png


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

* Create the ticket branch in the git repos.
  The branch should be named ``tickets/DM-12345``, where ``DM-12345`` is the ticket number assigned by Jira.
  Once the ticket is pushed to GitHub it is automatically linked to the JIRA component ticket.

  * No active development is ever done on the main or develop branches.
  * See :ref:`development-workflow` for more information on the development workflow.

* Write the code.
* Write the unit tests.
* Update any relevant documentation.
* When complete, move to In Review.

  * Complete meaning:

    * Add a link of the PR to the ticket.
    * Unit tests exist, have been successfully run and results have been added to the ticket or PR.
    * Add a link to the generated documentation site.

In Review
---------

* Once the code is complete and all unit tests are passing, initiate a pull request on the develop branch and assign it to the Reviewer(s).
* See :ref:`development-workflow-review-etiquete` for more information on the review etiquete.
* The Reviewer ensures:

  * Code is complete and understandable.
  * CI is passing.
  * Documentation is done, including a reference to the lsst.io site.
  * All requirements, as defined in the ticket description, are met.

* If issues are found:

  * Update Jira with issue.

    Comments on GitHub PR are preferred instead of in the Jira ticket.

  * Sends back to developer:

    If conflicts arise during the review process, developers should reach out to the Scrum Master and/or the Software Architect to seek a conflict resolution.
    If a resolution can't be found the issue can be escalated further to the Product Owner and the Software Manager.

* If no issues are found, the Reviewer approves the PR and moves the Jira ticket to Reviewed with approval/minor changes requested.

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

Review process
==============

* Verify all description requirements are met.
* Verify all acceptance criteria are met.
* Verify quality.
* If making a GitHub PR, you can assign the reviewer as a reviewer for it as well.
* If findings occur:

    * Update comment field with findings.
    * Move to In Progress (Review Fail) - step optional.
    * Notify the task owner.

* If no findings occur, move to Resolved

Bug and Improvement Process
===========================

* Bug and Improvement issues can be created by anybody with access to Jira.
* Use the CSC master table to correctly assign the developer.

* No work will be completed on an issue without approval.
* If a bug or Improvement is identified to be 1 Story Point or more, it will be added to a Sprint when work is started.
* If a Bug or Improvement is less than 1 Story Point, a task will be created with enough issues linked to achieve at least 1 Story Point.
* Work on Bugs and Improvements will follow the standard Task process.

    * See above Task Process.

Closing Process
===============

* JIRA QC access only.
* Verify all work is completed.
* If work is not complete:

    * Update Comment field with findings.
    * Move to Open.
    * Notify the task owner.
