from aiogram import Bot
import asyncio

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os
import logging
from core.manage_dp import dp
from core.utils.commands import set_commands
from core.middlewares.countermiddleware import CounterMiddleware
from core.utils.db import db_connect
from core.utils.loggers import get_logger
from settings import bot, async_scheduler

logger = get_logger(__name__)

async def start():
    await db_connect()
    await set_commands(bot=bot)
    try:
        # async_scheduler.start()
        logger.info('Бот запущен')
        await dp.start_polling(bot, skip_updates=True)
    except Exception as ex_name:
        logger.error(ex_name)
    finally:
        # async_scheduler.shutdown(wait=True)
        logger.info('Бот остановлен')
        await bot.session.close()

if __name__ == '__main__':
  try:
    asyncio.run(start())
  except Exception as ex:
    print(ex)