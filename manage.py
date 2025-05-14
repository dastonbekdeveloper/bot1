from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7708092203:AAFVlPOWCAFoj4MzCPr6MSJC0bDXjSX6oQU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Men oddiy botman. Menga xabar yuboring, mpien aynan shuni qaytaraman.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"Siz shuni yubordingiz: {user_text}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Run bot
    app.run_polling()

if __name__ == "__main__":
    main()