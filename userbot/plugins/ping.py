import asyncio
from datetime import datetime

from ..core.managers import edit_or_reply
from . import catub, hmention, mention

plugin_category = "tools"


@catub.cat_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        catevent = await edit_or_reply(event, "𝗣𝗼𝗻𝗴")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await catevent.edit(f"𝗔𝘃𝗲𝗿𝗮𝗴𝗲\n`{ms}` 𝗆𝗌")
    else:
        catevent = await edit_or_reply(event, "𝗣𝗼𝗻𝗴")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(f"𝗣𝗼𝗻𝗴\n`{ms}` 𝗆𝗌",)
       
