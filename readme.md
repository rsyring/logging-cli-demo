Logging CLI Demo
========================

This is a small demo app showing how you can integrate Python logging levels with CLI switches.

It also includes:

* Optional Sentry support.  The idea being that you could run commands in cron jobs using the
  "--with-sentry" option and capture any errors for further analysis.
* Logs are, by default, sent to a local syslog server.  Mostly tested on Linux.  YMMV on this and
  you can use the configuration file or CLI options to turn this off.
* Configuration options can be set using environment values or the app's configuration file.

App Setup
---------

1. Assuming Python 3.6+
2. Create/activate a virtualenv
3. `pip install requirements.txt`


Configuration
-------------

Sentry and Syslog behavior can be controlled through the app's configuration file or environment
variables.

Location of the configuration file is OS dependent.  See output of `logging-cli config` for the
location of the file.

The files are read by the [dotenv](https://github.com/theskumar/python-dotenv) library.  Example
file contents:

```
# default values shown
SENTRY_DSN=linode api token

# anything other than "yes" is considered a "no"
LOGGING_USE_SYSLOG=yes
```

Logging Demo
------------

After the above setup, you can run these commands and should get similar output:

```
# logging-cli config
App temp dpath: /tmp/logging-cli
Config file: /home/rsyring/.config/logging-cli
LOGGING_USE_SYSLOG: yes
SENTRY_DSN: None

$ logging-cli log-stuff
ERROR - logging_cli.cli - Logging an error
WARNING - logging_cli.cli - Logging a warning
Logging info

$ logging-cli --quiet log-stuff
ERROR - logging_cli.cli - Logging an error
WARNING - logging_cli.cli - Logging a warning

$ logging-cli --debug log-stuff
DEBUG - logging_cli.libs.logs - Using syslog address: /dev/log
ERROR - logging_cli.cli - Logging an error
WARNING - logging_cli.cli - Logging a warning
INFO - logging_cli.cli - Logging info
DEBUG - logging_cli.cli - Logging debug stuff

# Notice the message about the syslog address goes away, but not due to logging levels, we are
# instead disabling syslog logging.
$ LOGGING_USE_SYSLOG=no logging-cli --debug log-stuff
ERROR - logging_cli.cli - Logging an error
WARNING - logging_cli.cli - Logging a warning
INFO - logging_cli.cli - Logging info
DEBUG - logging_cli.cli - Logging debug stuff
```
