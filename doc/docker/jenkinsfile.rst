##################
Deploy Jenkinsfile
##################

.. warning:: Not ready for actual usage

It is assumed that a dockerfile is already written.

The deploy Jenkinsfile is meant to build the final docker image for deploying the CSC.
The procedure is to build the image based on ticket branch, develop or master.
Then pushes the image to DockerHub and the LSST Nexus 3 Docker Registry if it is public or only to the Nexus 3 Docker Registry if it is private.

Begin by touching a ``Jenkinsfile.deploy`` in the root CSC repo.
Then change the ``dockerImageName*`` variables to contain the name of the csc package i.e. ``ts-atdome`` inside of ``lsstts/ts-atdome:master``
The Parameters section is for handling versions of system-wide dependencies such as ts-salobj and ts-idl in order to maintain working containers.
It is likely that those values will be different for each CSC.
However, they will change given time.

.. note:: PLACEHOLDER

.. .. literalinclude:: Jenkinsfile.docker.template
    :caption: Jenkinsfile.deploy
