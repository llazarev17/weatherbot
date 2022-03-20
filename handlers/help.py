from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())  # декоратор на фход принимает фильтра /help
async def bot_help(message: types.Message):  # фу-ия bot_help будет вызвана, как только пользователь введет /help
    await message.answer('Этот бот поможет узнать погоду')  # текст сообщения, которое получит пользователь
