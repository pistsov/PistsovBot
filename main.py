import telebot
from telebot import types
import requests

token = '6264270259:AAGBz_RiyDBKF97Pdhq1EN1Iq77BNUKXyG4'

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇪🇺Курс евро💶')
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Привет! Я умею выводить курс евро! Жми кнопку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def euro(message):
    print(message.from_user.username, message.text)
    if message.text == '🇪🇺Курс евро💶':
        bot.send_message(chat_id=message.chat.id,
                         text='1 евро = ' + str(data['Valute']['EUR']['Value']) + ' рублей по курсу ЦБ РФ на сегодня')
    else:
        bot.send_message(chat_id=message.chat.id,
                         text='Я умею выводить только курс евро по кнопке, не балуйся, ' + message.from_user.username + '!')


bot.polling(none_stop=True)