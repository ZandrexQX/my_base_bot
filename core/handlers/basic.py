from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from .msg_text import basic_text
from ..utils.db import User
from ..utils.db.commands_db import select_user_id, add_query
from settings import ADMIN_ID

router_basic = Router()


@router_basic.message(Command('start'))
async def get_start(message: Message, bot: Bot):
    user = await select_user_id(user_id=message.from_user.id)
    if not user:
        await bot.send_message(ADMIN_ID, text=f"New user: {message.from_user.first_name}")
        username = message.from_user.first_name
        await add_query(model=User,
                        user_id=message.from_user.id,
                        username=username)
    user = await select_user_id(user_id=message.from_user.id)
    await bot.send_message(message.from_user.id,
                           basic_text(user.username))


# @router_basic.message()
# async def get_help():
#     pass


@router_basic.message()
async def get_some_command(message: Message):
    text = message.text
    if text.lower() in ['привет', 'здравствуйте', 'добрый день', 'hi', 'hello']:
        await message.answer("Приветствую")
    elif text.lower() in ['пока', 'прощай', 'by']:
        await message.answer('Прощайте')
    else:
        await message.answer(text=f'Я не могу пока ответить на "{text}"')
