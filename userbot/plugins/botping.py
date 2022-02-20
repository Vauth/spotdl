from datetime import datetime
from userbot import catub
from ..Config import Config

botusername = Config.TG_BOT_USERNAME

@catub.bot_cmd(
    pattern=f"^/ping({botusername})?([\s]+)?$",
    from_users=Config.OWNER_ID,
)
async def ping(event):
    start = datetime.now()
    catevent = await event.reply("𝗣𝗼𝗻𝗴")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await catevent.edit(f"𝗣𝗼𝗻𝗴\n`{ms}` 𝗆𝗌")
	
