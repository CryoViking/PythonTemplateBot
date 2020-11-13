# Python Discord Bot Project Template
#####Author: CryosisOS

### Default commands:
- ping
- shutdown
- clear_logs

### Settings:
Inside ``./res/settings.json`` configure the values appropriate to the configuration needed for the discord bot that  
you are building.
```json
{
  "token": "bot token here",
  "prefix": "prefix here",
  "bot_name": "bot name here",
  "description": "Place your bot description here",
  "log_channel": 000000000000000000 //Put the channel ID that you want log output to go to.
}
```

### Running the Bot:
To run the bot, execute the following command from the root folder of the project.
```shell script
py main.py
```
If you are smart enough to figure out how to run it from another directory. **Note**: the log file location  
is relevant to where the command is ran from. The default location if you don't change it is:
```
./logs
``` 

### Configuring Log Location:
Inside ``utils/Logger.py`` there is a variable that defines a relative location for the log file and its name.  
You can change this to anything that you want to. The variable name is:
```python
LOG_FILE = "./logs"
```

### Adding Commands
Inside ``commands/Commands.py`` there is a register function. To add more commands to the bot add to this function.
Example:
```python
def register(bot: Bot):
    @bot.DISCORD_API.command()
    async def ping(ctx, *args):
        await ctx.send(f"pong <@{ctx.author.id}>")

    @bot.DISCORD_API.command()
    async def shutdown(ctx, *args):
        # ... function code

    @bot.DISCORD_API.command()
    async def clear_logs(ctx, *args):
        # ... function code

    # Below is an example of an added function
    @bot.DISCORD_API.command()
    async def HelloWorld(ctx, *args):
        # ... do something for this command
```
The added command is ``HelloWorld`` to execute the command, restart the bot and in discord enter  
``<prefix>HelloWorld`` and the command will execute.

### Adding Events
Inside ``events/Events.py`` there is a register function. To add more event listeners to the discord bot, add  
to this register function. Available event names are listed on the official Discord.py documentation.
Example:
```python
def register(bot: Bot):
    @bot.DISCORD_API.event
    async def on_ready():
        print(f"Bot is running, all further console output being logged to: {LOG_FILE}")
        log(1, "Bot is online and running")

    @bot.DISCORD_API.event
    async def on_voice_state_update(member, before, after):
        # ... function code
```
The format for adding a new event is the same for adding a new command.