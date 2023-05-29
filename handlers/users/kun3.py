from aiogram.types import Message
from .uchkunga import *
from loader import dp


@dp.message_handler(text="🗓 3 kunga ma'lumot")
async def uch(message : Message):
    await message.answer(f"{bugun('tashkent')} {bugun2('tashkent')}\n"
                         f"🌡{ Max('tashkent')}..{Min('tashkent')}, {bulut('tashkent')}\n"
                         f"Yog'ingarchilik ehtimoli: {yongin('tashkent')}\n\n"
                         f"{bugu2('tashkent')} {bugun22('tashkent')}\n"
                         f"🌡 {Max2('tashkent')}..{Min2('tashkent')}, {bulut2('tashkent')}")