from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_btn():
    markup = InlineKeyboardMarkup()
    uz_en = InlineKeyboardButton("O'zbekcha πΊπΏ β‘οΈ π¬π§ Inglizcha", callback_data='uz_en')
    uz_ru = InlineKeyboardButton("O'zbekcha πΊπΏ β‘οΈ π·πΊ Ruscha", callback_data='uz_ru')
    en_uz = InlineKeyboardButton("Inglizcha π¬π§ β‘οΈ πΊπΏ O'zbekcha", callback_data='en_uz')
    en_ru = InlineKeyboardButton("Inglizcha π¬π§ β‘οΈ π·πΊ Ruscha", callback_data='en_ru')
    ru_uz = InlineKeyboardButton("Ruscha π·πΊ β‘οΈ πΊπΏ O'zbekcha", callback_data='ru_uz')
    ru_en = InlineKeyboardButton("Ruscha π·πΊ β‘οΈ π¬π§ Inglizcha", callback_data='ru_en')
    markup.add(uz_en, uz_ru, en_uz, en_ru, ru_en, ru_uz, row_width=2)
    return markup

