from pathlib import Path
import tempfile

from appdirs import AppDirs

# diretory path to the top-level python module
pymod_dpath = Path(__file__).parent.parent
project_dpath = pymod_dpath.parent

app_tmp_dpath = Path(tempfile.gettempdir()) / 'logging-cli'

# AppDirs will give us the correct location for cross-platform output.
# See `logging-cli config` for
# the location of this file on your system.
_appdirs = AppDirs('logging-cli')
config_fpath = Path(_appdirs.user_config_dir)
