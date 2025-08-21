import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "Какая погода в Москве?")
async def aitext(message: Message):
    response = requests.get("https://wttr.in/Moscow?format=3")
    weather = response.text.strip()
    await message.answer(weather)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я скажу тебе про погоду в Москве")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
