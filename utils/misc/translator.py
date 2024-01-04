from aiogram import types
from googletrans import Translator


async def translator(message: types.Message):
    google_trans = Translator()
    lang = google_trans.detect(message.text).lang
    if len(message.text.split()) >= 1:
        if lang == 'uz':
            await message.reply(google_trans.translate(message.text, dest='en').text)
        elif lang == 'en':
            await message.reply(google_trans.translate(message.text, dest='uz').text)
        else:
            await message.reply(f"Bu Bot bu tildagi gapni tarjima qila olmaydi uzr 🙂")
    else:
        await message.reply("Bunday so'z topilmadi yoki kattaroq gap yozing.\n"
                            "That word did not find or write longer sentence")
