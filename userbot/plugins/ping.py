import asyncio
from datetime import datetime

from ..core.managers import edit_or_reply
from . import catub, hmention

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
        catevent = await edit_or_reply(event, "__**✮ Pong!**__")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await catevent.edit(f"**🏓 Average Ping ! **\n┏━━━━━━━┓\n┃ ⁭⁫⌘ {ms}\n┗━━━━━━━┛")
    else:
        catevent = await edit_or_reply(event, "<b><i>✮ Pong!</b></i>", "html")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(
            f"┏━━━━━━━┓\n┃ ⁭⁫⌘ {ms} \n┗━━━━━━━┛",
            parse_mode="html",
        )
        