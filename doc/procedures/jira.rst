#########
TSSW Jira
#########

.. todo::

    Update with current information

Stand Up Etiquette
==================

* Meetings are in the DKist Conference Room at 10 AM Tucson time M-F
* There is a blue jeans connection and that number is located in the tssw_scrum channel as a pinned message
* Show up on time
* if you are unable to attend, email/message the Sprint Lead your current status

    * For vacations, training, conferences etc, send status update on the last day of work prior to the event.
    * Do not send updates during the event

* Each person gives current status for one minute

    * Update any task that gone to Review or Resolved
    * Update team on current task in progress
    * Update team on any issues/roadblocks/concerns for the current task

* Save detailed information for Parking Lot time
* After everyone has given status, the Scrum master will ask if anyone wants any parking lot.

Standbot
--------

Standbot is a slack bot that allows for status to be given by answering a series of questions.
Every Monday-Friday of a sprint week, at 9AM Tucson time, standbot will ask for a developer's status.
Once every developer, except for ones that are skipped, answers with status.
Standbot will post status to the slack channel where someone will post the resulting pdf to a `confluence page <https://confluence.lsstcorp.org/display/LTS/Stand-up>`_.

Parking Lot Etiquette
=====================

* Begins immediately after the Stand-up meeting
* Speak with team members that can help with an issue, or are interested in the task
* Move lengthy conversations to a different room and/or time

Sprints
=======

* Sprints are two weeks long
* Before each sprint begins (or after the previous sprint), the product owner and the developer will meet to decide what the tasks will be for each sprint.
* Load Sprint tasks on the Monday that starts the Sprint
* Resolve tasks as soon as possible
* On the Friday that ends a sprint

    * Notify Sprint Lead of any tasks that won't be resolved
    * Notify Sprint Lead why the task won't be resolved
    * Notify Sprint Lead of time frame work is expected to be resolved

* Keep commitment to approximately 8 story points (2 weeks)
* Monthly Retrospective Meetings

    * Go over accomplishments
    * Go over any process issues that can be improved
    * Explain future schedule and path

Task Process
============

* Do not create Epics.
  That is the responsiblity of the Sprint Lead.
* Task creation

    * Keep task size between 1 and 5 story points
    
        * If task is a fixed length (i.e. training/conferences/etc.) create one task (see task creation above)
        * Fixed length tasks can be larger than 5 Story Points

    * If added during a Sprint in progress, notify Sprint Lead if this is out of scope work for the current Sprint
    * if work is to be completed during the current Epic's time frame, link to the Epic

        * If not, notify Sprint Lead that a new epic is needed

    * Required fields to create a task

        Project
            Telescope and Site Software(TSS)
        
        Issue Type
            Task

        Summary
            Quick description of the work to be accomplished

        Component/s
            Appropriate WBS Component in the list

        Assignee
            Click the Assign to me link

        Description field
            * Overview of what the task is to accomplish
            * List any prereqsites for the task to start or complete 
            * List any Unit tests, if any, for a reviewer to run

        Story Points
            Size of task (1-5 SP per task)

        Epic Link
            Link to the current epic

        * Feel free to use any of the other fields, though they are not required

* Daily task updates

    * Use the Comment field
    * Update daily with progress
    * Update with thoughts to try or test
    * Update with success/failure when it is tried
    * Update with any delays in resolving the task
    * Updated by Reviewers with any findings, or for pass

* Story Points

    * Do not change the Story Point size, complete the task as normal

* Move to In Progress state when work begins

    * Attach any relevant documents or notes

* Move to In Review state once work is complete.

    * Assign the appropriate reviewer(s)

Review process
==============

* Verify all description requirements are met
* Verify all acceptance criteria are met
* Verify quality
* If findings occur

    * Update comment field with findings
    * Move to In Progress (Review Fail)
    * Notify the task owner

* If no findings occur

    * Move to Resolved

Bug and Improvement Process - (unofficial)

* Bug and Improvement issues can be created by anybody with access to Jira
* Scrum master will be assigned all Bugs and Improvements for triage

    * Scrum master will change assignee

* Bugs and Improvements will be prioritized and approved through an Issue Triage team

    * Attendees TBS
    * Triage team will indentify which developer/subsystem will be tasked with the issue

* No work will be completed on an issue without approval
* If a bug or Improvement is indentified to be 1 Story Point or more, it will be added to a Sprint when work is started
* If a Bug or Improvement is less than 1 Story Point, a task will be created with enough issues linked to achieve at least 1 Story Point
* Work on Bugs and Improvements will follow the standard Task process

    * See above Task Process

Closing Process
===============

    * JIRA QC access only
    * Verify all work is completed
    * If work is not complete
        
        * Update Comment field with findings
        * Move to Open
        * Notify the task owner

    * if work is complete

        * Move to Closed