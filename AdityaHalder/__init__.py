from AdityaHalder.modules.core.dbs import dbb
from AdityaHalder.modules.core.dirs import dirs
from AdityaHalder.modules.core.github import git
from AdityaHalder.modules.core.robot import xdbot
from AdityaHalder.modules.core.client import *
from AdityaHalder.modules.core.sudo import sudo

from .logging import LOGGER


HELPABLE = {}
MOD_LOAD = []
MOD_NOLOAD = []


# Directories
dirs()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Load Sudo Users from DB
sudo()

# Robot Client
robot = xdbot()

# Users Clients
userx = botxd()

# Engine Client
app = self.one
