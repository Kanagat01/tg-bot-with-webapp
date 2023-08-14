from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(types.InlineKeyboardButton(
        "Открыть приложение", web_app=WebAppInfo(url="")))
    await message.answer(f"Привет, это тестовый бот магазина кросовок!", reply_markup=kb)


executor.start_polling(dp)
