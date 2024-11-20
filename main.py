from aiogram import Bot
import asyncio

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os
import logging
from core.manage_dp import dp
from core.utils.commands import set_commands
from core.middlewares.countermiddleware import CounterMiddleware
from my_base.core.utils.db import db_connect

logging.basicConfig(level=logging.INFO,
                    # filename='bot_log.log',
                    format="[%(asctime)s] - [%(levelname)s] - "
                               "%(funcName)s:%(lineno)d - %(message)s",
                    datefmt='%d-%m-%y %H:%M:%S')
load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = Bot(token=token, default=DefaultBotProperties(parse_mode='MARKDOWN'))
# Регистрируем миддлвари
dp.message.outer_middleware(CounterMiddleware())

async def start():
    # await db_connect()
    logging.info('Бот запущен')
    await set_commands(bot=bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
  try:
    asyncio.run(start())
  except Exception as ex:
    print(ex)