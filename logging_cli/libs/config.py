from os import environ

# You can also use files to set these environ variables, see fspaths.py or
# `logging-cli config` output for the location of the file that will be used.
SENTRY_DSN = environ.get('SENTRY_DSN')
LOGGING_USE_SYSLOG = environ.get('LOGGING_USE_SYSLOG', 'yes')
