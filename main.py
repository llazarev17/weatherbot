import telebot
import config

bot = telebot.TeleBot(config.token)
print(bot.get_me())


@bot.message_handler(content_types=["text"])
def handle_text(massege):
    bot.send_message(massege.chat.id, "Hi")


if __name__ == '__main__':
    bot.polling()
