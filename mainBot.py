from aiogram import Bot, Dispatcher, executor, types
import settings

API_TOKEN = settings.token # Bot token

bot: Bot = Bot(token=API_TOKEN) # creating object bot
dp: Dispatcher = Dispatcher(bot) # creating object dp

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('zxc\nsad')

@dp.message_handler(commands=['help'])
async def process_help_commend(message: types.Message):
    await message.answer('kill me')

@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
