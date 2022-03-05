from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
       [KeyboardButton(text='📍 Отправить геолокацию', request_location=True)],
    ],
    resize_keyboard=True
)
