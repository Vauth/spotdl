import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, mention

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
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "-"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "𝘚𝘦𝘦𝘮𝘴 𝘢𝘱𝘱𝘢𝘳𝘦𝘯𝘵𝘭𝘺 𝘐'𝘮 𝘢𝘭𝘪𝘷𝘦"
    CAT_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/c2e40a1217606fa1c07f0.jpg"
    cat_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = cat_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        PIC = random.choice(CAT)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(event, caption)


temp = "{ALIVE_TEXT}\n\n\
{EMOJI} 𝘜𝘴𝘦𝘳𝘣𝘰𝘵 𝘷𝘦𝘳𝘴𝘪𝘰𝘯: `{catver}`\n\
{EMOJI} 𝘛𝘦𝘭𝘦𝘵𝘩𝘰𝘯 𝘷𝘦𝘳𝘴𝘪𝘰𝘯: `{telever}`\n\
{EMOJI} 𝘗𝘺𝘵𝘩𝘰𝘯 𝘷𝘦𝘳𝘴𝘪𝘰𝘯: `{pyver}`\n\
{EMOJI} 𝘜𝘱𝘵𝘪𝘮𝘦: `{uptime}`\n\
{EMOJI} 𝘗𝘪𝘯𝘨: `{ping}`\n\
{EMOJI} 𝘔𝘢𝘴𝘵𝘦𝘳: {mention}\n"


@catub.cat_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}ialive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "-"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**Userbot is Up and Running**"
    cat_caption = f"{ALIVE_TEXT}\n"
    cat_caption += f"**{EMOJI} Telethon version:** `{version.__version__}`\n"
    cat_caption += f"**{EMOJI} Userbot version:** `{catversion}`\n"
    cat_caption += f"**{EMOJI} Python version:** `{python_version()}`\n"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, cat_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
