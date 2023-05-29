from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Bugungi ob-havo")
        ],
        [
            KeyboardButton(text="🗓 3 kunga ma'lumot")
        ],
        [
            KeyboardButton(text="👨‍👩‍👧‍👦 Biz haqimizda"),
            KeyboardButton(text="📊Statistika")
        ]
    ],resize_keyboard=True
)
menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Bugungi ob-havo")
        ],
        [
            KeyboardButton(text="🗓 3 kunga ma'lumot")
        ]
    ],resize_keyboard=True
)