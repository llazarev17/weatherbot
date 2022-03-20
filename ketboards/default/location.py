from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# переменная, в которой храним клавиатуру для отправки локации
location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
       [KeyboardButton(text='📍 Отправить геолокацию', request_location=True)],
    ],
    resize_keyboard=True
)
