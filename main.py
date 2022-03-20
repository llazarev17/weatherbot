from aiogram import Dispatcher

#  фу-ия будет вызвана при старте бота
async def on_startup(dispatcher: Dispatcher):
    from utils.commands import set_commands
    await set_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor, Dispatcher
    from handlers import dp

    #  запуск бота
    executor.start_polling(dp, on_startup=on_startup)
