from aiogram import Bot
import asyncio
from dotenv import load_dotenv
import os
import logging
from core.manage_dp import dp
from core.utils.commands import set_commands
from core.utils.db_postgress import db_connect
from core.utils.db.commands_db import insert_query

logging.basicConfig(level=logging.WARNING,
                    # filename='bot_log.log',
                    format="[%(asctime)s] - [%(levelname)s] - "
                               "%(funcName)s:%(lineno)d - %(message)s",
                    datefmt='%d-%m-%y %H:%M:%S')
load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = Bot(token=token, parse_mode='HTML')

async def start():
    # await db_connect()
    await set_commands(bot=bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())