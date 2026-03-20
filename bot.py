import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = ""
ADMIN_ID =  123456789

bot = Bot(token=TOKEN)
dp = Dispatcher()


users = {}


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Ismingizni yozing:")
    users[message.from_user.id] = {}


@dp.message()
async def get_name(message: types.Message):
    user_id = message.from_user.id

    if user_id in users:
        name = message.text
        users[user_id]["name"] = name

        
        await bot.send_message(
            ADMIN_ID,
            f"Yangi user:\nIsm: {name}\nID: {user_id}"
        )

        await message.answer("Rahmat! Ma'lumot qabul qilindi ")

        del users[user_id]


async def main():
    await dp.start_polling(bot)

asyncio.run(main())