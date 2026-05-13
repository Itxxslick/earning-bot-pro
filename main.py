import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8745253166:AAHQ_yDbPkSOKbXdn2mf424kAaVZfZzeE3s")

users = {}

def get_user(user_id):
    if user_id not in users:
        users[user_id] = {"coins": 0}
    return users[user_id]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Bot is running!\nUse /daily and /balance")

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user = get_user(user_id)

    user["coins"] += 10
    await update.message.reply_text(f"🎁 +10 coins\n💰 Total: {user['coins']}")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user = get_user(user_id)

    await update.message.reply_text(f"💰 Balance: {user['coins']} coins")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user = get_user(user_id)
    user["coins"] += 1

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("daily", daily))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
