import logging
import os

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.environ['TG_BOT_API_TOKEN']
logging.basicConfig(level=logging.INFO)


is_next_content = True
got_content = False
got_style = False

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Handler for /start and /help
    """
    await message.reply(
"""
Этот телеграм-бот является финальным проектом в продвинутом потоке курса DLSchool (Осень 2022) и реализует перенос стиля.

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
    global is_next_content
    is_next_content = True
    await message.answer("Выберите и отправьте фото, на которое будет переноситься стиль")


@dp.message_handler(commands=['style'])
async def receive_style(message: types.Message):
    global is_next_content
    is_next_content = False
    await message.answer("Выберите и отправьте фото, c которого будет переноситься стиль")


@dp.message_handler(content_types=['photo'])
async def photo_processing(message):
    """
    Saves photos sent by user. How the photo will be used is defined by got_content and got_style flags.
    """

    global is_next_content
    global got_content
    global got_style

    # Receive content photo
    if is_next_content:
        await message.photo[-1].download('content.jpg')
        await message.answer("Контент-фото загружено. Используйте /style для загрузки фото-стиля")
        is_next_content = False
        got_content = True

    # Receive style photo
    else:
        await message.photo[-1].download('style.jpg')
        await message.answer("Стиль-фото загружено. Используйте /go для начала переноса")
        is_next_content = True
        got_style = True


@dp.message_handler(commands=['go', 'start_transfer'])
async def start_transfer(message: types.Message):
    
    global is_next_content
    global got_content
    global got_style

    if not got_content:
        is_next_content = True
        await message.answer("Контент-фото не загружено")
        await message.answer("Выберите и отправьте фото, на которое будет переноситься стиль")
    elif not got_style:
        is_next_content = False 
        await message.answer("Стиль-фото не загружено")
        await message.answer("Выберите и отправьте фото, c которого будет переноситься стиль")
    else:
        await message.answer("Go, go, Power Rangers!")
        await message.answer("Процесс может занять некоторое время...")


@dp.message_handler(commands=['cancel'])
async def receive_style(message: types.Message):
    global is_next_content
    global got_content
    global got_style
    is_next_content = True
    got_content = False
    got_style = False
    
    await message.answer("Процесс отменен. Используйте /content и /style, чтобы загрузить изображения")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
