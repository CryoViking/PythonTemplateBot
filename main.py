# Author: CryosisOS
# Date Created: 2020-11-07
# GitHub: CryosisOS

# Imports
import json
from discord.ext import commands

# Project Imports
from objects.Bot import Bot, BotConfiguration
from utils.Logger import log
import commands.Commands as Commands
import events.Events as Events


# Loads a JSON file into a raw object. No validation performed.
def load_config(filename):
    with open(filename) as file:
        data = file.read()
    return json.loads(data)


# The main method of the program
def __main__():
    configuration = BotConfiguration(load_config(filename="./res/settings.json"))  # Hardcoded for now is fine.
    bot_api = commands.Bot(command_prefix=configuration.prefix, description=configuration.description)
    bot = Bot(bot=bot_api, configuration=configuration)
    Commands.register(bot)
    Events.register(bot)
    bot.DISCORD_API.run(bot.CONFIGURATION.token)


if __name__ == '__main__':
    __main__()
