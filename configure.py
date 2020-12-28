#!/usr/bin/env python3
########################################################################################################################
# Performs a first time config of the bot.
########################################################################################################################

import json

# For nicer prompt message.
INFO = {
    "token": "bot token",
    "prefix": "bot prefix",
    "bot_name": "bot name",
    "description": "bot description",
    "log_channel": "bot log channel ID"
}
# Config file path.
CONFIG_PATH = "./res/settings.json"

def prompt_option(option = "token"):
    """Prompts user for option input.

    Args:
        option: The valid options from `INFO`.

    Returns:
        The input string from user.

    Raises:
        ValueError: If `option` is invalid.
    """
    if option not in INFO:
        raise ValueError(f"bad option: {option}")
    return input(f"Enter {INFO[option]}: ")

def user_input():
    """Get user input on all options.

    Returns:
        A dict containing the option and user input.
    """
    ret = {}
    for (opt, _) in INFO.items():
        ret[opt] = prompt_option(opt)


if __name__ == "__main__":
    options = {}
    for (opt, _) in INFO.items():
        options[opt] = prompt_option(opt)

    js = json.dumps(options, indent = 2)
    with open(CONFIG_PATH, "w") as f:
        f.write(js)
    print(f"\nWrite file complete:\n{js}")
