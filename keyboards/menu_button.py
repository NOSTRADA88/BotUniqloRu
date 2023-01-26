from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Начало работы с ботом'),
        # types.BotCommand(command='/help', description='Справка по работе бота'),
        # types.BotCommand(command='/support', description='Поддержка'),
        # types.BotCommand(command='/contacts', description='Другие способы связи')
    ]
    await dp.bot.set_my_commands(main_menu_commands)


test_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
test_button1 = KeyboardButton(text="Тестовая кнопка номер 1")
test_button2 = KeyboardButton(text="Тестовая кнопка номер 2")
test_button3 = KeyboardButton(text="Тестовая кнопка номер 3")
test_button4 = KeyboardButton(text="Тестовая кнопка номер 4")
test_kb.add(test_button1).add(test_button2).add(test_button3, test_button4)


test_ikb = InlineKeyboardMarkup(row_width=2)
inline_button1 = InlineKeyboardButton(text="Инлайн кнопка 1", callback_data="button1")
inline_button2 = InlineKeyboardButton(text="Инлайн кнопка 2", callback_data="button2")
inline_button3 = InlineKeyboardButton(text="Инлайн кнопка 3", url="https://github.com/aiogram/deta/issues")
inline_button4 = InlineKeyboardButton(text="Инлайн кнопка 4", url="https://github.com/settings/profile")
test_ikb.add(inline_button1).add(inline_button2).add(inline_button3, inline_button4)

