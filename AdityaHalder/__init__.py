from AdityaHalder.modules.core.dbs import dbb
from AdityaHalder.modules.core.dir import dirs
from AdityaHalder.modules.core.git import git
from AdityaHalder.modules.core.robot import xdbot, self
from AdityaHalder.modules.core.client import botxd, tgbot, vcbot
from AdityaHalder.modules.core.sudo import sudo

from .logging import LOGGER

HELPABLE = {}

# Robot Client Details
getmebot = self.get_me()

if getmebot.last_name:
 BOT_NAME = getmebot.first_name + " " + getmebot.last_name
else:
 BOT_NAME = getmebot.first_name

BOT_UNAME = getmebot.username
BOT_USERID = getmebot.id

# UserBot Account Client Details
getmecli = tgbot.get_me()

if getmecli.last_name:
 CLIBOT_NAME = getmecli.first_name + " " + getmecli.last_name
else:
 CLIBOT_NAME = getmecli.first_name

CLIBOT_UNAME = getmecli.username
CLIBOT_USERID = getmecli.id

# VcBot Account Client Details
getmevc = vcbot.get_me()

if getmevc.last_name:
 VCBOT_NAME = getmevc.first_name + " " + getmevc.last_name
else:
 VCBOT_NAME = getmevc.first_name

VCBOT_NAME = getmevc.username
VCBOT_USERID = getmevc.id

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
