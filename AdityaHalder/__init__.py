from AdityaHalder.modules.core.dbs import dbb
from AdityaHalder.modules.core.dirs import dirs
from AdityaHalder.modules.core.github import git
from AdityaHalder.modules.core.robot import xdbot
from AdityaHalder.modules.core.client import *
from AdityaHalder.modules.core.sudo import sudo

from .logging import LOGGER

HELPABLE = {}

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


# Robot Client Details
robot.name = self.name
robot.username = self.username
robot.id = self.id

# UserBot Account Client Details
tgbot.name = tgbot.name
tgbot.username = tgbot.username
tgbot.id = tgbot.id

# VcBot Account Client Details
vcbot.name = vcbot.name
vcbot.username = vcbot.username
vcbot.id = vcbot.id
