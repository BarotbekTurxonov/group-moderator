from aiogram import types
from aiogram.types import ContentTypes
from keyboards.inline.inline import guruh
from loader import dp, bot
import asyncio
gr_id =  -1001421149312# BU yerda Coding Supportni ID raqami turadi!


@dp.message_handler(chat_id=-1001697156886) # Bu yerda Samarqand IT PARK group ID raqami!
async def gr_join(message: types.Message):
    chesk_group = await bot.get_chat_member(chat_id=gr_id,user_id=message.from_user.id)
    if message.from_user.id == 1087968824:
        pass
    elif message.from_user.id != 1087968824:
        if chesk_group['status'] != 'left':
            pass
        else:
            await message.delete()
            await message.answer(text=f"@{message.from_user.username} | #ID{message.from_user.id}\n<b>Guruhda yozish uchun <a href='https://t.me/mrit_support'>↗️Coding Support↗️</a> ga obuna bo'ling!</b>",disable_web_page_preview=True,reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="↗️Coding Support↗️", url=f'https://t.me/mrit_support')))
            await asyncio.sleep(30)
            await message.delete()