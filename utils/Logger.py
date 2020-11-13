# Author: CryosisOS
# Date Created: 2020-11-07
# GitHub: CryosisOS

# IMPORTS
from datetime import datetime
import os


LOG_FILE = "./logs"

LEVELS = {
    1: "INFO",
    2: "WARN",
    3: "ERROR",
    4: "CRITICAL"
}


def log(severity, message):
    timestamp = datetime.now()
    timestamp_string = timestamp.strftime("%Y-%m-%d|%H:%M:%S")
    with open(LOG_FILE, "a+") as file:
        file.write(f"{timestamp_string}\t{LEVELS[severity]}\t{message}\n")


def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
