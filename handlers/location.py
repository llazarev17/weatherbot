from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
# from utils.db.schemas import User
from ketboards.default import main_keyboard
from states import UserProfile


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=UserProfile.location)
async def get_location(message: types.Message, state: FSMContext):
    await message.answer(
        text='Вот список того, что я умею',
        reply_markup=main_keyboard
    )
