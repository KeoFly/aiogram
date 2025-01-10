import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

from app.handlers import router
from app.admin import admin

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(admin, router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')