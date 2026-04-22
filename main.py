import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
TOKEN = "8765087703:AAEtnnpfQsCH6pzi3sli6zMiYik2m5A3Zcg"
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Присоединиться к игре 🎮", 
                web_app=WebAppInfo(url="https://www.google.com")
            )
        ],
        [
            InlineKeyboardButton(
                text="Получить нашу карту 💳", 
                url="https://www.mtbank.by/cards/halva/"
            )
        ]
    ])
    await message.answer(
        "👋 Добро пожаловать в МТбанк!\n\n"
        "Присоединяйся к игре для ранних последователей или оформи свою карту прямо сейчас.",
        reply_markup=keyboard
    )
async def main():
    print("Бот запущен! Заходи в Телеграм и пиши /start")
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")