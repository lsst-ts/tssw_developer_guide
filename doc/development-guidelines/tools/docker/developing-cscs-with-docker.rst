.. _developing-cscs-with-docker:

###########################
Developing CSCs with docker
###########################

Philosophy
##########

The procedure adopted by TSSW is to develop/write code on your local computer, using your preferable development tools (VSCode, PyCharm, Atom, emacs, vim, vi, etc).

Docker will be used to generate the SAL libraries, to run unit tests and run the code.
This allows you to get the best development experience, as you develop on your own machine natively and only uses docker to run/test the code.
It also avoids issues with the container exiting and you losing any content that was left in the container.

Pulling the development environment
###################################

While development happens on your local machine, docker allows you to easily start a fresh environment to build SAL libraries, run unit tests and the code.
The development container is constantly updated with the latest version of the libraries (salobj, sal and xml).

To pull the image, go on the command line and type:

.. prompt::
    
    docker pull lsstts/develop-env:develop

This is a pretty large docker image as it contains most of the software one needs to develop TSSW stack (CSCs and SAL Scripts).

The image is updated daily with new software merged during the previous day.
It is good practice to update the image at least once a month.
If you get behind, you may experience various issues (this is usually the first thing we ask when people have issues).

Create a development directory
##############################

Before running the development environment container we recommend creating a directory to host the code you will work on your local machine.
If you already have a directory than skip to the next session.

We recommend using a path like ``~/Develop/tsrepos`` to store the repositories you will be working on from TSSW.
To create this directory you can run the following command in the command line:

.. prompt::

    mkdir -p ~/Develop/tsrepos

Running the container
#####################

Run docker mounting the directory with your code into it:

.. prompt::

    docker run -it --rm --name dev -v ~/Develop/tsrepos/:/home/saluser/tsrepos lsstts/develop-env:develop

The command above will run the container in interactive mode (``-it``), will remove the container once it exits (``--rm``) and will name the container "dev" (``--name dev``).
It is also mounting the local directory ``~/Develop/tsrepos/`` in the ``/home/saluser/tsrepos`` path inside the container.

After executing the command above, you will be in a prompt inside the container.
Any command you type there will be executed by the container, which also contains all the software stack required to test/run the TSSW components.

The container ships with a variety of packages from TSSW and you can also setup your own packages for developing in the container.
To do that you can either use ``eups`` or ``pypi`` to setup the package for development.

For example, if you are working on a project called ``ts_myproject`` and want to set it up in the container, you would first close the repository in the ``~/Develop/tsrepos`` directory from your machine (it is better not to clone the repository from inside the container).
Then you can setup the project using one of the following options:

.. tab-set::

  .. tab-item:: Using eups

    From the container prompt, execute the following sequence:
    
    .. prompt:: bash

        cd /home/saluser/tsrepos/ts_myproject
        eups declare -r . -t $USER
        setup ts_myproject -t $USER

    In the example above replace ``ts_myproject`` with the name of the project you are working on.

  .. tab-item:: Using pypy

    From the container prompt, execute the following sequence:
    
    .. prompt:: bash

        cd /home/saluser/tsrepos/ts_myproject
        python -m pip install -e .

    In the example above replace ``ts_myproject`` with the name of the project you are working on.
    The ``-e`` option used with ``pip`` above install the package in "edit" mode, which basically points python to the code in the repository instead of instructing ``pip`` to install the package in your environment.

Now you should be able to run the unit tests in you project from inside the container.

Known issues
############

File permission in Linux
========================

When using docker in linux the file permissions from the OS are also used inside the containers.
This ends up causing issues if the used id inside the container don't match your user id.
This can be solved by using something called Access Control List(s) or ACL.
First you start by creating a group called saluser with the group id of 73006 and make your user a member of that group.

.. prompt:: bash

	sudo groupadd -g 73006 saluser
	usermod -aG saluser ${USER}

.. note:: You'll need to logout and login again for this change to take effect.

The next step is to change group ownership of the tsrepos to saluser and set the default group set bit so that future files and directory are owned by saluser.

.. prompt:: bash

	chgrp -R saluser ~/Develop/ts_repos/   # This sets the group ownership to saluser for all files and folders under and including ts_repos
	chmod -R g+s ~/Develop/ts_repos/  # This sets the future files and folders created to directory to be under saluser group otherwise it would be your default user group.
	setfacl -d -m -R g:73006:rwX ~/Develop/ts_repos/  # This creates an ACL that allows saluser to have read, write and execute permissions for files and folders under ts_repos, the capital X only sets the executable bit for directories which is safer than every file also be executable with a lower case x
	
Using this method, you can work with the files and folders as bind mounts within both the docker container and as regular storage on your system with no issue.
You would also not lose the changes each time the container is lost for one reason or another(shutdown or power outage).

Another way around this issue is to make sure you user id matches the one in the container.
All develop-env containers are build with saluser with uid:gid=73006:73006.

If you can not change the user/group id in your linux machine, another alternative is to use the container with VSCode extension.
This allows you to open the content of the container is VSCode.
In this case, you need to be careful about committing/pushing your work since the container storage is ephemeral.
You may want to remove the ``--rm`` option in the command shown above to make sure the containers lingers around after it exits.

In this case, you can bring the container up with the command:

.. prompt:: bash

    docker run dev

Where ``dev`` is the name of the container we selected with the ``--name`` option.
