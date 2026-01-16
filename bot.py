from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = "8407069489:AAF2brwSXTR9hq4H2ktIRfp0DQbwQd2a9YU"

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("🤖 Bot online e funcionando!")

app.add_handler(CommandHandler("start", start))

print("Bot iniciado...")
app.run_polling()
