# Coded By R.I.P
# Telegram : t.me/RIP_PROJECTS/
import os
from pyrogram import Client

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # https://t.me/BotFather
APP_ID = int(os.environ.get("API_ID" , 12345678)) # Get From https://my.telegram.org
API_HASH = os.environ.get("API_HASH" , "") # Get From https://my.telegram.org

plugins = dict(
    root="plugins",
)

app = Client(
    'Fake Information',
    bot_token= BOT_TOKEN,
    api_id = APP_ID,
    api_hash= API_HASH,
    plugins=plugins
)


app.run()