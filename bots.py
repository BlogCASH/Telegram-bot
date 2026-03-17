import asyncio 
from aiogram import Bot , Dispatcher ,types   
from aiogram.filters import Command 
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


TOKEN = ''

bot = Bot(token = TOKEN) #token olish

db = Dispatcher() #dispechirdan obyekt olish

kb = ReplyKeyboardMarkup(
    keyboard = [[KeyboardButton(text="Kurslar")]],

    resize_keyboard=True
)



@db.message(Command("start")) # userdan kelgan buyruqni filtirlash
async def Start_hadler(message : types.Message):
    await message.answer("Qaysi kurslarimizda o'qimoqchisiz",  reply_markup=kb) #bu userga malumot chiqarish

@db.message(Command("help")) # userdan kelgan buyruqni filtirlash
async def Start_had(message : types.Message):
    await message.answer("Nima savol qiynayabti ?") #bu userga malumot chiqarish

@db.message(Command("call")) # userdan kelgan buyruqni filtirlash
async def Start_had(message : types.Message):
    await message.answer("Biz bilan bog'lanish +998 ** *** ** **") #bu userga malumot chiqarish

@db.message()
async def msg(message: types.Message):
    if message.text == "Salom":
        await message.answer("Bizning kurslarimiz . IT , Ingilis tili va boshqalar")
    
async def main():
    await db.start_polling(bot) # botni ishga tushuruvchi Funksiya
asyncio.run(main())
































