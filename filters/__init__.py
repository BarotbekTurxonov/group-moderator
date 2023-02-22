from aiogram import Dispatcher
from .guruh import InMyGroups
from .kanal import Kanal
from .shaxsiy import Shaxsiy

from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(InMyGroups)
    dp.filters_factory.bind(Kanal)
    dp.filters_factory.bind(Shaxsiy)
