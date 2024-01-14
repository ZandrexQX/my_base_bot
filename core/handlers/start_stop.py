from aiogram import Bot, Router
from dotenv import load_dotenv
import os

router_start_stop = Router()
load_dotenv()

admin_id = os.getenv('ID_ADMIN')


@router_start_stop.startup()
async def start_bot(bot: Bot):
    me = await bot.get_me()
    await bot.send_message(admin_id, text=f"Bot {me.first_name} started!")


@router_start_stop.shutdown()
async def stop_bot(bot: Bot):
    me = await bot.get_me()
    await bot.send_message(admin_id, text=f"Bot {me.first_name} stopped!")
