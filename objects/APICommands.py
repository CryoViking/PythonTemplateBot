from discord.ext import commands
from utils.Logger import log


class BaseCommand:
    def __init__(self, tag: str, bot_api: commands.Bot):
        self.tag = tag
        self.DISCORD_API = bot_api

    @staticmethod
    def requires_args():
        return False


class ShutdownCommand(BaseCommand):
    def __init__(self, bot_api: commands.Bot):
        super().__init__(tag="shutdown", bot_api=bot_api)

    def do_option(self, args: str):
        log(1, "Bot is being shutdown via API")
        await self.DISCORD_API.logout()
        log(1, "Bot has been shutdown via API")

    def requires_args(self):
        return False


def initialise_api_commands(discord_api):
    shutdown = ShutdownCommand(discord_api)
    return {
        shutdown.tag: shutdown
    }
