from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from .handlers.start_stop import router_start_stop
from .handlers.basic import router_basic
from settings import use_redis, middleware_scheduler

routers = [
    router_start_stop,
    router_basic,
]

dp: Dispatcher = Dispatcher()
dp.include_routers(*routers)

# if use_redis:
#   storage = RedisStorage.from_url('redis://localhost:6379/0')
#   dp.message.middleware.register(ThrottlingMiddleware(storage=storage))

# Регистрируем миддлвари
# dp.message.outer_middleware(CounterMiddleware())
dp.update.middleware.register(middleware_scheduler)