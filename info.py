import os

SESSION = "teraboxdl"
API_ID = int(os.getenv("API_ID", "22141398"))
API_HASH = os.getenv("API_HASH", "0c8f8bd171e05e42d6f6e5a6f4305389")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7277194738:AAHapce3wJ-kSG3WDYG5oxg9wYxaenYwZ-8")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002284232975"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002284232975"))
PORT = int(os.getenv("PORT", "8080"))
FORCE_CHANNEL = int(os.getenv("FORCE_CHANNEL", "-1002379643238"))
ADMINS = [5660839376, 6167872503, 5961011848]
DAILY_LIMITS = 20
MAINTENANCE_MODE = False  # Change to False to disable maintenance mode

MAINTENANCE_MESSAGE = (
    "⚠️ **Maintenance Mode Activated** ⚙️\n\n"
    "Our bot is currently undergoing scheduled maintenance to improve performance and add new features.\n\n"
    "Please check back in a while. We’ll be back soon, better than ever!\n\n"
    "💬 **Support Group:** [SUPPORT](https://t.me/AnSBotsSupports)\n\n"
    "**– Team Support**"
)
