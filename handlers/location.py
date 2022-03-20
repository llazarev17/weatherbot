from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from ketboards.default import main_keyboard
from utils.weather import get_weather, conditions
from states import UserProfile


# хенлдер для отправки погоды
# вызовет фу-ию get_location, когда пользователь отправит локацию
@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=UserProfile.location)
async def get_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    weather = await get_weather(lat, lon)

    description = conditions[weather['fact']['condition']]  # достаем описание из словаря погода
    temperature = round(weather['fact']['temp'])  # достаем темпиратуру из словаря погода
    # достаем название локации  из словаря погода
    location = f"{weather['geo_object']['country']['name']}, {weather['geo_object']['province']['name']} - {weather['geo_object']['district']['name']}"

    await state.finish()  # сбрасываем значение локации отправленное пользоватлем
    await message.answer(
        text=f'Темпиратура: {round(temperature)} \n'
             f'Описание: {description} \n'
             f'Локация: {location}',  # текст сообщения с погодой отпровдяемый пользоватлю
        reply_markup=main_keyboard  # клавиатура, отправляемая пользователлю
    )
