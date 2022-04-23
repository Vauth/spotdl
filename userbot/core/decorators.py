import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from ..Config import Config
from ..sql_helper.globals import gvarstatus


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        auser = list(Config.SUDO_USERS)
        auser.append(Config.OWNER_ID)
        if (c_q.query.user_id and c_q.query.user_id in auser):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            HELP_TEXT = (
                gvarstatus("HELP_TEXT")
                or "What could have been."
            )
            await c_q.answer(
                HELP_TEXT,
                alert=True,
            )

    return wrapper
