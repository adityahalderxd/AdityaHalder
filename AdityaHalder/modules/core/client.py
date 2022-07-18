import sys
from pyrogram import Client
from AdityaHalder import config
from ...logging import LOGGER

assistants = []
assistantids = []


class botxd(Client):
    def __init__(self):
        tcbot = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING_SESSION),
            no_updates=True,
        )
        vcbot = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.SESSION_STRING),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting User ID Clients")
        if config.STRING_SESSION:
            await tcbot.start()
            try:
                await tcbot.join_chat("AdityaServer")
                await tcbot.join_chat("AdityaDiscus")
            except:
                pass
            assistants.append(1)
            try:
                await tcbot.send_message(
                    config.LOG_GROUP_ID, "UserBot Client Started"
                )
            except:
                LOGGER(__name__).error(
                    f"UserBot Account has failed to access the log Group. Make sure that you have added your UserBot Account to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await tcbot.get_me()
            tcbot.username = get_me.username
            tcbot.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                tcbot.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                tcbot.name = get_me.first_name
            LOGGER(__name__).info(
                f"UserBot Client Started as {tcbot.name}"
            )
        if config.SESSION_STRING:
            await vcbot.start()
            try:
                await vcbot.join_chat("AdityaServer")
                await vcbot.join_chat("AdityaDiscus")
            except:
                pass
            assistants.append(2)
            try:
                await vcbot.send_message(
                    config.LOG_GROUP_ID, "VcBot Client Started"
                )
            except:
                LOGGER(__name__).error(
                    f"VcBot Account has failed to access the log Group. Make sure that you have added your VcBot Account to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await vcbot.get_me()
            vcbot.username = get_me.username
            vcbot.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                vcbot.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                vcbot.name = get_me.first_name
            LOGGER(__name__).info(
                f"VcBot Client Started as {vcbot.name}"
            )
