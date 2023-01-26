import logging
import os

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.environ['TG_BOT_API_TOKEN']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Handler for /start and /help
    """
    await message.reply("Bust a move.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
