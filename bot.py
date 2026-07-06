# bot.py — v4: Tozalangan versiya — welcome + Web App tugmasi
# Testlar va lug'at endi Web App (Mini App) ichida bo'ladi.
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    WebAppInfo,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "")  # Web App tayyor bo'lgach Railway'da shu o'zgaruvchiga link qo'yamiz
LINE = "━━━━━━━━━━━━━"

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    name = message.from_user.first_name or "do'st"
    text = (
        f"👋 <b>Salom, {name}!</b>\n"
        f"{LINE}\n"
        "🇷🇺 <b>Rus tili o'rganish botiga xush kelibsiz!</b>\n\n"
        "Bu yerda sizni kutmoqda:\n"
        "   📚 0 dan PRO gacha testlar\n"
        "   ⛩ Anime lug'ati — 230+ so'z\n"
        "   🎯 Daraja va natijalar tizimi\n"
        f"{LINE}\n"
        "👇 Boshlash uchun tugmani bosing!"
    )
    if WEBAPP_URL:
        kb = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(
                text="🚀 O'rganishni boshlash",
                web_app=WebAppInfo(url=WEBAPP_URL),
            )
        ]])
        await message.answer(text, reply_markup=kb)
    else:
        await message.answer(
            text + "\n\n<i>⚙️ Ilova hozircha tayyorlanmoqda — tez orada!</i>"
        )


@dp.message()
async def fallback(message: Message) -> None:
    await message.answer("👇 /start buyrug'ini bosing 😊")


async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment o'zgaruvchisi topilmadi!")
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
