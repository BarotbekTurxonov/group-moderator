from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

guruh = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="➕Botni guruhga qo'shish➕",url="https://t.me/ReaLJoin_Robot?startgroup=start")],
        [
            InlineKeyboardButton(text="👨🏻‍💻 Admin",url="t.me/MrGayratov"),
            InlineKeyboardButton(text="Kanal 📢",url="t.me/IT_Subject")
        ],
        [InlineKeyboardButton(text="♻️Botni ulashish♻️",switch_inline_query="\nSizning guruhlaringizni oson va xavfsiz boshqarish uchun eng yaxshi takomillashgan qorovul botdir!\n\nBotni Guruhingizga qoshish uchun pastdagi ssilkani bosing 👇🏻👇🏻👇🏻\n\nhttps://t.me/ReaLJoin_Robot?startgroup=start")]
    ]
)