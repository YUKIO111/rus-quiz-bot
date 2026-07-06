# bot.py
import asyncio
import json
import logging
import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from questions import QUESTIONS

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Token kodda emas, environment'da!
SCORES_FILE = "scores.json"
QUIZ_LEN = 10  # Bitta testdagi maksimal savollar soni

CATEGORIES = {
    "lugat": "📖 Lug'at (A1)",
    "grammatika": "📗 Grammatika (A2–B2)",
    "talaffuz": "🗣 Talaffuz",
}

dp = Dispatcher()
sessions: dict[int, dict] = {}  # user_id -> joriy test holati


# ---------- Natijalarni saqlash (JSON) ----------

def load_scores() -> dict:
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_scores(scores: dict) -> None:
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


# ---------- Klaviaturalar ----------

def main_menu() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=title, callback_data=f"cat:{key}")]
        for key, title in CATEGORIES.items()
    ]
    rows.append(
        [InlineKeyboardButton(text="📊 Natijalarim", callback_data="stats")]
    )
    return InlineKeyboardMarkup(inline_keyboard=rows)


# ---------- Handlerlar ----------

@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    await message.answer(
        "Salom! 🇷🇺 Bu — rus tili quiz boti.\n\n"
        "Kategoriyani tanlang va savollarga javob bering. "
        "Har bir javobdan keyin izoh chiqadi — shu bilan o'rganasiz!",
        reply_markup=main_menu(),
    )


@dp.callback_query(F.data.startswith("cat:"))
async def start_quiz(call: CallbackQuery) -> None:
    category = call.data.split(":", 1)[1]
    pool = QUESTIONS.get(category, [])
    if not pool:
        await call.answer("Bu kategoriyada hali savol yo'q", show_alert=True)
        return

    questions = random.sample(pool, min(QUIZ_LEN, len(pool)))
    sessions[call.from_user.id] = {
        "category": category,
        "questions": questions,
        "index": 0,
        "correct": 0,
    }
    await call.answer()
    await call.message.answer(
        f"{CATEGORIES[category]} testi boshlandi! "
        f"Jami {len(questions)} ta savol. Omad! 🍀"
    )
    await send_question(call.message, call.from_user.id)


async def send_question(message: Message, user_id: int) -> None:
    s = sessions[user_id]
    q = s["questions"][s["index"]]
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=v, callback_data=f"ans:{i}")]
            for i, v in enumerate(q["variantlar"])
        ]
    )
    await message.answer(
        f"❓ Savol {s['index'] + 1}/{len(s['questions'])}\n\n{q['savol']}",
        reply_markup=kb,
    )


@dp.callback_query(F.data.startswith("ans:"))
async def handle_answer(call: CallbackQuery) -> None:
    s = sessions.get(call.from_user.id)
    if not s:
        await call.answer("Avval /start bosib test tanlang", show_alert=True)
        return

    q = s["questions"][s["index"]]
    chosen = int(call.data.split(":", 1)[1])

    if chosen == q["togri"]:
        s["correct"] += 1
        text = f"✅ To'g'ri!\n\n💡 {q['izoh']}"
    else:
        togri_javob = q["variantlar"][q["togri"]]
        text = f"❌ Noto'g'ri. To'g'ri javob: {togri_javob}\n\n💡 {q['izoh']}"

    await call.answer()
    await call.message.edit_reply_markup(reply_markup=None)  # tugmalarni o'chirish
    await call.message.answer(text)

    s["index"] += 1
    if s["index"] < len(s["questions"]):
        await send_question(call.message, call.from_user.id)
    else:
        await finish_quiz(call.message, call.from_user.id)


async def finish_quiz(message: Message, user_id: int) -> None:
    s = sessions.pop(user_id)
    total = len(s["questions"])
    correct = s["correct"]
    percent = round(correct / total * 100)

    # Eng yaxshi natijani saqlash
    scores = load_scores()
    user_scores = scores.setdefault(str(user_id), {})
    best = user_scores.get(s["category"], 0)
    if percent > best:
        user_scores[s["category"]] = percent
        save_scores(scores)

    if percent >= 80:
        baho = "🏆 Ajoyib!"
    elif percent >= 50:
        baho = "👍 Yaxshi, davom eting!"
    else:
        baho = "📚 Yana mashq qilish kerak."

    await message.answer(
        f"Test tugadi! 🎉\n\n"
        f"Natija: {correct}/{total} ({percent}%)\n{baho}",
        reply_markup=main_menu(),
    )


@dp.callback_query(F.data == "stats")
async def show_stats(call: CallbackQuery) -> None:
    user_scores = load_scores().get(str(call.from_user.id), {})
    await call.answer()
    if not user_scores:
        await call.message.answer("Siz hali test yechmagansiz. Boshlaymizmi? 😉")
        return

    lines = ["📊 Eng yaxshi natijalaringiz:\n"]
    for key, title in CATEGORIES.items():
        if key in user_scores:
            lines.append(f"{title}: {user_scores[key]}%")
    await call.message.answer("\n".join(lines))


# ---------- Ishga tushirish ----------

async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment o'zgaruvchisi topilmadi!")
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
