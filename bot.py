from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from aiogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo

dp = Dispatcher()
bot = Bot('token')

webapp = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text='Подтвердить',
    web_app=WebAppInfo(url="https://bdosha.github.io/web_app_tg_test/"))]])


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать в тест долбанного WebApp", reply_markup=webapp)
    return


@dp.message()
async def message(message: Message):
    await message.answer('Неизвестная команда')


if __name__ == '__main__':
    dp.run_polling(bot)
