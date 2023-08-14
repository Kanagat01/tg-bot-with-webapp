import logging
from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(
        "Открыть приложение", web_app=WebAppInfo(url="https://kanagat01.github.io/tg-bot-with-webapp/")))
    await message.answer(f"Привет, это тестовый бот магазина кросовок!", reply_markup=kb)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    executor.start_polling(dp)
