from apps.models import Message
from telethon import TelegramClient


async def handle_unread_messages(user_bot: TelegramClient) -> list[Message]:
    unread_messages = []
    # FIXME: rebase to env chat id
    me = await user_bot.get_me()
    async for dialog in user_bot.iter_dialogs():
        if dialog.unread_count > 0:
            last_unread_message = await user_bot.get_messages(dialog.id, limit=1)
            unread_messages.append(
                Message(
                    user_id=me.id,
                    dialog=dialog.name,
                    text=last_unread_message[0].text,
                    datetime=last_unread_message[0].date
                )
            )
    return unread_messages
