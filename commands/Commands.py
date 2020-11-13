# Author: CryosisOS
# Date Created: 2020-11-07
# GitHub: CryosisOS

# Imports
from objects import Bot
from utils.Logger import log, clear_logs as clearlogs


def register(bot: Bot):
    @bot.DISCORD_API.command()
    async def ping(ctx, *args):
        await ctx.send(f"pong <@{ctx.author.id}>")

    @bot.DISCORD_API.command()
    async def shutdown(ctx, *args):
        log(1, "Bot is being shutdown")
        await bot.DISCORD_API.logout()
        log(1, "Bot has been shutdown")

    @bot.DISCORD_API.command()
    async def clear_logs(ctx, *args):
        clearlogs()
        log(1, "Log file has been cleared and reset.")
        channel = bot.DISCORD_API.get_channel(bot.CONFIGURATION.log_channel)
        await channel.send(f"Logs have been cleared")
