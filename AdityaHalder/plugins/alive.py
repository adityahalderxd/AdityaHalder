# AdityaHalder
import asyncio
from pyrogram import *
from pyrogram.types import *

from AdityaHalder import *
from AdityaHalder.modules.core.sudo import SUDOERS
from AdityaHalder.modules.helpers.basic import edit_or_reply
from AdityaHalder.modules.helpers.filters import command


@Client.on_message(command(["alive"]) & SUDOERS)
async def alive(client: Client, message: Message):
    await edit_or_reply(message, "**🥀 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Gᴇɴɪᴜs Mᴀsᴛᴇʀ ✨ ...**")



__MODULE__ = "Aʟɪᴠᴇ"
__HELP__ = f"""
**🥀 Tᴇsᴛ Yᴏᴜʀ Bᴏᴛ Wᴏʀᴋɪɴɢ Oʀ Nᴏᴛ.**

`.alive` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**
"""
