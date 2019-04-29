CSC Development
===============
:author: Tiago Ribeiro

Template
--------
The first step in developing a new CSC is to create the standard directory tree to store the source code.
For that you can use the Template generator provided by DM which also provides templates for T&S code.

You can find the template generator in this link: https://github.com/lsst/templates

It already includes the possiblity of generating lsst-ts code, setting up the directory tree to follow T&S standard and generates basic eups/scons config files (used for development).
Users can install it locally on their machines (works on MacOS). 
You should run this on your development computer, where you want to store your code, not inside the container.

It is important to understand that development happens on your local computer, using your preferable development tools(PyCharm,Atom,emacs,vim,vi).
Docker will be used to generate the SAl libraries, to run unit tests and run the code.

Pulling the development environment
-----------------------------------

While development happens on your local machine, docker allows you to easily start a fresh environment to build SAL libaries, run unit tests and the code.
The development container is constantly updated with the latest version of the libraries (salobj, sal and xml).
For help contact Tiago Ribeiro.

Do pull the image, go on the command line and type:

.. code::

    docker pull lsstts/develop-env:latest
    docker run -v <your_local_development_folder>:/home/saluser/develop -it lsstts/develop-env:latest

You can build SALPY libraries by typing `make_salpy_libs.py <name> [<name2>...]` which will build them and install in a location where they are immediately usable (ts_sal/lib for the C++ library and ts_sal/python for the SALPY library).

On the second command (docker run) the option -v <your_local_development_folder>:/home/saluser/develop will mount a folder on your computer inside the "develop" folder of the container.
This is how you enable docker to access the code you will be developing.

Developing on your own local folder on Docker
---------------------------------------------
To use your own local repository for ts_xml the suggested method is to use eups/setup to replace the repository used by the container by your own.
To do that, assuming you are working on ts_xml that is inside <your_local_development_folder>, and that was mounted inside the container do;

.. code::

    cd /home/saluser/develop/ts_xml
    eups declare -r . ts_xml -t $USER 
    setup ts_xml -t $USER 

Once you do that, the command make_salpy_libs will search your local ts_xml repo to build the topics.
You can develop the xml locally on your computer and build the sal libraries with make_salpy_lib.py and they will be available to use inside the container.

In case you want to fall back to the xml inside the container you just need to do:

.. code::

    setup ts_xml -t current

Running scons and CSC Unit tests
--------------------------------

For unit tests that uses sal to run properly with scons you need to modify the file <repository_root>/tests/SConscript to have something like this:

.. code::

    #-*- python -*-
    import os 

    from lsst.sconsUtils import env, scripts
    scripts.BasicSConscript.tests(pyList=[])

    for name in ("OSPL_URI", "OPENSPLICE_LOC"):
        val = os.environ.get(name)
        if val is not None:
            env.AppendENVPath(name,val)

Adding executables to your repository
-------------------------------------

You can add an executable script to your repository to initialize your CSC.
To do that, add the script to the directory <repository_root>/bin.src and add the following to the file <repository_root>/ups/<repository_name>.table

.. code::

    envPrepend(PATH, ${PRODUCT_DIR}/bin)

This way, when you setup your package it will add <repository_root>/bin to the $PATH environment variable and when you run scons, it will copy the scripts in <repository_root>/bin.src to <repository_root>/bin and make them executables.

Installing docker on CentOS
===========================

:author: James Bufill

Docker Install via Docker's repository
--------------------------------------

#. Install required packages

    > $ sudo yum install -y yum-utils

#. Set up the stable repository:

    > $ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

#. Install the latest version of Docker CE and containerd:

    $ sudo yum install docker-ce docker-ce-cli containerd.io 

#. Start Docker (Docker is installed but not started):

    $ sudo docker run hello-world

#. Post install

    #. Create the docker group:

        $ sudo groupadd docker

    #. Add your user to the docker group:

        $ sudo usermod -aG docker $USER

    #. Log out and log back in so that your group membership is re-evaluated.

        If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

    #. Verify that you can run docker commands without sudo:

        $ docker run hello-world

Configure Docker with the overlay2 storage driver
-------------------------------------------------

#. Prerequisites

    #. Verify you CentOS is uing 3.10.0-514 of the Linux kernel or higher

        $uname -s -r

    # Determine filesystem type

        $ df -TH /home

    #. If filesystem is xfs:

        #. Verify that the ftype option is set to 1.

            $ xfs_info /home 

        #. If ftype is set to 0, then format the xfs filesystem correctly, use the flag -n ftype=1 ***
            *** The overlay2 driver is supported on xfs backing filesystems, but only with d_type=true enabled.
            (d_type == "directory entry type"; used by Linux kernel to describe the information of a directory on the filesystem)

        #. Easier option, if available, is to configure Docker to point to an ext4 mounted filesystem.

            .. note::
                You may format the filesystem and mount it into /var/lib/docker (the default docker daemon (root) dir) or with a name of your liking.

                    e.g. filesystem: /dev/sdb1 mounted on: /home2 and docker root dir set to:/home2/docker-base/docker

                Make sure add this mount to /etc/fstab to make it permanent.

                    e.g. entry in /etc/fstab:/dev/sdb1 /home2 ext4 defaults 0 0

        #. If filesystem is ext4, nothing more to do.

#. Configuration

    #. Stop Docker

        $ sudo systemctl stop docker

    #. If necessary, copy the contents of the docker root dir(by default:/var/lib/docker) to a temporary location.

        $ cp -au /var/lib/docker /var/lib/docker.back

    #. Edit /etc/docker/daemon.json.
        If it does not yet exist, create it.
        Assuming that the file was empty, add the following contents.

        {
        "storage-driver": "overlay2"
        }

        .. note::
            If you wish to change the default docker root dir (recommended, especially if an ext4 filesystem is available), then also add the new path to /etc/docker/daemon.json as follows:

                {
                "data-root":"/new/data/root/path"
                }
                e.g.
                    {
                    "data-root":"/home2/docker-base/docker"
                    }
    
    #. start Docker

        $ sudo systemctl start docker

    #. Verify that the daemon is using the overlay2 storage driver.
        Use the docker info command and look for Storage Driver and Backing filesystem.

        $ docker info

            e.g. xfs file system, default Docker Root Dir 

                Containers: 0
                Images: 0
                Storage Driver: overlay2
                Backing Filesystem: xfs
                Supports d_type: true
                Native Overlay Diff: true
                <output truncated>
                Docker Root Dir:/etc/lib/docker
                <output truncated>

            e.g. ext4 filesystem,

                Containers: 0
                Images: 0
                Storage Driver: overlay2
                Backing Filesystem: extfs
                Supports d_type: true
                Native Overlay Diff: true
                <output truncated>
                Docker Root Dir:/home2/docker-base/docker
                <output truncated>

SAL Development
===============
:author: Russell Owen

.. note::
    These instructions are useful for those planning on developing SAL with the development container.

This is my personal take on the best way for software developers to run the lsst/queue Docker container. 
My emphasis is keeping all code and generated SALPY libraries on your own disk, so changes persist between invocations of the docker container.
This lets you pick and choose which version of the package you want to use, upgrade whenever you like, and use your favorite tools for editing code and managing git.
The down side is you have to build all the telescope and site packages that you want to use yourself.
This is not intended for deployment!

* Install Docker, start it running and log into your Docker account.
* `docker pull lsst/queue:develop`
* Make sure you have a single directory that contains git clones of all of the Telescope and Site github repositories that you use.
  This should include ts_sal, ts_xml and ts_salobj at a minimum, ts_scriptqueue, ts_standardscripts and ts_externalscripts are also likely to be useful, plus any other packages you are working on or using.
  I will refer to this directory as <your_tsrepos>.
* Create a directory tree <your_tsrepos>/docker/queue (in other words mkdir <your_tsrepos>/docker and then mkdir <your_tsrepos>/docker/queue).
  Having the hierarchy makes it easy to add fixup scripts for other docker containers.
* Put the attached setup.sh script into <your_tsrepos>/docker/queue
* If you wish to use the built in version of ts_xml, ts_sal, ts_salobj or ts_scriptqueue then edit your setup.sh to not declare those.
  Be careful about dependencies: built in packages should use only other built in packages.
* Put the attached setup.env file into <your_tsrepos>/docker/queue
* Edit setup.sh to remove the "eups declare" and "setup" lines for any packages you don't want and to add any packages you do want.
  You should have a one-to-one mapping between packages you "eups declare" and "setup" and those that you have git cloned in <your_tsrepos>
* Put the following into your `~/.bashrc` file so you can easily run the lsst/queue Docker container.
  There is nothing magic about `--name queue`, and indeed if you want to have more than one lsst/queue container running at the same time you must assign a unique name to each one.

  alias runqueue="docker run -it --rm --name queue \
  -v $HOME/.config:/home/saluser/.config \
  -v <your_tsrepos>:/home/saluser/tsrepos \
  lsst/queue \
  /home/saluser/tsrepos/docker/queue/setup.sh
* This shares your .config dir so your Docker container can find your standard flake8 config.
  I have attached my ~/.config/flake8 file, which matches LSST standards. 
  .. warning::
    It will download with an extension ".dms" which you should remove, so the final name is just "flake8".

* To get started with your Docker container, in a fresh terminal session type the following:

    $ runqueue
    $ cd tsrepos/ts_...
    $ scons

This will build Test and Script SALPY libraries and run the unit tests.
Note that having scons build SALPY libraries is unique to ts_sal (because proving that libraries can be built is an important test in its own right). 
For other ts_packages you have to build the libraries you want before running unit tests.

* To build the SALPY libraries for any other package, use the `make_salpy_libs.py` command.
  This puts the libraries where the ts_packages can find them.
  For example make_salpy_libs ScriptQueue ATMCS ATDome ..
* Build the SALPY libraries for any other packages(s) you want to use.
  You only have to do this once, unless a package changes.

    * Check out whatever version of ts_xml you want to use (you can do this outside of inside the Docker container; I prefer outside).
    * `make_salpy_libs.py <name1> <name2>... e.g. make_salpy_libs ScriptQueue ATMCS ATDome`

* Build all the packages you depend on (this is where using lsst/queue with the included packages is a win, since they're already built).
  For each package:

    * Check out the version you want to build (again you can do this inside or outside the container)
    * In your Docker container:

        * `cd tsrepos/ts_<name>`
        * # setup -r . # not necessary if you declared and setup the package in docker/queue/setup.sh
        * scons

* At this point you should be good to go.
  You can run any of your packages.
  And if you quit Docker and start it again, all the SALPY libraries you built and all the code you checked out will be in the same state it was.
  Your packages will still be built.
* To work on a package you can do all your editing and git with your favorite tools outside your docker container.
  Just use the Docker container to build the software and run unit tests.

Docker
======
:author: Eric Coughlin
Docker is a container(specialized vm) builder which allows for the deployment of applications in exact(specified)
conditions.
It is very helpful in allowing applications to be developed and therefore deployed in the ideal working conditions.
Docker is certainly an excellent tool for helping to run our applications under the right circumstances.
Please see the link to documentation `here <https://docs.docker.com/>`__.
Docker images can be uploaded to image repositories which allow users to docker pull images using their docker client.
One such repository is dockerhub, which is the official docker repository for hosting this images.
LSST has several of its teams located on docker hub.
Our team has a docker hub located under organization lsstts.
Ask one of the team members for access to it in order to push images to it.
One useful feature of docker is that Jenkins integrates very nicely with it.
When running a Jenkins pipeline, a docker image can be used as the build agent without affecting the master system
running Jenkins.
This means that developers will have an easier time getting their builds completed with Jenkins by using docker
containers.

Docker for Windows
------------------
Docker for Windows is nice to use provided you are an administrator account or have the ability to add yourself to
the docker group.
Otherwise permissions will become the bane of your existance as running any docker commands require administrator
privileges and volume mounting requires setup by LSST IT.

Docker on Linux VM
------------------
Docker can be installed on a linux vm because of the way that virtualization works on the linux kernel.
If you are running a windows/mac host and have a virtualbox VM running any recent linux distro this should work for
you.
In this example, we will assume that the host system is Windows 10 and that the VM is a virtualbox CentOS 7 machine.
We will also assume that you have a virtual machine up and running in this case.

#. Setup docker repos

    #. install prerequisites
        .. code-block:: bash

            sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    #. Add docker repo to yum
        .. code-block:: bash

            sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

#. Install docker-ce
    .. code-block:: bash

        sudo yum install docker-ce

#. Start docker service
    .. code-block:: bash

        sudo systemctl start docker
        # Optional
        sudo systemctl enable docker # this will allow the docker daemon to start when the OS starts

.. seealso::
    https://docs.docker.com/install/linux/docker-ce/centos/