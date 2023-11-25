import telebot
from telebot import types
from background import keep_alive
import get_rates_async

token = '6264270259:AAGBz_RiyDBKF97Pdhq1EN1Iq77BNUKXyG4'

bot = telebot.TeleBot(token)

eur, usd = get_rates_async.main()
eur_text = '1 евро = ' + str(eur) + ' рублей по курсу ЦБ РФ на сегодня'
usd_text = '1 доллар = ' + str(usd) + ' рублей по курсу ЦБ РФ на сегодня'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇪🇺Курс евро💶')
    btn2 = types.KeyboardButton('🇺🇸Курс доллара💵')
    btn3 = types.KeyboardButton('❤️')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.from_user.id, 'Привет! Я умею выводить курс евро и доллара! Жми кнопку. '
                                           'На другие сообщения я отвечать не стану', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_message(message):
    print(message.from_user.username, message.text)
    match message.text:
        case '🇪🇺Курс евро💶':
            bot.send_message(chat_id=message.chat.id, text=eur_text)
        case '🇺🇸Курс доллара💵':
            bot.send_message(chat_id=message.chat.id, text=usd_text)
        case '❤️':
            bot.send_message(chat_id=message.chat.id,
                             text='@' + message.from_user.username + ', ты просто прелесть!😘💋')
        case s if s.startswith('@PistsovBot'):
            bot.send_message(chat_id=message.chat.id,
                             text='@' + message.from_user.username + ', я тебе русским по белому сказал - только кнопки! '
                                                                     'На китайском ещё сказать что ле? Я пока так не умею...')


keep_alive()
bot.polling(none_stop=True)
