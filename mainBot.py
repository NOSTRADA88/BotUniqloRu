import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType
from config import load_config
from aiogram.types.web_app_info import WebAppInfo
from keyboards.menu_button import set_main_menu

logger = logging.getLogger(__name__)



async def main():
    logging.basicConfig(level=logging.INFO, format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
                        u'[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    config = load_config('.env')

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML') # creating object bot
    dp: Dispatcher = Dispatcher(bot) # creating object dp

    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True) # creating object keyboard

    # creating objects buttons
    button_1: KeyboardButton = KeyboardButton('Dogs')
    button_2: KeyboardButton = KeyboardButton('Lions')

    keyboard.add(button_1, button_2) #adding buttons
    keyboard.add(KeyboardButton(text='Отправить телефон', request_contact=True))
    keyboard.add(KeyboardButton(text='Отправить геолокацию', request_location=True))
    keyboard.add(KeyboardButton(text='Start Web App', web_app=WebAppInfo(url="https://stepik.org/")))

    async def process_start_command(message: types.Message):
        await message.answer('What scares u more ?', reply_markup=keyboard) # /start

    async def process_dog_answer(message: types.Message):
        await message.answer('Dogs are the best creatures', reply_markup=ReplyKeyboardRemove()) # dogs answer + chat bar closing

    async def process_lion_answer(message: types.Message):
        await message.answer('Lions pretty scary =(', reply_markup=ReplyKeyboardRemove()) # lions answer + chat bar closing

    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_dog_answer, text='Dogs')
    dp.register_message_handler(process_lion_answer, text='Lions')

    # @dp.message_handler(commands=['start'])
    # async def process_start_command(message: types.Message):
    #     await message.answer('zxc\nsad')
    #
    # @dp.message_handler(commands=['help'])
    # async def process_help_commend(message: types.Message):
    #     await message.answer('kill me')
    #
    # @dp.message_handler()
    # async def send_echo(message: types.Message):
    #     await message.reply(message.text)
    await set_main_menu(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot was stopped')
