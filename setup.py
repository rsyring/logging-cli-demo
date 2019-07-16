import pathlib

from setuptools import setup, find_namespace_packages

cdir = pathlib.Path(__file__).parent
VERSION_SRC = cdir.joinpath('logging_cli', 'version.py').read_text('utf-8')
version_globals = {}
exec(VERSION_SRC, version_globals)

setup(
    name='Logging CLI Example',
    version=version_globals['VERSION'],
    author='Randy Syring',
    author_email='randy@thesyrings.us',
    packages=find_namespace_packages(include=['logging_cli', 'logging_cli.*']),
    entry_points={
        'console_scripts': [
            'logging-cli=logging_cli.cli:cli',
        ],
    },

)
