from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loader import dp
from ketboards.default import main_keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text='Вот список того, что я умею',
        reply_markup=main_keyboard
    )
