import telebot

API_TOKEN = "8082904025:AAGFsnZ8zNNJ_Q_TYIdRiPOvVKdDz07kKJY"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Бота запущено!")
    bot.infinity_polling()


