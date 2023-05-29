from aiogram.types import Message

from keyboards.default.menu import menu
from keyboards.default.viloyatlar import vil
from keyboards.inline.ulashish import *
from loader import dp
from handlers.users.obhavo import *
from handlers.users.uchkunga import *

@dp.message_handler(text="📅 Bugungi ob-havo")
async def tosh(messge : Message):
    await messge.answer("Qaysi viloyatning ob-havo ma'lumotini olishni istaysiz?",reply_markup=vil)

@dp.message_handler(text="Toshkent")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('tashkent')} \n<b>{Viloyat('tashkent')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('tashkent')}...{min('tashkent')} , {obhavo('tashkent')}\n\n"
                             f"<b>Tong</b> : {tong('tashkent')} \n"
                             f"<b>Kun</b> : {kunh('tashkent')}\n"
                             f"<b>Oqshom</b> : {oqshom('tashkent')}\n"
                             f"_________________________________________\n"
                             f" {Oy('tashkent')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('tashkent')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True,reply=menu)


@dp.message_handler(text="Andijon")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('andijan')} \n<b>{Viloyat('andijan')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('andijan')}...{min('andijan')} , {obhavo('andijan')}\n\n"
                             f"<b>Tong</b> : {tong('andijan')} \n"
                             f"<b>Kun</b> : {kunh('andijan')}\n"
                             f"<b>Oqshom</b> : {oqshom('andijan')}\n"
                             f"_________________________________________\n"
                             f" {Oy('andijan')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('andijan')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Farg'ona")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('ferghana')} \n<b>{Viloyat('ferghana')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('ferghana')}...{min('ferghana')} , {obhavo('ferghana')}\n\n"
                             f"<b>Tong</b> : {tong('ferghana')} \n"
                             f"<b>Kun</b> : {kunh('ferghana')}\n"
                             f"<b>Oqshom</b> : {oqshom('ferghana')}\n"
                             f"_________________________________________\n"
                             f" {Oy('ferghana')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('ferghana')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Samarqand")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('samarkand')} \n<b>{Viloyat('samarkand')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('samarkand')}...{min('samarkand')} , {obhavo('samarkand')}\n\n"
                             f"<b>Tong</b> : {tong('samarkand')} \n"
                             f"<b>Kun</b> : {kunh('samarkand')}\n"
                             f"<b>Oqshom</b> : {oqshom('samarkand')}\n"
                             f"_________________________________________\n"
                             f" {Oy('samarkand')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('samarkand')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Buxoro")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('bukhara')} \n<b>{Viloyat('bukhara')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('bukhara')}...{min('bukhara')} , {obhavo('bukhara')}\n\n"
                             f"<b>Tong</b> : {tong('bukhara')} \n"
                             f"<b>Kun</b> : {kunh('bukhara')}\n"
                             f"<b>Oqshom</b> : {oqshom('bukhara')}\n"
                             f"_________________________________________\n"
                             f" {Oy('bukhara')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('bukhara')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Guliston")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('gulistan')} \n<b>{Viloyat('gulistan')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('gulistan')}...{min('gulistan')} , {obhavo('gulistan')}\n\n"
                             f"<b>Tong</b> : {tong('gulistan')} \n"
                             f"<b>Kun</b> : {kunh('gulistan')}\n"
                             f"<b>Oqshom</b> : {oqshom('gulistan')}\n"
                             f"_________________________________________\n"
                             f" {Oy('gulistan')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('gulistan')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Jizzax")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('jizzakh')} \n<b>{Viloyat('jizzakh')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('jizzakh')}...{min('jizzakh')} , {obhavo('jizzakh')}\n\n"
                             f"<b>Tong</b> : {tong('jizzakh')} \n"
                             f"<b>Kun</b> : {kunh('jizzakh')}\n"
                             f"<b>Oqshom</b> : {oqshom('jizzakh')}\n"
                             f"_________________________________________\n"
                             f" {Oy('jizzakh')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('jizzakh')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Zarafshon")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('zarafshan')} \n<b>{Viloyat('zarafshan')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('zarafshan')}...{min('jizzakh')} , {obhavo('zarafshan')}\n\n"
                             f"<b>Tong</b> : {tong('zarafshan')} \n"
                             f"<b>Kun</b> : {kunh('zarafshan')}\n"
                             f"<b>Oqshom</b> : {oqshom('zarafshan')}\n"
                             f"_________________________________________\n"
                             f" {Oy('zarafshan')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('zarafshan')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Qarshi")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('karshi')} \n<b>{Viloyat('karshi')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('karshi')}...{min('karshi')} , {obhavo('karshi')}\n\n"
                             f"<b>Tong</b> : {tong('karshi')} \n"
                             f"<b>Kun</b> : {kunh('karshi')}\n"
                             f"<b>Oqshom</b> : {oqshom('karshi')}\n"
                             f"_________________________________________\n"
                             f" {Oy('karshi')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('karshi')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Navoiy")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('navoi')} \n<b>{Viloyat('navoi')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('navoi')}...{min('navoi')} , {obhavo('navoi')}\n\n"
                             f"<b>Tong</b> : {tong('navoi')} \n"
                             f"<b>Kun</b> : {kunh('navoi')}\n"
                             f"<b>Oqshom</b> : {oqshom('navoi')}\n"
                             f"_________________________________________\n"
                             f" {Oy('navoi')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('navoi')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Navoiy")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('navoi')} \n<b>{Viloyat('navoi')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('navoi')}...{min('navoi')} , {obhavo('navoi')}\n\n"
                             f"<b>Tong</b> : {tong('navoi')} \n"
                             f"<b>Kun</b> : {kunh('navoi')}\n"
                             f"<b>Oqshom</b> : {oqshom('navoi')}\n"
                             f"_________________________________________\n"
                             f" {Oy('navoi')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('navoi')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Namangan")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('namangan')} \n<b>{Viloyat('namangan')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('namangan')}...{min('namangan')} , {obhavo('namangan')}\n\n"
                             f"<b>Tong</b> : {tong('namangan')} \n"
                             f"<b>Kun</b> : {kunh('namangan')}\n"
                             f"<b>Oqshom</b> : {oqshom('namangan')}\n"
                             f"_________________________________________\n"
                             f" {Oy('namangan')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('namangan')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Nukus")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('nukus')} \n<b>{Viloyat('nukus')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('nukus')}...{min('nukus')} , {obhavo('namangan')}\n\n"
                             f"<b>Tong</b> : {tong('nukus')} \n"
                             f"<b>Kun</b> : {kunh('nukus')}\n"
                             f"<b>Oqshom</b> : {oqshom('nukus')}\n"
                             f"_________________________________________\n"
                             f" {Oy('nukus')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('nukus')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Nukus")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('nukus')} \n<b>{Viloyat('nukus')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('nukus')}...{min('nukus')} , {obhavo('namangan')}\n\n"
                             f"<b>Tong</b> : {tong('nukus')} \n"
                             f"<b>Kun</b> : {kunh('nukus')}\n"
                             f"<b>Oqshom</b> : {oqshom('nukus')}\n"
                             f"_________________________________________\n"
                             f" {Oy('nukus')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('nukus')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Termiz")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('termez')} \n<b>{Viloyat('termez')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('termez')}...{min('termez')} , {obhavo('termez')}\n\n"
                             f"<b>Tong</b> : {tong('termez')} \n"
                             f"<b>Kun</b> : {kunh('termez')}\n"
                             f"<b>Oqshom</b> : {oqshom('termez')}\n"
                             f"_________________________________________\n"
                             f" {Oy('termez')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('termez')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Urganch")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('urgench')} \n<b>{Viloyat('urgench')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('urgench')}...{min('urgench')} , {obhavo('urgench')}\n\n"
                             f"<b>Tong</b> : {tong('urgench')} \n"
                             f"<b>Kun</b> : {kunh('urgench')}\n"
                             f"<b>Oqshom</b> : {oqshom('urgench')}\n"
                             f"_________________________________________\n"
                             f" {Oy('urgench')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('urgench')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

@dp.message_handler(text="Xiva")
async def tosh(messge : Message):
    await messge.answer(text=f"{kun('khiva')} \n<b>{Viloyat('khiva')}</b> hududida kutilayotgan ob-havo.\n\n"
                             f"🌡 {harorat('khiva')}...{min('khiva')} , {obhavo('khiva')}\n\n"
                             f"<b>Tong</b> : {tong('khiva')} \n"
                             f"<b>Kun</b> : {kunh('khiva')}\n"
                             f"<b>Oqshom</b> : {oqshom('khiva')}\n"
                             f"_________________________________________\n"
                             f" {Oy('khiva')}\n"
                             f"_________________________________________\n"
                             f"{Namlik('khiva')}\n"
                             f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/ob_havo_uz_robot'>Ob-Havo</a>\n"
                             f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",reply_markup=menu,disable_web_page_preview=True)

