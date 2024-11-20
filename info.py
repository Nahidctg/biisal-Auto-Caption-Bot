# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "7528643689"))
API_ID = int(getenv("API_ID", "28870226"))
API_HASH = str(getenv("API_HASH", "a5b1ff3f75941649bf5bc159782f0f00"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7899900845:AAHEJZdghS15fvXPjWZf5t9chu65LpvtLm0"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://cogana5793:cogana5793@cluster0.1uo0s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/AllBotUpdatemy'>{file_name} Telegram : @AllBotUpdatemy\n\nForward the file before Downloading.</a></b>",
    )
)
