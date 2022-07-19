import os
import re
import asyncio
import importlib
import sys

from pyrogram import idle
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pytgcalls.exceptions import NoActiveGroupCall

from AdityaHalder import config
from AdityaHalder.logging import logger
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
    LOGGER("AdityaHalder").info("User Bot Started Successfully")
    LOGGER("AdityaHalder").info("Checking Assistant Client ...")
    if (ass):
        LOGGER("AdityaHalder").info(
            "Assistant Client Found, Starting Assistant Client"
        )
        await ass.start()
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



home_text_pm = f"""**I Aᴍ Gᴇɴɪᴜs, Aɴ Aᴅᴠᴀɴᴄᴇᴅ UsᴇʀBᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.**"""


@bot.on_message(command(["start"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/027283ee9defebc3298b8.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 Hᴇʟʟᴏ, I Aᴍ Gᴇɴɪᴜs » Aɴ Aᴅᴠᴀɴᴄᴇᴅ
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ.

┏━━━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ'xD› : [Aᴅɪᴛʏᴀ Hᴀʟᴅᴇʀ](https://t.me/adityahalder)
┣★ Uᴘᴅᴀᴛᴇs ›› : [Aᴅɪᴛʏᴀ Sᴇʀᴠᴇʀ](https://t.me/adityaserver)
┣★ Sᴜᴘᴘᴏʀᴛ » : [Aᴅɪᴛʏᴀ Dɪsᴄᴜs](https://t.me/adityadiscus)
┗━━━━━━━━━━━━━━━━━━━┛

💞 Cʟɪᴄᴋ Oɴ Dᴇᴘʟᴏʏ Bᴜᴛᴛᴏɴ Tᴏ Mᴀᴋᴇ
Yᴏᴜʀ Oᴡɴ » Gᴇɴɪᴜs Usᴇʀ Bᴏᴛ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Dᴇᴘʟᴏʏ Gᴇɴɪᴜs UsᴇʀBᴏᴛ ✨", url=f"https://github.com/GeniusBoi/Genius-UserBot")
                ]
                
           ]
        ),
    )
    
    
    
@bot.on_message(command(["help"]) & SUDOERS)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await robot.send_message(config.LOG_GROUP_ID, text, reply_markup=keyboard)




async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
Gᴇɴɪᴜs UsᴇʀBᴏᴛ Vᴇʀ : `2.0` 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ Gᴇɴɪᴜs Cᴏᴍᴍᴀɴᴅs ✨...**
""".format(
            first_name=name
        ),
        keyboard,
    )

@bot.on_callback_query(filters.regex("close") & SUDOERS)
async def close(_, CallbackQuery):
    await CallbackQuery.message.delete()

@bot.on_callback_query(filters.regex("aditya") & SUDOERS)
async def aditya(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@bot.on_callback_query(filters.regex(r"help_(.*?)") & SUDOERS)
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
Gᴇɴɪᴜs UsᴇʀBᴏᴛ Vᴇʀ : `2.0` 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ Gᴇɴɪᴜs Cᴏᴍᴍᴀɴᴅs ✨...**
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :** ", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ ʙᴀᴄᴋ", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 ᴄʟᴏsᴇ", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await robot.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)
    

if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AdityaHalder").info("Stopping Aditya Halder! GoodBye")
