from aiogram import Dispatcher
from .handlers.start_stop import router_start_stop
from .handlers.basic import router_basic
from .handlers.register import router_reg


routers = [
    router_start_stop,
    router_reg,
    router_basic,
]

dp: Dispatcher = Dispatcher()
dp.include_routers(*routers)
