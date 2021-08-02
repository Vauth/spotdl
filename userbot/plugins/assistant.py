from userbot import catub
from ..core.managers import edit_or_reply

plugin_category = "bot"

@catub.cat_cmd(
    pattern="assistant$",
    command=("assistant", plugin_category),
    info={
        "header": "To start Assistant Bot",
        "usage": [
            "{tr}assistant",
        ],
    },
)
async def source(e):
    "To start Assistant Bot"
    await edit_or_reply(
        e,
        "My [Assistant](https://t.me/DazaiSunBot?start) Bot",
    )