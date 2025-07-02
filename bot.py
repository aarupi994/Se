import telebot

# 🔑 Replace this with your actual bot token
TOKEN = "7232868612:AAEE686letBrsPMdJ28S1QJv51MXY2B5lNc"  # Example: "123456789:ABCDEF..."

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# /start command handler
@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.send_message(
        message.chat.id,
        "Seedha maut 😅 jhat jaisa Name hai\n\nAnd TAKING TAKING CHHIII\n\nJOIN OUR CHANNEL: https://t.me/+bIiViZAAPDExNGZl"
    )

# Polling to keep bot running
print("🤖 Bot is running... Press Ctrl+C to stop.")
bot.infinity_polling()
