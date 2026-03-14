import asyncio 
from aiogram import Bot , Dispatcher ,types   
from aiogram.filters import Command 
Token = ''
bot = Bot(token = Token) #token olish
db = Dispatcher() #dispechirdan obyekt olsih
@db.message(Command("start")) # userdan kelgan buyruqni filtirlash
async def Start_hadler(message : types.Message):
    await message.answer("Botga kirishdan maqsadingiz nima ?") #bu userga malumot chiqarish

@db.message(Command("help")) # userdan kelgan buyruqni filtirlash
async def Start_had(message : types.Message):
    await message.answer("Botimizning qayeriga tushunmayabsiz ?") #bu userga malumot chiqarish

@db.message(Command("call")) # userdan kelgan buyruqni filtirlash
async def Start_had(message : types.Message):
    await message.answer("biz bilan bog'lanish +998 ** *** ** **") #bu userga malumot chiqarish


async def main():
    await db.start_polling(bot) # botni ishga tushuruvchi Funksiya
asyncio.run(main())

