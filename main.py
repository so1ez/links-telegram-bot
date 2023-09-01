import telebot
from telebot import types

from settings import SETTINGS


if __name__ == "__main__":
    
    bot = telebot.TeleBot(SETTINGS.TOKEN)

    @bot.message_handler(commands=["start"])
    def start(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Поехали!")
        markup.add(btn)
        bot.send_message(message.from_user.id, SETTINGS.HELLO_MSG, reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def menu1(message):
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Telegram")
        btn2 = types.KeyboardButton("VKontakte")
        btn3 = types.KeyboardButton("Github")
        btn4 = types.KeyboardButton("In*tagram")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)

        if message.text == "Telegram":
            bot.send_message(message.from_user.id, SETTINGS.TELEGRAM_LINK, reply_markup=markup)                     
        elif message.text == "VKontakte":
            bot.send_message(message.from_user.id, SETTINGS.VK_LINK, reply_markup=markup)
        elif message.text == "Github":
            bot.send_message(message.from_user.id, SETTINGS.GITHUB_LINK, reply_markup=markup)
        elif message.text == "In*tagram":
            bot.send_message(message.from_user.id, SETTINGS.IN_TAGRAM_LINK, reply_markup=markup)

        bot.send_message(message.from_user.id, "Какую ссылку Вам предоставить?", reply_markup=markup)


    bot.polling(none_stop=True, interval=0)