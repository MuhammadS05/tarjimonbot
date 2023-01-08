from telebot.types import Message


from loader import bot
from inline import get_btn
from config import ADMIN_ID


user_list = []

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    if message.text == '/start':
        text = f"Assalomu alaykum, {message.from_user.first_name}!\n\nTarjima yo'lini tanlang👇:"
        markup = get_btn()

        id = message.from_user.id
        if id in user_list:
            pass
        else:
            user_list.append(id)
        print(user_list)
        count = 0
        for i in user_list:
            count += 1
        bot.send_message(ADMIN_ID, count)

    else:
        text = "Yordam yoki murojaatlar uchun @manage_get ga yozishingiz mumkin"
        markup = None
    bot.send_message(chat_id,
                     text, reply_markup=markup)




