from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import Router
import asyncio

TKN_API = "7610963065:AAESZu7gb89TMkmQLGRQGO3JzwZpZ5dmnmk"
bot = Bot(token=TKN_API)
dp = Dispatcher()
router = Router()


@router.message()
async def echo(message: Message):
    await message.answer(text=message.text)


async def echotgbot():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(echotgbot())
