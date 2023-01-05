from aiogram import Dispatcher, types

async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Начало работы с ботом'),
        types.BotCommand(command='/help', description='Справка по работе бота'),
        types.BotCommand(command='/support', description='Поддержка'),
        types.BotCommand(command='/contacts', description='Другие способы связи')
    ]
    await dp.bot.set_my_commands(main_menu_commands)