from aiogram import types
from loader import dp


@dp.message_handler()  # декоратор обработчик сообщений
async def bot_echo(message: types.Message):  # фу-ия которая будет вызвана если ни один фильтр не подошел
    await message.answer(message.text)  # текст сообщения, которое отправил пользователь
