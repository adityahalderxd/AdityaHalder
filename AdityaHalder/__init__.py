from AdityaHalder.modules.core.dbs import dbb
from AdityaHalder.modules.core.dirs import dirs
from AdityaHalder.modules.core.github import git
from AdityaHalder.modules.core.sudo import sudo
from AdityaHalder.modules.core.clients import *
from AdityaHalder.modules.core.info import *

from .logging import LOGGER


# Helpers

HELPABLE = {}
MOD_LOAD = []
MOD_NOLOAD = []


# Checker

dirs()
git()
dbb()
sudo()


# Clients

app = app
ass = ass
bot = bot

# Clients Information

app_fnm = app_fnm
app_unm = app_unm
app_uid = app_uid

ass_fnm = ass_fnm
ass_unm = ass_unm
ass_uid = ass_uid

bot_fnm = bot_fnm
bot_unm = bot_unm
bot_uid = bot_uid
