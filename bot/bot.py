from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
import asyncio
from aiogram.filters import Command

token = '8074417550:AAEleMarcs1g-fok315PXafRlYKqpShboUI'
dp = Dispatcher()
bot = Bot(token=token)

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Бот работает! Ожидаю сообщений...')
    

async def main():
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())