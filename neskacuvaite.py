# meta developer: @angellmodules

from telethon.tl.functions.channels import JoinChannelRequest
from .. import loader

@loader.tds
class AutoJoinModule(loader.Module)
    strings = {"name": "AutoJoin"}

    async def client_ready(self, client, db):
        await client(JoinChannelRequest("angellmodules"))
