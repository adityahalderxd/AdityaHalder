import sys
from pyrogram import Client
from AdityaHalder import config
from ...logging import LOGGER


assistants = []
assistantids = []


app = Client(
    config.STRING_SESSION,
    config.API_ID,
    config.API_HASH,
    plugins=dict(root="plugins"),
    no_updates=True,
)

ass = Client(
    config.SESSION_STRING,
    config.API_ID,
    config.API_HASH,
    no_updates=True,
)

bot = Client(
    "AdityaHalder",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
)


class botxd(Client):
    def __init__(self):
        self.one = app
        self.two = ass

    async def start(self):
        LOGGER(__name__).info(f"Starting User ID Clients")
        if config.STRING_SESSION:
            await self.one.start()
            try:
                await self.one.join_chat("AdityaServer")
                await self.one.join_chat("AdityaDiscus")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "UserBot Client Started"
                )
            except:
                LOGGER(__name__).error(
                    f"UserBot Account has failed to access the log Group. Make sure that you have added your UserBot Account to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"UserBot Client Started as {self.one.name}"
            )
        if config.SESSION_STRING:
            await self.two.start()
            try:
                await self.two.join_chat("AdityaServer")
                await self.two.join_chat("AdityaDiscus")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "VcBot Client Started"
                )
            except:
                LOGGER(__name__).error(
                    f"VcBot Account has failed to access the log Group. Make sure that you have added your VcBot Account to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(
                f"VcBot Client Started as {self.two.name}"
            )
