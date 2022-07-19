from AdityaHalder.modules.core.client import *

app_get_me = app.get_me()
ass_get_me = ass.get_me()
bot_get_me = bot.get_me()


if app_get_me.last_name:
    app_fnm = app_get_me.first_name + " " + app_get_me.last_name
else:
    app_fnm = app_get_me.first_name

app_unm = app_get_me.username
app_uid = app_get_me.id


if ass_get_me.last_name:
    ass_fnm = ass_get_me.first_name + " " + ass_get_me.last_name
else:
    ass_fnm = ass_get_me.first_name

ass_unm = ass_get_me.username
ass_uid = ass_get_me.id


if bot_get_me.last_name:
    bot_fnm = bot_get_me.first_name + " " + bot_get_me.last_name
else:
    bot_fnm = bot_get_me.first_name

bot_unm = bot_get_me.username
bot_uid = bot_get_me.id
