##################
Docker Development
##################

Docker is TSSW's preferred method for CSC development.
Docker is a containerization software designed to help application environments maintain consistency between machines.

Installing docker on CentOS
===========================

Docker Install via Docker's repository
--------------------------------------

#. Install required packages

    ..    prompt:: bash
    
        sudo yum install -y yum-utils

#. Set up the stable repository:

    .. prompt:: bash
    
        sudo yum-config-manager \
        --add-repo \
        https://download.docker.com/linux/centos/docker-ce.repo

#. Install the latest version of Docker CE and containerd:

    .. prompt:: bash
     
        sudo yum install docker-ce docker-ce-cli containerd.io 

#. Start Docker (Docker is installed but not started):

    .. prompt:: bash
    
        sudo docker run hello-world

#. Post install

    #. Create the docker group:

        .. prompt:: bash
        
            sudo groupadd docker

    #. Add your user to the docker group:

        .. prompt:: bash
        
            sudo usermod -aG docker $USER

    #. Log out and log back in so that your group membership is re-evaluated.

        If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

    #. Verify that you can run docker commands without sudo:

        .. prompt:: bash
        
            docker run hello-world

Configure Docker with the overlay2 storage driver
-------------------------------------------------

#. Prerequisites

    #. Verify you CentOS is uing 3.10.0-514 of the Linux kernel or higher

        .. prompt:: bash

            uname -s -r

    # Determine filesystem type

        .. prompt:: bash

            df -TH /home

    #. If filesystem is xfs:

        #. Verify that the ftype option is set to 1.

            .. prompt::  bash
            
                xfs_info /home 

        #. If ftype is set to 0, then format the xfs filesystem correctly, use the flag -n ftype=1
            The overlay2 driver is supported on xfs backing filesystems, but only with d_type=true enabled.
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

        .. prompt:: bash
        
            sudo systemctl stop docker

    #. If necessary, copy the contents of the docker root dir(by default:/var/lib/docker) to a temporary location.

        .. prompt:: bash
        
            cp -au /var/lib/docker /var/lib/docker.back

    #. Edit /etc/docker/daemon.json.
        If it does not yet exist, create it.
        Assuming that the file was empty, add the following contents.

        .. code::

            {
            "storage-driver": "overlay2"
            }

        .. note::
            If you wish to change the default docker root dir (recommended, especially if an ext4 filesystem is available), then also add the new path to /etc/docker/daemon.json as follows:

            .. code::

                {
                "data-root":"/new/data/root/path"
                }
                # e.g.
                {
                "data-root":"/home2/docker-base/docker"
                }
    
    #. start Docker

        .. prompt:: bash
        
            sudo systemctl start docker

    #. Verify that the daemon is using the overlay2 storage driver.
        Use the docker info command and look for Storage Driver and Backing filesystem.

        .. code:: 
        
            $ docker info

            # e.g. xfs file system, default Docker Root Dir 

                Containers: 0
                Images: 0
                Storage Driver: overlay2
                Backing Filesystem: xfs
                Supports d_type: true
                Native Overlay Diff: true
                <output truncated>
                Docker Root Dir:/etc/lib/docker
                <output truncated>

            # e.g. ext4 filesystem,

                Containers: 0
                Images: 0
                Storage Driver: overlay2
                Backing Filesystem: extfs
                Supports d_type: true
                Native Overlay Diff: true
                <output truncated>
                Docker Root Dir:/home2/docker-base/docker
                <output truncated>

CSC Development
===============

Template
--------
The first step in developing a new CSC is to create the standard directory tree to store the source code.
For that you can use the `Template generator <https://github.com/lsst/templates>`_ provided by DM which also provides templates for T&S CSCs.

It already includes the possiblity of generating lsst-ts code, setting up the directory tree to follow T&S standard and generates basic eups/scons config files (used for development).
Users can install it locally on their machines (works on MacOS). 
You should run this on your development computer, where you want to store your code, not inside the container.

It is important to understand that development happens on your local computer, using your preferable development tools(PyCharm,Atom,emacs,vim,vi).
Docker will be used to generate the SAl libraries, to run unit tests and run the code.

Pulling the development environment
-----------------------------------

While development happens on your local machine, docker allows you to easily start a fresh environment to build the SAL libaries, run unit tests and the CSC.
The development container is constantly updated with the latest version of the libraries (salobj, sal and xml).

To pull the image, go on the command line and type:

.. prompt:: bash

    docker pull lsstts/develop-env:c010
    docker run -v <your_local_development_folder>:/home/saluser/develop -it lsstts/develop-env:c010

Developing on your own local folder on Docker
---------------------------------------------
To use your own local repository for ts_xml the suggested method is to use eups/setup to replace the repository used by the container by your own.
To do that, assuming you are working on ts_xml that is inside <your_local_development_folder>, and that was mounted inside the container do;

.. prompt:: bash

    cd /home/saluser/develop/ts_xml
    eups declare -r . ts_xml -t $USER 
    setup ts_xml -t $USER 

Once you do that, the command make_salpy_libs will search your local ts_xml repo to build the topics.
You can develop the xml locally on your computer and build the sal libraries with make_salpy_lib.py and they will be available to use inside the container.

In case you want to fall back to the xml inside the container you just need to do:

.. prompt:: bash

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

This way, when you setup your package it will add <repository_root>/bin to the $PATH environment variable and when you run scons, it will copy the scripts in <repository_root>/bin.src to <repository_root>/bin and make them executable.

Creating a Dockerfile
=====================
First clone the `ts_Dockerfiles <https://github.com/lsst-ts/ts_Dockerfiles>`_ repo.
Create a {csc-name} folder.

.. prompt:: bash

    mkdir athexapod

Touch ``Dockerfile`` inside of the folder.

Then use the template provided below to fill the file out.
Change {csc-name} to the name of the CSC.
Change {config_repo} to the name of the configuration repo. 

.. literalinclude:: Dockerfile.template
    :caption: Dockerfile
    :language: dockerfile

Touch ``setup.sh`` inside of the folder.

Then use the template provided below to fill the file out.
Change {csc-name} to the name of the CSC.

.. literalinclude:: setup.sh.template
    :caption: setup.sh
    :language: bash

