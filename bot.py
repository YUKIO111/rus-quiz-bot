# bot.py — v2
# Yangiliklar: bitta xabarda ishlaydi (chat toza qoladi), HTML format,
# progress bar, daraja (rank) tizimi, "Keyingi savol" tugmasi.
import asyncio
import json
import logging
import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from questions import CATEGORIES, QUESTIONS

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SCORES_FILE = "scores.json"
QUIZ_LEN = 10  # bitta testdagi maksimal savollar soni
LINE = "───────────────"

dp = Dispatcher()
sessions: dict[int, dict] = {}  # user_id -> joriy test holati

RANKS = [
    (95, "🏆 PRO"),
    (80, "🥇 Usta"),
    (60, "🥈 Bilimdon"),
    (40, "🥉 O'rganuvchi"),
    (0, "🌱 Yangi boshlovchi"),
]


def get_rank(avg: float) -> str:
    for limit, name in RANKS:
        if avg >= limit:
            return name
    return RANKS[-1][1]


def progress_bar(value: int, total: int, width: int = 10) -> str:
    filled = round(width * value / total) if total else 0
    return "▰" * filled + "▱" * (width - filled)


# ---------- Natijalarni saqlash (JSON) ----------

def load_scores() -> dict:
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_scores(scores: dict) -> None:
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


# ---------- Menyu ----------

def menu_text() -> str:
    return (
        "🇷🇺 <b>Rus tili Quiz Bot</b>\n"
        f"{LINE}\n"
        "0 dan 🏆 PRO gacha — o'zingizga mos bo'limni tanlang.\n"
        "Har javobdan keyin izoh chiqadi — shu bilan o'rganasiz 😉"
    )


def main_menu() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=title, callback_data=f"cat:{key}")]
        for key, title in CATEGORIES.items()
    ]
    rows.append(
        [InlineKeyboardButton(text="📊 Natijalarim va darajam", callback_data="stats")]
    )
    return InlineKeyboardMarkup(inline_keyboard=rows)


@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    await message.answer(menu_text(), reply_markup=main_menu())


@dp.callback_query(F.data == "menu")
async def back_to_menu(call: CallbackQuery) -> None:
    await call.answer()
    await call.message.edit_text(menu_text(), reply_markup=main_menu())


# ---------- Test ----------

@dp.callback_query(F.data.startswith("cat:"))
async def start_quiz(call: CallbackQuery) -> None:
    category = call.data.split(":", 1)[1]
    pool = QUESTIONS.get(category, [])
    if not pool:
        await call.answer("Bu bo'limda hali savol yo'q", show_alert=True)
        return

    questions = random.sample(pool, min(QUIZ_LEN, len(pool)))
    sessions[call.from_user.id] = {
        "category": category,
        "questions": questions,
        "index": 0,
        "correct": 0,
    }
    await call.answer()
    await show_question(call)


async def show_question(call: CallbackQuery) -> None:
    s = sessions[call.from_user.id]
    q = s["questions"][s["index"]]
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=v, callback_data=f"ans:{i}")]
            for i, v in enumerate(q["variantlar"])
        ]
    )
    text = (
        f"{CATEGORIES[s['category']]}\n"
        f"{progress_bar(s['index'], len(s['questions']))}  "
        f"<b>{s['index'] + 1}/{len(s['questions'])}</b>\n"
        f"{LINE}\n\n"
        f"❓ <b>{q['savol']}</b>"
    )
    await call.message.edit_text(text, reply_markup=kb)


@dp.callback_query(F.data.startswith("ans:"))
async def handle_answer(call: CallbackQuery) -> None:
    s = sessions.get(call.from_user.id)
    if not s:
        await call.answer("Avval /start bosib bo'lim tanlang", show_alert=True)
        return

    q = s["questions"][s["index"]]
    chosen = int(call.data.split(":", 1)[1])

    if chosen == q["togri"]:
        s["correct"] += 1
        head = "✅ <b>To'g'ri!</b>"
    else:
        head = (
            "❌ <b>Noto'g'ri.</b>\n"
            f"To'g'ri javob: <b>{q['variantlar'][q['togri']]}</b>"
        )

    s["index"] += 1
    last = s["index"] >= len(s["questions"])
    btn = "🏁 Natijani ko'rish" if last else "➡️ Keyingi savol"
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=btn, callback_data="next")]]
    )
    text = (
        f"{head}\n\n"
        f"💡 <i>{q['izoh']}</i>\n"
        f"{LINE}\n"
        f"Hisob: <b>{s['correct']}/{s['index']}</b>"
    )
    await call.answer()
    await call.message.edit_text(text, reply_markup=kb)


@dp.callback_query(F.data == "next")
async def next_step(call: CallbackQuery) -> None:
    s = sessions.get(call.from_user.id)
    if not s:
        await call.answer("Test topilmadi. /start bosing", show_alert=True)
        return
    await call.answer()
    if s["index"] < len(s["questions"]):
        await show_question(call)
    else:
        await finish_quiz(call)


async def finish_quiz(call: CallbackQuery) -> None:
    s = sessions.pop(call.from_user.id)
    total = len(s["questions"])
    correct = s["correct"]
    percent = round(correct / total * 100)

    scores = load_scores()
    user_scores = scores.setdefault(str(call.from_user.id), {})
    rekord = ""
    if percent > user_scores.get(s["category"], 0):
        user_scores[s["category"]] = percent
        save_scores(scores)
        rekord = "\n🎖 <b>Yangi shaxsiy rekord!</b>"

    if percent >= 90:
        baho = "🏆 Zo'r! PRO darajaga juda yaqinsiz!"
    elif percent >= 70:
        baho = "🥇 Juda yaxshi natija!"
    elif percent >= 50:
        baho = "👍 Yaxshi, davom eting!"
    else:
        baho = "📚 Yana mashq qilamiz — hammasi oldinda!"

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Qayta yechish", callback_data=f"cat:{s['category']}")],
            [InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu")],
        ]
    )
    await call.message.edit_text(
        f"🏁 <b>Test tugadi!</b>\n"
        f"{LINE}\n\n"
        f"{CATEGORIES[s['category']]}\n"
        f"{progress_bar(correct, total)}  <b>{correct}/{total}</b> ({percent}%)\n\n"
        f"{baho}{rekord}",
        reply_markup=kb,
    )


# ---------- Statistika va daraja ----------

@dp.callback_query(F.data == "stats")
async def show_stats(call: CallbackQuery) -> None:
    user_scores = load_scores().get(str(call.from_user.id), {})
    await call.answer()
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="menu")]]
    )
    if not user_scores:
        await call.message.edit_text(
            "📊 Siz hali test yechmagansiz.\nBirinchi bo'limni boshlaymizmi? 😉",
            reply_markup=kb,
        )
        return

    lines = [f"📊 <b>Eng yaxshi natijalaringiz</b>\n{LINE}"]
    for key, title in CATEGORIES.items():
        pct = user_scores.get(key)
        if pct is not None:
            lines.append(f"{title}\n{progress_bar(pct, 100)}  <b>{pct}%</b>")
        else:
            lines.append(f"{title}\n{progress_bar(0, 100)}  <i>hali yechilmagan</i>")

    avg = sum(user_scores.get(k, 0) for k in CATEGORIES) / len(CATEGORIES)
    lines.append(
        f"{LINE}\nDarajangiz: <b>{get_rank(avg)}</b>\n"
        "<i>🏆 PRO bo'lish uchun barcha bo'limlarda 95%+ to'plang!</i>"
    )
    await call.message.edit_text("\n\n".join(lines), reply_markup=kb)


# ---------- Ishga tushirish ----------

async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment o'zgaruvchisi topilmadi!")
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
