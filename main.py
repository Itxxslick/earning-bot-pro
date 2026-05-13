from telegram.ext import Application, CommandHandler

TOKEN = "8745253166:AAHQ_yDbPkSOKbXdn2mf424kAaVZfZzeE3s"

app = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Hello")

app.add_handler(CommandHandler("start", start))

app.run_polling()
