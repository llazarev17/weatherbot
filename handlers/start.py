from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loader import dp
from ketboards.default import main_keyboard


@dp.message_handler(CommandStart())  # декоратор фильтрует сообщение на '/start'
async def bot_start(message: types.Message):  # фу-ия bot_start будет вызвана, как только пользователь введет /start
    await message.answer(
        text='Вот список того, что я умею',  # текст сообщения, которое получит пользователь
        reply_markup=main_keyboard  # клавиатура, которую полчит пользователь
    )
