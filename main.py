from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio


API_TOKEN = "8082904025:AAGFsnZ8zNNJ_Q_TYIdRiPOvVKdDz07kKJY"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer("Привіт,напиши що небуть!")

@dp.message()
async def echo_message(message: Message):
    await message.answer(message.text)

async def main():
    print("Бота запущено")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


if __name__ == "__main__":
    print()
    executor.start_polling(dp, skip_updates=True)

