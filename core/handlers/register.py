# from aiogram import Bot, Router, F
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
#
# from my_base.core.states.reg_state import RegisterState
# from my_base.core.utils.db.commands_db import select_user_id, add_query
#
# router_reg = Router()
#
#
# @router_reg.message(F.text == 'Зарегистрироваться')
# async def start_register(message: Message, state: FSMContext, bot: Bot):
#     user = await select_user_id(user_id=message.from_user.id)
#     if user:
#         await bot.send_message(message.from_user.id, f'{user.username} уже зарегистрирован')
#     else:
#         await bot.send_message(message.from_user.id, f'Как к вам обращаться? 🖊')
#         await state.set_state(RegisterState.regName)
#
#
# @router_reg.message(RegisterState.regName)
# async def reg_name(message: Message, state: FSMContext, bot: Bot):
#     await bot.send_message(message.from_user.id, f'Приятно познакомиться {message.text}\n'
#                                                  f'Теперь введите ваш возраст - 🖊')
#
#     await state.update_data(regname=message.text)
#     await state.set_state(RegisterState.regAge)
#
#
# @router_reg.message(RegisterState.regAge)
# async def reg_age(message: Message, state: FSMContext, bot: Bot):
#     if message.text.isdigit():
#         if 0 <= int(message.text) <= 100:
#             await state.update_data(regage=int(message.text))
#             reg_data = await state.get_data()
#             name = reg_data.get('regname')
#             age = reg_data.get('regage')
#             msg = f'Приятно познакомиться {name}'
#             await bot.send_message(message.from_user.id, msg)
#             await add_query(user_id=message.from_user.id, username=name, age=age)
#             await state.clear()
#         else:
#             await bot.send_message(message.from_user.id, f'Возраст указан неверно.\n'
#                                                          f'Введите корректный возраст:')
#     else:
#         await bot.send_message(message.from_user.id, f'Вы ввели "{message.text}". Введите возраст:')