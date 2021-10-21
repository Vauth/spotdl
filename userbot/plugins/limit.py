#By @FeelDeD
from telethon import functions
from . import catub

plugin_category = "useless"

@catub.cat_cmd(
    pattern="limit",
    command=("limit", plugin_category),
    info={
        "header": "Check your account limitation",
        "usage": [
            "{tr}limit",
        ],
    },
)
async def wave(odi):
    "Account Check"
    await odi.edit("`Processing ...`")
    chat = "@SpamBot"
    async with odi.client.conversation(chat) as conv:
        try:
            await odi.client(functions.contacts.UnblockRequest(conv.chat_id))
            start = await conv.send_message('/start')
            end = await conv.get_response()
            result = await odi.edit(end.text)
            msgs = []
            for _ in range(start.id, end.id+2): msgs.append(_)
            await odi.client.delete_messages(conv.chat_id, msgs)
            await odi.client.send_read_acknowledge(conv.chat_id)
        except result:
        	await odi.edit("`Something went Wrong`")