from telethon import TelegramClient
from settings import BotSettings


def get_bot(bot_settings: BotSettings) -> TelegramClient:
    return TelegramClient(
        'userbot', 
        api_id=bot_settings.API_ID, 
        api_hash=bot_settings.API_HASH,
        device_model='Model',
        system_version='4.16.30-vxCUSTOM',
        app_version='1.2.0',
    )
