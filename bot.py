import asyncio
import logging
import json

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher()




@dp.message(F.text, Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, который отправляет файлы из ответов из других чатов, даже приватных. Просто отправь мне свой ответ с функцией 'Ответить в другом чате' (Или перешли такое) на сообщение , которое ты хочешь получить, и я отправлю его тебе.")
@dp.message(F.text)
async def cmd_start(message: types.Message):
    json_data = message.model_dump_json()
    data = json.loads(json_data)
    file2 = data["external_reply"]
    try:
        file3 = file2["animation"]
        file4 = file3["file_id"]
        await message.answer("Загружаю гифку")
        print(file4)
        file = await bot.get_file(file4)
        await bot.download_file(file.file_path, "file.gif")
        text_file = FSInputFile("file.gif")
        await message.answer_animation(text_file)
    except:
        try:
            file3 = file2["voice"]
            file4 = file3["file_id"]
            await message.answer("Загружаю голосовое сообщение")
            print(file4)
            file = await bot.get_file(file4)
            await bot.download_file(file.file_path, "file.ogg")
            text_file = FSInputFile("file.ogg")
            await message.answer_voice(text_file)
        except:
            try:
                file3 = file2["video"]
                file4 = file3["file_id"]
                await message.answer("Загружаю видео")
                print(file4)
                file = await bot.get_file(file4)
                await bot.download_file(file.file_path, "file.mp4")
                text_file = FSInputFile("file.mp4")
                await message.answer_video(text_file)
            except:
                try:
                    file3 = file2["photo"]
                    print(file3)
                    file4 = file3[-1]["file_id"]
                    await message.answer("Загружаю фото")
                    print(file4)
                    file = await bot.get_file(file4)
                    await bot.download_file(file.file_path, "file.jpg")
                    text_file = FSInputFile("file.jpg")
                    await message.answer_photo(text_file)
                except:
                    await message.answer("Не могу обработать этот тип данных")


async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
