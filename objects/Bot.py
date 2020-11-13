# Author: CryosisOS
# Date Created: 2020-11-07
# GitHub: CryosisOS

# Imports
from discord.ext import commands


class BotConfiguration:
    def __init__(self, json):
        self.prefix = json["prefix"]
        self.token = json["token"]
        self.bot_name = json["bot_name"]
        self.description = json["description"]
        self.log_channel = json["log_channel"]


class Bot:
    def __init__(self, bot: commands.Bot, configuration: BotConfiguration):
        self.DISCORD_API: commands.Bot = bot
        self.CONFIGURATION: BotConfiguration = configuration
        self.name = configuration.bot_name
        self.description = configuration.description
