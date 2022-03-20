from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# переменная, в которой храним клавиатуру с основным меню
# В будущем можно реализовать закоментированные команды
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🌤 Погода сейчас'),
            # KeyboardButton(' 🌅 На завтра')
        ],
        # [
        #     # KeyboardButton('🔮 На 5 дней'),
        #     KeyboardButton('🔮 На 10 дней')
        # ],
        # [
        #     KeyboardButton('⚙️ Настройки')
        # ]
    ],
    resize_keyboard=True
)
