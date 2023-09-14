import telebot
from telebot import types
import requests
from background import keep_alive

token = "6264270259:AAGBz_RiyDBKF97Pdhq1EN1Iq77BNUKXyG4"

data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
bot = telebot.TeleBot(token)
botname = ["@PistsovBot"]


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇪🇺Курс евро💶")
    btn2 = types.KeyboardButton("🇺🇸Курс доллара💵")
    btn3 = types.KeyboardButton("❤️")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.from_user.id, "Привет! Я умею выводить курс евро и доллара! Жми кнопку. "
                                           "На другие сообщения я отвечать не стану", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def send_message(message):
    print(message.chat.id, message.from_user.username, message.text)
    if message.text == "🇪🇺Курс евро💶":
        bot.send_message(chat_id=message.chat.id,
                         text="1 евро = " + str(data["Valute"]["EUR"]["Value"]) + " рублей по курсу ЦБ РФ на сегодня")
    elif message.text == "🇺🇸Курс доллара💵":
        bot.send_message(chat_id=message.chat.id,
                         text="1 доллар = " + str(data["Valute"]["USD"]["Value"]) + " рублей по курсу ЦБ РФ на сегодня")
    elif message.text == "❤️":
        bot.send_message(chat_id=message.chat.id,
                         text="@" + message.from_user.username + ", ты просто прелесть!😘💋")
    elif "@pistsovbot" in message.text.lower():
        bot.send_message(chat_id=message.chat.id,
                         text="@" + message.from_user.username + ", я тебе русским по белому сказал - только кнопки! "
                                                           "На китайском ещё сказать что ле? Я пока так не умею...")


keep_alive()
bot.polling(none_stop=True)