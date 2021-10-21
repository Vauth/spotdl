import re
from telethon import Button
from telethon.events import CallbackQuery, InlineQuery
from userbot import catub
from ..core.decorators import check_owner

CALC = {}

plugin_category = "utils"

m = [
    "AC",
    "C",
    "⌫",
    "%",
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "x",
    "00",
    "0",
    ".",
    "÷",
]
tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
lst.append([Button.inline("=", data="calc=")])


@catub.cat_cmd(
    pattern="icalc(?:\s|$)([\s\S]*)",
    command=("icalc", plugin_category),
    info={
        "header": "Inline Calculator",
        "usage": "{tr}icalc",
        "description": "Awesome inline calculator with buttons.",
    },
)
async def icalc(e):
    if e.client._bot:
        return await e.reply("𝗗𝗮𝘇𝗮𝗶 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿", buttons=lst)
    results = await e.client.inline_query(Config.TG_BOT_USERNAME, "calc")
    await results[0].click(e.chat_id, silent=True, hide_via=True)
    await e.delete()


@catub.tgbot.on(InlineQuery)
async def inlinecalc(event):
    query_user_id = event.query.user_id
    query = event.text
    string = query.lower()
    if (
        query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS
    ) and string == "calc":
        event.builder
        calc = event.builder.article(
            "Calc", text="𝗗𝗮𝘇𝗮𝗶 𝗜𝗻𝗹𝗶𝗻𝗲 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿", buttons=lst
        )
        await event.answer([calc])


@catub.tgbot.on(CallbackQuery(data=re.compile(b"calc(.*)")))
@check_owner
async def _(e):  # sourcery no-metrics
    x = (e.data_match.group(1)).decode()
    user = e.query.user_id
    get = None
    if x == "AC":
        if CALC.get(user):
            CALC.pop(user)
        await e.edit(
            "𝗗𝗮𝘇𝗮𝗶 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿",
            buttons=[Button.inline("Open Again", data="recalc")],
        )
    elif x == "C":
        if CALC.get(user):
            CALC.pop(user)
        await e.answer("Cleared")
    elif x == "⌫":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get[:-1]})
            await e.answer(str(get[:-1]))
    elif x == "%":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "/100"})
            await e.answer(str(get + "/100"))
    elif x == "÷":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "/"})
            await e.answer(str(get + "/"))
    elif x == "x":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "*"})
            await e.answer(str(get + "*"))
    elif x == "=":
        if CALC.get(user):
            get = CALC[user]
        if get:
            if get.endswith(("*", ".", "/", "-", "+")):
                get = get[:-1]
            out = eval(get)
            try:
                num = float(out)
                await e.answer(f"Answer: {num}", cache_time=0, alert=True)
            except BaseException:
                CALC.pop(user)
                await e.answer("Error", cache_time=0, alert=True)
        await e.answer("None")
    else:
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + x})
            return await e.answer(str(get + x))
        CALC.update({user: x})
        await e.answer(str(x))


@catub.tgbot.on(CallbackQuery(data=re.compile(b"recalc")))
@check_owner
async def _(e):
    m = [
        "AC",
        "C",
        "⌫",
        "%",
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "-",
        "1",
        "2",
        "3",
        "x",
        "00",
        "0",
        ".",
        "÷",
    ]
    tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
    lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
    lst.append([Button.inline("=", data="calc=")])
    await e.edit("𝗗𝗮𝘇𝗮𝗶 𝗜𝗻𝗹𝗶𝗻𝗲 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿", buttons=lst)
