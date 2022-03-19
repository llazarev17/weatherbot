from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from ketboards.default import main_keyboard
from utils.weather import get_weather, conditions
from states import UserProfile


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=UserProfile.location)
async def get_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    weather = await get_weather(lat, lon)

    description = conditions[weather['fact']['condition']]
    temperature = round(weather['fact']['temp'])
    location = f"{weather['geo_object']['country']['name']}, {weather['geo_object']['province']['name']} - {weather['geo_object']['district']['name']}"

    await state.finish()
    await message.answer(
        text=f'Темпиратура: {round(temperature)} \n'
             f'Описание: {description} \n'
             f'Локация: {location}',
        reply_markup=main_keyboard
    )
