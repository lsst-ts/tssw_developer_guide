
########################
Tips & Tricks for pytest
########################

-   Run in verbose/no-capture/fail first mode:

    .. prompt::

        pytest -vsx

    v :
        verbose mode shows the result of each test individually

    s :
        no-capture shows results or print statements

    x :
        stop/fail on the first test failure


-   Show log messages:

    .. prompt::

        pytest -vsx --log-cli-level DEBUG

    log-cli-level : 
        controls the log level for the command line at runtime.
        This allows you to see the log messages as the test runs without the need to fiddle with python logger.
        You can also use different levels; INFO, WARNING and ERROR.

-   Run a single test file (e.g. the one you are working on):

    .. prompt::

        pytest -vsx tests/test_maintel_disable_m1m3_balance_system.py


-   Run a single test from a single file (e.g. debugging a specific error):

    .. prompt::

        pytest -vsx tests/test_maintel_disable_m1m3_balance_system.py -k test_executable

    This will actually do a regular expression match in the test name, so it will actually run everything that matches “test_executable”.
