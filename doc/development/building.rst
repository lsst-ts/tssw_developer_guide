Building Applications
=====================

`Jenkins <https://tssw-ci.lsst.org/>`_ is the chosen Continuous Integration platform.

    * Each application should have a build job in Jenkins.
    * Jenkins chooses which node to execute the builds on.
    * Each build should run the unit tests.
      If the build is successful (including the unit tests), it should generate artifacts that can either be directly deployed or used by other upstream builds to generate deployable artifacts.

For the packaging system, the following applies:

    * Python software should be packed with conda.
    * RPM is a acceptable for C++ and other types of applications (e.g. the middleware).
    * Java code should use maven. (not sure this is true, maybe check with Dave what he does for Tony).
    * Labview is still TBD.
    * For exceptions an RFC ticket is required.
