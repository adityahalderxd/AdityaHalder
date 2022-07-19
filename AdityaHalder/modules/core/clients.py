import os
import sys
from AdityaHalder.config import *
from pyrogram import Client
from ...logging import LOGGER


if STRING_SESSION:
    app = Client(
        session_name=STRING_SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="AdityaHalder.plugins")
)
else:
    app = None

if SESSION_STRING:
    ass = Client(
        session_name=SESSION_STRING,
        api_id=API_ID,
        api_hash=API_HASH,
)
else:
    ass = None

if BOT_TOKEN:
    bot = Client(
        "AdityaHalder",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
)
else:
    bot = None
