import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

from core.utils.loggers import get_logger
from core.utils.schedulers.todo_schedular import AsyncScheduler

logger = get_logger(__name__)
use_redis = True
DEBUG_MODE = False

load_dotenv()
token = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ID_ADMIN')
bot = Bot(token=token, default=DefaultBotProperties(parse_mode='MARKDOWN'))

async_scheduler = AsyncScheduler()
logger.info('Планировщик запущен')
middleware_scheduler = async_scheduler.get_middleware_scheduler()

for job in async_scheduler.get_jobs():
    print(job.id, job.next_run_time)
