import unittest
from unittest.mock import AsyncMock

import bot

class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        message = AsyncMock()
        await bot.hello(message)
        message.answer.assrt_called_with(text="Привет, я Бот-повар\nЯ создан для того, чтобы помочь тебе найти простые рецепты, кроме доширака",
                         reply_markup=bot.keyboard)

class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        message = AsyncMock()
        await bot.show_recept(message)
        message.answer.assrt_called_with(text="У нас представлены некоторые рецепты. \n"
                         "Выберете, что у вас есть в холодильнике", reply_markup=bot.rec)

if __name__ == '__main__':
    unittest.main()
