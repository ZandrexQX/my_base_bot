from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message
from ..utils.db.commands_db import select_id
from ..keyboards.reg_kb import get_reg_kb

router_basic = Router()


@router_basic.message(Command('start'))
async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, text="Бот начал работать")
    user = await select_id(user_id=message.from_user.id)
    if user:
        await bot.send_message(message.from_user.id, f"Добро пожаловать {user.username}\n"
                                                     f"Дата регистрации: {user.reg_date}")
    else:
        await bot.send_message(message.from_user.id, f"Добро пожаловать {message.from_user.username}\n"
                                                     f"Вы не зарегистрированы.", reply_markup=get_reg_kb())


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
