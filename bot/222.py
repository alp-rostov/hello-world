import telebot


TOKEN = "5415208660:AAFxUkGHduPsZ2I7WhfVVn_w71yfDmQ-1nM"

bot = telebot.TeleBot ( TOKEN )
@bot.me
def handle_start_help(message):
    pass