.. _installing_docker_on_centos:

###########################
Installing docker on CentOS
###########################

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

