from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from handlers.users.obhavo import *

ulashisht = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ulashish",switch_inline_query=f"\n{kun('tashkent')} \n{Viloyat('tashkent')} hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('tashkent')} +{tong('tashkent')} , {obhavo('tashkent')}\n\n"
                                 f"Tong : {tong('tashkent')} \n"
                                 f"Kun : {kunh('tashkent')}\n"
                                 f"Oqshom : {oqshom('tashkent')}\n_________________________________________\n"
                             f" {Oy('tashkent')}\n_________________________________________\n"
                             f"{Namlik('tashkent')}\n"
                             f"Doimiy ob-havo ma'lumotlarin @Ob_Havo_uz_robot")
        ]
    ]
)
ulashisha = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ulashish",switch_inline_query=f"\n{kun('andijan')} \n{Viloyat('andijan')} hududida kutilayotgan ob-havo.\n\n"
                                 f"🌡 {harorat('andijan')} +{tong('andijan')} , {obhavo('andijan')}\n\n"
                                 f"Tong : {tong('andijan')} \n"
                                 f"Kun : {kunh('andijan')}\n"
                                 f"Oqshom : {oqshom('andijan')}\n_________________________________________\n"
                                 f"{Oy('andijan')}\n_________________________________________\n"
                                 f"{Namlik('andijan')}\n"
                                 f"Doimiy ob-havo ma'lumotlari @Ob_Havo_uz_robot")
        ]
    ]
)