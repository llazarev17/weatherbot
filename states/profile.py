from aiogram.dispatcher.filters.state import StatesGroup, State


# класс хранит значение локации, переданное пользоватлем
class UserProfile(StatesGroup):
    location = State()
