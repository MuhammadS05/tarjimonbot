from telebot.types import CallbackQuery, Message
import translators.server as tts

from loader import bot
from inline import get_btn


@bot.callback_query_handler(func=lambda call: call)
def reaction_to_calls(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
    from_lang, to_lang = call.data.split('_')
    if from_lang == 'uz':
        text = f"Tarjima uchun so'z yoki matn kiriting:"
    elif from_lang == 'ru':
        text = f"Введите слово или текст для перевода:"
    else:
        text = 'Write the word or text to translate:'

    msg = bot.send_message(chat_id, text)
    bot.register_next_step_handler(msg, action, from_lang, to_lang)

def action(message: Message, from_lang, to_lang):
    chat_id = message.chat.id
    word = message.text
    translated_word = tts.google(word, from_lang, to_lang)
    bot.send_message(chat_id, f"{translated_word}\n\nTarjima yo'lini tanlang👇:", reply_markup=get_btn())


