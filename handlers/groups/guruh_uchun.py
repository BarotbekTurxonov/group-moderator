from aiogram import types
from aiogram.types import ContentTypes
from keyboards.inline.inline import guruh
from filters.guruh import InMyGroups
from loader import dp, bot
from aiogram.dispatcher.filters import Command
from filters.admins import AdminFilter
from filters.guruh import InMyGroups
import datetime
import asyncio
import re
import aiogram

# FOR HANDLERS
@dp.message_handler(chat_id=(-1001842369674, -1001831195516), commands='start')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await message.delete()

@dp.message_handler(chat_id=(-1001842369674,-1001831195516) ,content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    nick = message.new_chat_members[0].full_name
    chat_id =  message.chat.id
    mes_id = message.message_id
    await bot.delete_message(chat_id=chat_id,message_id=mes_id)

@dp.message_handler(chat_id=(-1001842369674,-1001831195516),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    nick = message.left_chat_member.full_name
    chat_id =  message.chat.id
    mes_id = message.message_id
    await bot.delete_message(chat_id=chat_id,message_id=mes_id)



# FOR ADMINS
@dp.message_handler(InMyGroups(), AdminFilter(), Command("ro", prefixes="!"))
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    """
    !ro 
    !ro 5 
    !ro 5 test
    !ro test
    !ro test test test
    /ro 
    /ro 5 
    /ro 5 test
    /ro test
    """
    # 5-minutga izohsiz cheklash
    # !ro 5
    # command='!ro' time='5' comment=[]

    # 50 minutga izoh bilan cheklash
    # !ro 50 reklama uchun ban
    # command='!ro' time='50' comment=['reklama', 'uchun', 'ban']

    time = int(time)

    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik! {err.args}")
        return

    # Пишем в чат
    delete = await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
                         f"Sabab:  <b>{comment}</b>")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    # 5 sekun kutib xabarlarni o'chirib tashlaymiz
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()
    # await delete.delete()

# read-only holatdan qayta tiklaymiz
@dp.message_handler(InMyGroups(), AdminFilter(),Command("unro", prefixes="!"))
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=False,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    
    await asyncio.sleep(5)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.answer(f"Foydalanuvchi <a href='https://t.me/{member.username}'>{member.full_name}</a> tiklandi!", disable_web_page_preview=True)

    # xabarlarni o'chiramiz
    # await message.delete()
    await service_message.delete()