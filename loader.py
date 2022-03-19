from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp import ClientSession

from config import token

storage = MemoryStorage()
session = ClientSession()
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
