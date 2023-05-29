from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum, <b>{message.from_user.full_name}</b>!\n\n"
                         f"Ob-havo Ma'lumotlari olishni istasangiz bo'limlardan o'zingizga kerakli sahifani tanlang❗️",
                         reply_markup=menu)


