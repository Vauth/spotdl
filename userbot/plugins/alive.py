#made by @feelded

import random
import re
import time
from platform import python_version
import asyncio
from datetime import datetime
from . import hmention
from telethon import version
from telethon.events import CallbackQuery
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, mention

#━━━━━━━━━━━━━━━#
plugin_category = "utils"
start = datetime.now()
@catub.cat_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or " ⁭⁫⌘ "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "✮ 𝕿𝖍𝖊 𝕭𝖔𝖙 𝕴𝖘 𝕽𝖚𝖓𝖓𝖎𝖓𝖌 𝕾𝖚𝖈𝖈𝖊𝖘𝖘𝖋𝖚𝖑𝖑𝖞 ✮"
    CAT_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph//file/80118c88a1d4eaaf332bc.jpg"
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        end = datetime.now()
        ms = (end - start).microseconds / 1000 
        cat_caption = f"**{ALIVE_TEXT}**\n\n"
        cat_caption += f"┏━━━━━━━━━━━━━━━━━━━┓\n"
        cat_caption += f"┃**{EMOJI} Database :** `{check_sgnirts}`\n"
        cat_caption += f"┃**{EMOJI} Telethon Version :** `{version.__version__}\n`"
        cat_caption += f"┃**{EMOJI} Userbot Version :** `{catversion}`\n"
        cat_caption += f"┃**{EMOJI} Python Version :** `{python_version()}\n`"
        cat_caption += f"┃**{EMOJI} Uptime :** `{uptime}\n`"
        cat_caption += f"┃**{EMOJI} Ping :** `{ms}` ms\n"
        cat_caption += f"┃**{EMOJI} Master :** {mention}\n"
        cat_caption += f"┗━━━━━━━━━━━━━━━━━━━┛\n"
        await event.client.send_file(
            event.chat_id,
            PIC,
            caption=cat_caption,
            reply_to=reply_to_id,
            allow_cache=True,
        )
        await event.delete()
    else:
        await edit_or_reply(
            event,
            f"**{ALIVE_TEXT}**\n\n"
            f"┏━━━━━━━━━━━━━━━━━━━┓\n"
            f"┃**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"┃**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"┃**{EMOJI} Userbot Version :** `{catversion}`\n"
            f"┃**{EMOJI} Python Version :** `{python_version()}\n`"
            f"┃**{EMOJI} Uptime :** `{uptime}\n`"
            f"┃**{EMOJI} Master :** {mention}\n"
            f"┗━━━━━━━━━━━━━━━━━━━┛\n",
        )
        
@catub.cat_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    cat_caption = f"**Catuserbot is Up and Running**\n"
    cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, cat_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

#made by @feelded