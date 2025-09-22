from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your bot token from BotFather
TOKEN = "8386947911:AAGZyFwIPJY2j861WaChiNv4NtoJXMlc6P4"

# Replace with the group ID you got earlier
GROUP_ID = -1001825127022   # example supergroup ID

# When user writes to bot in private chat
async def forward_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":   # only handle private chats
        text = update.message.text
        if text:
            await context.bot.send_message(chat_id=GROUP_ID, text=text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_group))

    app.run_polling()

if __name__ == "__main__":
    main()
