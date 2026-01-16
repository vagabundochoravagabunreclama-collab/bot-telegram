from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("🤖 Bot online e funcionando!")

app.add_handler(CommandHandler("start", start))

print("Bot iniciado...")
app.run_polling()
