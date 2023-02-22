from aiogram import types
from filters.kanal import Kanal
from loader import dp


# Echo bot
@dp.message_handler(Kanal(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
