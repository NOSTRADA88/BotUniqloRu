from asyncio import new_event_loop
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from BotUniqloRu.config import load_config
from keyboards.menu_button import set_main_menu
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from keyboards.menu_button import test_ikb, test_kb
config = load_config('.env')

loop = new_event_loop()
bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML') # creating object bot
dp: Dispatcher = Dispatcher(bot, loop=loop) # creating object dp

async def on_startup(dp):
    await set_main_menu(dp)

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True) # creating object keyboard

    # creating objects buttons
button_1: KeyboardButton = KeyboardButton('Dogs')
button_2: KeyboardButton = KeyboardButton('Lions')

keyboard.add(button_1, button_2) #adding buttons

client = AsyncIOMotorClient(config.db_link.link)
collection = client.UniqloThailand.clothes

# async def add_user(user_id):
#     date = datetime.now().date()
#     collection.insert_one({
#         "_id": user_id,
#         "date": str(date)
#     })
async def process_start_command(message: types.Message):
    await message.answer('how scared u most?', reply_markup=test_kb) # /start
    user_id = message.chat.id
    # await add_user(user_id)
async def process_dog_answer(message: types.Message):
    await message.answer('Dogs are the best creatures', reply_markup=ReplyKeyboardRemove()) # dogs answer + chat bar closing

async def process_lion_answer(message: types.Message):
    await message.answer('Lions pretty scary =(', reply_markup=ReplyKeyboardRemove()) # lions answer + chat bar closing

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_dog_answer, text='Dogs')
dp.register_message_handler(process_lion_answer, text='Lions')


@dp.message_handler(Text(equals="Тестовая кнопка номер 1"))
async def kb_button1(messasge: types.Message):
    await messasge.answer(text="Ты нажал на кнопку 1", reply_markup=test_ikb)


@dp.message_handler(Text(equals="Тестовая кнопка номер 2"))
async def kb_button1(messasge: types.Message):
    await messasge.answer(text="Ты нажал на кнопку 2", reply_markup=test_ikb)


@dp.message_handler(Text(equals="Тестовая кнопка номер 3"))
async def kb_button1(messasge: types.Message):
    await messasge.answer(text="Ты нажал на кнопку 3", reply_markup=test_ikb)


@dp.message_handler(Text(equals="Тестовая кнопка номер 4"))
async def kb_button1(messasge: types.Message):
    await messasge.answer(text="Ты нажал на кнопку 4", reply_markup=test_ikb)


@dp.callback_query_handler()
async def inline_test(callback: types.CallbackQuery):
    if callback.data == "button1":
        await callback.message.answer(text="Ты нажал на инлайн кнопку 1")
    if callback.data == "button2":
        await callback.message.answer(text="Ты нажал на инлайн кнопку 2")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



