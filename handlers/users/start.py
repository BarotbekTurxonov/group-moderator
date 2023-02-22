from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from keyboards.inline.inline import guruh
from filters.shaxsiy import Shaxsiy
from loader import dp,bot


@dp.message_handler(Shaxsiy(), CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await message.answer('Mrit Moderator botga xush kelibsiz!\nCoding Support - @mrit_support')
    # await bot.send_message(chat_id=user_id, text=f"👋🏻 Assalomu alaykum {message.from_user.full_name}!\n\n@MistrUz sizning guruhlaringizni <b>oson</b> va <b>xavfsiz boshqarish</b> uchun eng <b>takomillashgan</b> botdir!\n\n👉🏻 <b>Botni guruhingizga qo'shing</b> va ishga tushishi uchun <b>Admin</b> huquqini bering!\n\n❓ <b>QANDAY BUYRUQLAR BOR?\n\nBarcha buyruqlarni</b> ko'rish va ular qanday ishlashini bilish uchun /help buyrug'ini yuboring!\n "
    #                                              f"<a href='{'https://t.me/IT_Subject'}'>📃 Official Page</a>\n",disable_web_page_preview=True,reply_markup=guruh)