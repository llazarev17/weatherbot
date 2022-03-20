from aiogram import types
from loader import dp
from states import UserProfile
from ketboards.default import location_keyboard


@dp.message_handler(text='🌤 Погода сейчас') # декоратор фильтрует сообщение: 'Погода сейчас'
async def get_weather(message: types.Message): # фу-ия будет вызвана, как поступит сообщение  с текстом 'Погода сейчас'
    await message.answer(
        f'Отправь свою геолокацию, чтобы я показал тебе погоду:',  # текст сообщения, которое получит пользователь
        reply_markup=location_keyboard  # клавиатура, которую полчит пользователь
    )
    await UserProfile.first()

