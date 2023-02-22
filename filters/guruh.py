from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class InMyGroups(BoundFilter):
    MY_GROUPS = [-1001421149312]

    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        ) and message.chat.id in self.MY_GROUPS
