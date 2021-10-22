#By @FeelDeD
from datetime import datetime
from userbot import catub
from ..Config import Config

@catub.bot_cmd(
    pattern="^/ping$",
    from_users=Config.OWNER_ID,
)
async def ping(event):
    start = datetime.now()
    catevent = await event.reply("__✮ Pong!__")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await catevent.edit(f"**Pong!**\n`{ms}` ms")
	
