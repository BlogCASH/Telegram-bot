import logging 
import asyncio
import wikipedia
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types , F
from aiogram.filters import CommandStart

load_dotenv()

wikipedia.set_lang("uz")
API_TOKEN = ''
bot = bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Salom!    Men Wikipedia botiman. Siz menga biror mavzu haqida so'rashing  mumkin. Masalan, 'Python dasturlash tili' yoki 'O'zbekiston tarixi'")
@dp.message(F.text)
async def send_wikipedia_summary(message: types.Message):
    query = message.text
    try:
        summary = wikipedia.summary(query, sentences=3)
        await message.answer(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"Bu mavzu bir nechta ma'nolarga ega. Iltimos, quyidagi variantlardan birini tanlang:\n{e.options}")
    except wikipedia.exceptions.PageError:
        await message.answer("Kechirasiz, bu mavzu topilmadi. Iltimos, boshqa mavzu haqida so'rang.")
async def main():
    await dp.start_polling(bot)    
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))