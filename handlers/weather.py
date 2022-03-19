from aiogram import types
from loader import dp
from states import UserProfile
from ketboards.default import location_keyboard


@dp.message_handler(text='🌤 Погода сейчас')
async def get_weather(message: types.Message):
    await message.answer(
        f'Отправь свою геолокацию, чтобы я показал тебе погоду:',
        reply_markup=location_keyboard
    )
    await UserProfile.first()

