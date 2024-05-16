import asyncio
import config as config
from aiogram import Bot, Dispatcher
import logging

from handlers import common, msg, carreer_choise

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_router(common.router)
    dp.include_router(carreer_choise.router)
    dp.include_router(msg.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())