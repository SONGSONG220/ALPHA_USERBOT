import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "12345678"))
API_HASH = getenv("API_HASH", "abcdef1234567890abcdef1234567890")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "9876543210").split()))
OWNER_ID = int(getenv("OWNER_ID", "9876543210"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://username:password@cluster0.example.mongodb.net/mydb")
BOT_TOKEN = getenv("BOT_TOKEN", "123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/5badd2112e1e0cdf03a1f.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "🤖 I am Alive!")
PM_LOGGER = getenv("PM_LOGGER", "-1001234567890")
LOG_GROUP = getenv("LOG_GROUP", "-1001234567890")
GIT_TOKEN = getenv("GIT_TOKEN", None)
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMPURVI/ALPHA_USERBOT")
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
