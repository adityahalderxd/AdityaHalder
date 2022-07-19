import requests
from datetime import datetime
from pyrogram import filters, Client
from AdityaHalder.modules.core.sudo import SUDOERS
# ping checker

@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & SUDOERS)
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("**Checking ...**")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"**🤖 Aditya's Ping\n»** `{mp} ms`")


__MODULE__ = "Pɪɴɢ"
__HELP__ = f"""
**🥀 Cʜᴇᴄᴋ Yᴏᴜʀ Gᴇɴɪᴜs UsᴇʀBᴏᴛ Pɪɴɢ.**

`.ping` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**
"""
