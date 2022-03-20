from aiogram import Dispatcher, types


# фу-ия принимает на вход диспатчер
# сетапит команды для бота
async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
    ])
