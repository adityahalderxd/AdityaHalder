import os
import re
import asyncio
import importlib
import sys

from pyrogram import idle
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pytgcalls.exceptions import NoActiveGroupCall

from .logging import LOGGER
from AdityaHalder import config
from AdityaHalder import HELPABLE, MOD_LOAD, MOD_NOLOAD
from AdityaHalder.plugins import ALL_MODULES
from AdityaHalder.modules.core.sudo import SUDOERS
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.modules.core.clients import app, ass, bot
from AdityaHalder.utilities.inline import paginate_modules

loop = asyncio.get_event_loop()


async def init():
    LOGGER("AdityaHalder").info("Starting Bot Client")
    if (not bot):
        LOGGER("AdityaHalder").error(
            "Bot Client Start Failed!.. Exiting Process."
        )
        return
    else:
    await bot.start()
    LOGGER("AdityaHalder").info("Bot Client Successfully Started")
    LOGGER("AdityaHalder").info("Starting User Bot Client")
    if (not config.STRING_SESSION):
        LOGGER("AdityaHalder").error(
            "String Session Not Found!.. Exiting Process."
        )
        return
    if (not app):
        LOGGER("AdityaHalder").error(
            "User Bot Client Not Found!.. Exiting Process."
        )
        return
    await app.start()
    await app.join_chat("AdityaServer")
    await app.join_chat("AdityaDiscus")
    LOGGER("AdityaHalder").info("User Bot Started Successfully")
    LOGGER("AdityaHalder").info("Checking Assistant Client ...")
    if (ass):
        LOGGER("AdityaHalder").info(
            "Assistant Client Found, Starting Assistant Client"
        )
        await ass.start()
        await ass.join_chat("AdityaServer")
        await ass.join_chat("AdityaDiscus")
        LOGGER("AdityaHalder").info("Assistant Client Started")
    else:
     LOGGER("AdityaHalder").info(
            "Assistant Client Not Found!.."
        )
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module("AdityaHalder.plugins." + all_module)
        if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
    LOGGER("AdityaHalder.plugins").info(f">> Successfully imported: {all_module}.py")
    LOGGER("AdityaHalder.plugins").info("All Modules Imported")
    
    
    LOGGER("AdityaHalder").info("Aditya Halder Started Successfully")
    await idle()
    

if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AdityaHalder").info("Stopping Aditya Halder! GoodBye")
