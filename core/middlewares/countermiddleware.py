from aiogram import BaseMiddleware, Router
from aiogram.types import Message
from typing import Dict, Any, Callable, Awaitable


# Создание обработчика счетчика сообщений
class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        print(self.counter)
        return await handler(event, data)
