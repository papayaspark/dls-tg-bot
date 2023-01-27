import logging
import os

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.environ['TG_BOT_API_TOKEN']


next_is_content = True


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Handler for /start and /help
    """
    await message.reply(
"""
Этот телеграм-бот является финальным проектом в курсе DLSchool (Осень 2022) и реализует перенос стиля.

Доступные команды:
/start, /help - выводит данное сообщение;
/content - указывает, что загружаемое изображение - то, на которое будет переноситься стиль;
/style - указывает, что загружаемое изображение является "донором" стиля;
/go, /start_transfer - начинает процесс переноса и выводит результат после завершения этого процесса;
/cancel - отменяет все предыдущие действия (весь процесс придется начинать заново).

Типичная последовательность работы с ботом:
1) /start;
2) /content;
3) загрузить фото;
4) /style;
5) загрузить фото;
6) /go (полученное изображение будет выведено в чат).
        
""")


@dp.message_handler(commands=['content'])
async def receive_content(message: types.Message):
    next_is_content = True
    await message.answer("Выберите и отправьте фото, на которое будет переноситься стиль")


@dp.message_handler(commands=['style'])
async def receive_style(message: types.Message):
    next_is_content = False
    await message.answer("Выберите и отправьте фото, c которого будет переноситься стиль")


@dp.message_handler(commands=['go'])
async def start_transfer(message: types.Message):
    await message.answer("Go, go, Power Rangers!")
    await message.answer("This may take a while...")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
