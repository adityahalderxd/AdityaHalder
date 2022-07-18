import os
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")


# MANDATORY VARS
API_ID = int(getenv("API_ID", "1020199"))
API_HASH = getenv("API_HASH", "3672885f650c19ef18d53548bb641d5f")
BOT_TOKEN = getenv("BOT_TOKEN", "")
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
OWNER_ID = list(map(int, getenv("OWNER_ID", "5336023580").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))



# EXTRA VARS
ALIVE_IMAGE = getenv("ALIVE_IMAGE", "https://telegra.ph/file/cf866c27a0a74af0b2667.jpg")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
SESSION_STRING = getenv("SESSION_STRING", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5356564375").split()))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/adityaserver")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/adityadiscus")

# GITHUB VARS FOR FUTURE UPDATES
GIT_REPO = getenv("GIT_REPO", "https://github.com/AdityaHalderXD/AdityaHalder")
GIT_BRANCH = getenv("GIT_BRANCH", "AdityaHalder")
GIT_TOKEN = getenv("GIT_TOKEN", None)



# INTERNAL VARIBALES // DON'T TRY TO CHANGE
LOG_FILE_NAME = "aditya.txt"



