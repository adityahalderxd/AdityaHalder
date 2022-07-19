from AdityaHalder.modules.core.dbs import dbb
from AdityaHalder.modules.core.dirs import dirs
from AdityaHalder.modules.core.github import git
from AdityaHalder.modules.core.sudo import sudo

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
