from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from ketboards.default import location_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}\n'
             f'Отправь свою геолокацию, чтобы я показал тебе погоду:',
        reply_markup=location_keyboard
    )
