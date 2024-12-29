# meta developer: @angellmodules

from telethon.tl.functions.channels import JoinChannelRequest
from .. import loader

@loader.tds
class AutoJoinModule(loader.Module):
    """Модуль для автоматической подписки на канал"""

    strings = {"name": "AutoJoin"}

    async def client_ready(self, client, db):
        """Подписывается на канал при старте клиента"""
        await client(JoinChannelRequest("angellmodules"))
