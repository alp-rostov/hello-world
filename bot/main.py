from config import *
import telebot
from extensions import *
from telebot import types

bot = telebot.TeleBot ( TOKEN )
#кнопки валюты в конвекторе
conv_markup = types.ReplyKeyboardMarkup()
buttons=[]
for val in exch.keys():
    buttons.append(types.KeyboardButton (val.capitalize()))
conv_markup.add(*buttons)

#кнопки количества валюты в конвекторе
kol_markup = types.ReplyKeyboardMarkup()
buttons_kol=[]
for val_ in [300,500,1000,5000,10000]:
    buttons_kol.append(types.KeyboardButton (val_))
kol_markup.add(*buttons_kol)

@bot.message_handler(commands=['start', 'help'])
def start_message(message: telebot.types.Message):
    bot.send_message(message.chat.id,f"Приветствуем в боте обмена валют.\n\n "
                                     f"/values просмотр списка доступных валют \n"
                                     f"/convert перехода в конвертор валют")

@bot.message_handler(commands=['values'])
def start_message(message: telebot.types.Message):
    text = 'Доступные валюты:\n'+'\n'.join ( i for i  in exch.keys() )
    bot.reply_to(message, text)

@bot.message_handler(commands=['convert'])
def get_base(message: telebot.types.Message):
    bot.send_message ( message.chat.id, f"Приветствуем!\n"
                                        f"Введите валюту для конвертации",
                                         reply_markup=conv_markup)
    bot.register_next_step_handler(message, get_quote)

def get_quote(message: telebot.types.Message):
    base=message.text.strip()
    bot.send_message ( message.chat.id, f"Введите валюту в которую нужно конвертировать" )
    bot.register_next_step_handler(message, get_amount, base)

def get_amount(message: telebot.types.Message, base):
    quote=message.text.strip()
    bot.send_message ( message.chat.id, f"Введите количество валюты {base} которую необходимо конвертировать в валюту {quote}", reply_markup=kol_markup )
    bot.register_next_step_handler(message, get_price, base, quote)

def get_price(message: telebot.types.Message, base, quote):
    amount=message.text.strip()
    try:
        summa_exch = converter.get_price( base, quote, amount )
        bot.send_message(message.chat.id, summa_exch, reply_markup=types.ReplyKeyboardRemove() )
    except ApiExp as e:
        err_message ( message.chat.id, e )


@bot.message_handler(content_types='text')
def start_message(message: telebot.types.Message):
    try:
        base, quote, amount = message.text.split ( )
    except ValueError:
        err_message ( message.chat.id, 'Неверное количество параметров' )
    else:
        try:
            summa_exch = converter.get_price( base, quote, amount )
            bot.send_message(message.chat.id, summa_exch )
        except ApiExp as e:
            err_message(message.chat.id, e)


def err_message(id, e):
    bot.send_message ( id, f'Ошибка ввода данных! {e} \n\n '
                           f'Выберете команду для продолжения:\n '
                           f'/start - начальная страница \n'
                           f'/values - список валют для конвертиции \n'
                           f'/convert - конвертер валют \n')


bot.polling(none_stop=True)