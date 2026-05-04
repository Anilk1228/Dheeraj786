import os, asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Variable Imports
from vars import API_ID, API_HASH, BOT_TOKEN, OWNER, TOTAL_USERS
import globals

# 🔥 Flask app (ONLY for gunicorn, no thread)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Dheeraj Giri Uploader is Online!"

# 🔥 Bot setup
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- UI BUTTONS ---
main_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🎙️ Commands", callback_data="all_commands"),
        InlineKeyboardButton("⚙️ Settings", callback_data="setttings")
    ],
    [
        InlineKeyboardButton("💳 Premium", callback_data="upgrade_command"),
        InlineKeyboardButton("📊 Status", callback_data="info_command")
    ],
    [
        InlineKeyboardButton("👤 Contact Owner", url=f"tg://openmessage?user_id={OWNER}")
    ]
])

# --- START COMMAND ---
@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    caption = (
        f"👑 **Welcome, {m.from_user.first_name}!**\n\n"
        f"You are now using the official uploader bot of\n"
        f"✨ `𝐃𝐡𝐞𝐞𝐫𝐚𝐣 𝐆𝐢𝐫𝐢`.\n\n"
        f"➠ Submit your TXT file to begin extraction.\n"
        f"➠ High-speed, secure, and 24/7 processing.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"**Official Brand:** `@DheerajGiri_Bots` 🦁"
    )

    logo_wallpaper = "https://i.ibb.co/XQZ1r1n/1000479523.jpg"

    await bot.send_photo(
        chat_id=m.chat.id,
        photo=logo_wallpaper,
        caption=caption,
        reply_markup=main_buttons
    )

# --- REGISTER HANDLERS ---
from text_handler import register_text_handlers
from youtube_handler import register_youtube_handlers
from commands import register_commands_handlers

register_text_handlers(bot)
register_youtube_handlers(bot)
register_commands_handlers(bot)

# 🔥 MAIN ASYNC START
async def main():
    await bot.start()
    print("🚀 Bot Started Successfully")
    await idle()

# 🔥 ENTRY POINT
if __name__ == "__main__":
    asyncio.run(main())
