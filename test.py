import asyncio
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import InputFile

# Set up Telegram bot
bot_token = '7558765085:AAHA9j4WIlNfpkWXGoaErnowFFFRKaMtsk0'
chat_id = '6731228814'
bot = Bot(token=bot_token)

dp = Dispatcher()

# Define an async function to send the photo
async def send_photo(chat_id, image_path):
    try:
        # Use InputFile to wrap the image path
        photo = InputFile(image_path)
        await bot.send_photo(chat_id=chat_id, photo=photo)
    except PermissionError as e:
        print(f"PermissionError: {e}")
    finally:
        await bot.session.close()  # Close the bot session properly

# Run the async function
async def main():
    image_path = 'C:\\Users\\josej\\OneDrive\\Documentos\\GitHub\\intruder_detection\\output_images\\human_output_with_boxes_20240924_223444.jpg'
    await send_photo(chat_id, image_path)

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())

