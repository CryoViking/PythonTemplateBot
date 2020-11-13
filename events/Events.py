# Author: CryosisOS
# Date Created: 2020-11-07
# GitHub: CryosisOS

# Imports
import discord

# Project Imports
from objects import Bot
from utils.Logger import log, LOG_FILE


def register(bot: Bot):
    @bot.DISCORD_API.event
    async def on_ready():
        print(f"Bot is running, all further console output being logged to: {LOG_FILE}")
        log(1, "Bot is online and running")

    @bot.DISCORD_API.event
    async def on_voice_state_update(member, before, after):
        channel = bot.DISCORD_API.get_channel(bot.CONFIGURATION.log_channel)
        await channel.send(f"User joined a voice channel")
