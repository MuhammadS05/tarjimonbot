from telebot import TeleBot
from telebot.types import BotCommand


from config import TOKEN

bot = TeleBot(TOKEN)

bot.set_my_commands(commands=[
    BotCommand('start', 'Botni qayta ishga tushirish'),
    BotCommand('help', "Botda nosozliklar bo'lsa yordam")
])


bot.get_my_commands()