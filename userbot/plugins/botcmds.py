from telethon import events
from telethon import Button
from datetime import datetime
from userbot import catub
from ..Config import Config

botusername = Config.TG_BOT_USERNAME
users = list(Config.SUDO_USERS)
users.append(Config.OWNER_ID)

@catub.bot_cmd(
    pattern=f"^/ping({botusername})?([\s]+)?$",
    from_users=Config.OWNER_ID,
)
async def ping(event):
    start = datetime.now()
    b=Button.inline('Stats', data='stats')
    catevent = await tgbot.send_message(event.chat_id, "𝗣𝗼𝗻𝗴", buttons=b, reply_to=event.id)
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await catevent.edit(f"𝗣𝗼𝗻𝗴\n`{ms}` 𝗆𝗌")


@catub.bot_cmd(
    pattern=f"^/menu({botusername})?([\s]+)?$",
    from_users=users,
)
async def helpmenu(event):
    b=Button.inline('Click', data='mainmenu')
    m = await tgbot.send_message(event.chat_id, "**Open Help Menu**", buttons=b, reply_to=event.id)
