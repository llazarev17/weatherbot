from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp import ClientSession

from config import token

storage = MemoryStorage()  # храним данные ) в памяти
session = ClientSession()  # обьект http сессии см. aiohttp документацию
bot = Bot(token)  # обьект бот см документацию aigram
dp = Dispatcher(bot, storage=storage)  # диспатчер (храниит все обработчики сообщений)
