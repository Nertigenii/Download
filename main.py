import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = '8764717680:AAGYsxqVJp-JpFTN4hwLEQSgJ0msCC1KYAg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def get_tiktok_video(url):
    api_url = "https://tikwm.com/api/"
    params = {
        "url": url
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    if data.get("data"):
        return data["data"]["play"]  # ссылка без водяного знака
    return None


@dp.message_handler()
async def handle_message(message: Message):
    text = message.text

    if "tiktok.com" in text:
        await message.reply("⏳ Скачиваю видео...")

        video_url = get_tiktok_video(text)

        if video_url:
            await message.answer_video(video_url)
        else:
            await message.reply("❌ Не удалось скачать видео")
    else:
        await message.reply("Отправь ссылку на TikTok")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
