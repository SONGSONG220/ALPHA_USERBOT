import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "37096542"))
API_HASH = getenv("API_HASH", "e87f06819f9d2b3364502b978650568f")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7812646657").split()))
OWNER_ID = int(getenv("OWNER_ID", "7812646657"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://aditya0:aditya0@cluster0.9m8897t.mongodb.net/?appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "8759127283:AAGLmu1BVJcp2Rjqa6G5oFuvCjl9swZRdi0")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://files.catbox.moe/om20d5.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "🤖 I am Alive!")
PM_LOGGER = getenv("PM_LOGGER", "-1003812233808")
LOG_GROUP = getenv("LOG_GROUP", "-1003812233808")
GIT_TOKEN = getenv("GIT_TOKEN", None)
REPO_URL = getenv("REPO_URL", "https://github.com/SONGSONG220/ALPHA_USERBOT")
BRANCH = getenv("BRANCH", "main")

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
