import logging

import click
from dotenv import load_dotenv

from logging_cli import version

from logging_cli.libs import (
    config,
    logs,
    fspaths,
)


log = logging.getLogger(__name__)


@click.group()
@click.option('--quiet', 'log_level', flag_value='quiet')
@click.option('--info', 'log_level', flag_value='info', default=True)
@click.option('--debug', 'log_level', flag_value='debug')
@click.option('--with-sentry', is_flag=True, default=False)
@click.option('--use-syslog/--no-syslog', default=None)
def cli(log_level, with_sentry, use_syslog):
    if fspaths.config_fpath.exists():
        load_dotenv(fspaths.config_fpath)

    # if the flag isn't set, take it from the config value
    if use_syslog is None:
        use_syslog = config.LOGGING_USE_SYSLOG == 'yes'

    logs.init_logging(log_level, use_syslog)

    if with_sentry:
        if not config.SENTRY_DSN:
            log.error('Sentry DSN expected but not configured.')
        import sentry_sdk
        sentry_sdk.init(config.SENTRY_DSN)


@cli.command('log-stuff')
def log_stuff():
    log.error('Logging an error')
    log.warning('Logging a warning')
    log.info('Logging info')
    log.debug('Logging debug stuff')


@cli.command('version')
def _version():
    print('Version:', version.VERSION)


@cli.command('config')
def _config():
    print('App temp dpath:', fspaths.app_tmp_dpath)
    print('Config file:', fspaths.config_fpath)
    for varname in sorted(dir(config)):
        if varname.isupper():
            print(f'{varname}:', getattr(config, varname))


if __name__ == '__main__':
    cli()
