=================
Conda Jenkinsfile
=================

This example is pretty much ready to go.
Replace `csc_name` with the name of the package/csc.
Replace `ts_config_{name_of_config}` with one of the configuration repos.
For more general information read `TSTN-003 <https://tstn-003.lsst.io>`_.


.. code::

    pipeline {
    agent any
    environment {
        package_name = "{csc_name}"
        dockerImageName = "lsstts/conda_package_builder:latest"
        container_name = "conda_${BUILD_ID}_${JENKINS_NODE_COOKIE}"
    }

    stages {
        stage("Pull Docker Image") {
            steps {
                script {
                sh """
                docker pull ${dockerImageName}
                """
                }
            }
        }
        stage("Start builder"){
            steps {
                script {
                    sh """
                    docker run --name ${container_name} -di --rm \
                        --env TS_CONFIG_{name_of_config}_DIR=/home/saluser/ts_config_{name_of_config} \
                        --env LSST_DDS_DOMAIN=citest \
                        -v ${WORKSPACE}:/home/saluser/source ${dockerImageName}
                    """
                }
            }
        }
        stage("Clone ts_config_{name_of_config}"){
            steps {
                script {
                    sh """
                    docker exec ${container_name} sh -c "git clone https://github.com/lsst-ts/ts_config_{name_of_config}.git"
                    """
                }
            }
        }
        stage("Create Conda package") {
            when {
                buildingTag()
            }
            steps {
                script {
                    sh """
                    docker exec ${container_name} sh -c 'cd ~/source/conda && source ~/miniconda3/bin/activate && source "\$OSPL_HOME/release.com" && conda build --prefix-length 100 .'
                    """
                }
            }
        }
        stage("Create Conda Dev package") {
            when {
                not {
                    buildingTag()
                }
            }
            steps {
                script {
                    sh """
                        docker exec ${container_name} sh -c 'cd ~/source/conda && source ~/miniconda3/bin/activate && source "\$OSPL_HOME/release.com" && conda build -c lsstts/label/dev --prefix-length 100 .'
                    """
                }
            }
        }

        stage("Push Conda Release package") {
            when {
                buildingTag()
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'CondaForge', passwordVariable: 'anaconda_pass', usernameVariable: 'anaconda_user')]) {
                    script {
                        sh """
                        docker exec ${container_name} sh -c "source ~/miniconda3/bin/activate && \
                            anaconda login --user ${anaconda_user} --password ${anaconda_pass} && \
                            anaconda upload -u lsstts --force \
                            ~/miniconda3/conda-bld/linux-64/ts-${package_name}*.tar.bz2"
                        """
                    }
                }
            }
        }
    }
    post {
        cleanup {
            sh """
            docker stop ${container_name}
            """
        }
    }
    }

Just change the set name to whatever the package name is.
Add and change the dependencies to match your package.

.. code::

    {% set data= load_setup_py_data() %}
    {% set name= "ts-athexapod" %}
    package:
    name: {{ name }}
    version: {{ data.get('version') }}

    source:
    path: ../

    build:
    script: python -m pip install --no-deps --ignore-installed .
    script_env:
        - PATH
        - PYTHONPATH
        - LD_LIBRARY_PATH
        - OSPL_HOME
        - PYTHON_BUILD_VERSION
        - PYTHON_BUILD_LOCATION
        - TS_CONFIG_ATTCS_DIR
        - LSST_DDS_DOMAIN

    test:
    requires:
        - pytest
        - pytest-flake8
        - pytest-cov
        - asynctest
        - numpy
        - astropy
        - jsonschema
        - pyyaml
        - boto3
        - moto
        - ts-dds
        - ts-idl
        - ts-salobj
    source_files:
        - python
        - bin
        - tests
        - schema
        - setup.cfg
    commands:
        - py.test

    requirements:
    host:
        - python
        - pip
        - setuptools_scm
        - setuptools
        - pytest-runner
    run:
        - python
        - setuptools
        - setuptools_scm
        - ts-salobj
        - ts-idl
