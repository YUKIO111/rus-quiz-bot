# questions.py
# Savollar bazasi: 0 dan PRO gacha, 6 bo'lim.
# Yangi savol qo'shish uchun kerakli ro'yxatga yangi dict qo'shing.

CATEGORIES = {
    "lugat_a1": "📖 Lug'at — A1",
    "lugat_a2": "📚 Lug'at — A2–B1",
    "gram_a1": "📘 Grammatika — A1",
    "gram_b": "📗 Grammatika — A2–B2",
    "talaffuz": "🗣 Talaffuz",
    "suhbat": "💬 Jonli so'zlashuv",
}

QUESTIONS = {
    "lugat_a1": [
        {"savol": "«Молоко» so'zining ma'nosi nima?", "variantlar": ["Suv", "Sut", "Non", "Choy"], "togri": 1, "izoh": "Молоко — sut. Talaffuzi: «malako»."},
        {"savol": "«Книга» so'zining ma'nosi nima?", "variantlar": ["Deraza", "Stol", "Kitob", "Eshik"], "togri": 2, "izoh": "Книга — kitob. Urg'u: КНИ́-га."},
        {"savol": "«Окно» so'zining ma'nosi nima?", "variantlar": ["Deraza", "Devor", "Shift", "Pol"], "togri": 0, "izoh": "Окно — deraza. Urg'u oxirida: «akno»."},
        {"savol": "«Вода» so'zining ma'nosi nima?", "variantlar": ["Suv", "Olov", "Havo", "Tuproq"], "togri": 0, "izoh": "Вода — suv. Talaffuzi: «vada»."},
        {"savol": "«Друг» so'zining ma'nosi nima?", "variantlar": ["Dushman", "Qo'shni", "Do'st", "Aka"], "togri": 2, "izoh": "Друг — do'st. Talaffuzi: «druk»."},
        {"savol": "«Хлеб» so'zining ma'nosi nima?", "variantlar": ["Non", "Suv", "Go'sht", "Tuz"], "togri": 0, "izoh": "Хлеб — non. Talaffuzi: «xlep»."},
        {"savol": "«Дом» so'zining ma'nosi nima?", "variantlar": ["Uy", "Ko'cha", "Shahar", "Xona"], "togri": 0, "izoh": "Дом — uy. Я дома — Men uydaman."},
        {"savol": "«Кошка» so'zining ma'nosi nima?", "variantlar": ["It", "Mushuk", "Qush", "Sigir"], "togri": 1, "izoh": "Кошка — mushuk. It esa — собака."},
        {"savol": "«Семья» so'zining ma'nosi nima?", "variantlar": ["Do'stlar", "Oila", "Qo'shnilar", "Bolalar"], "togri": 1, "izoh": "Семья — oila. Talaffuzi: «sim'ya»."},
        {"savol": "«Rahmat» ruschada qanday aytiladi?", "variantlar": ["Пожалуйста", "Спасибо", "Привет", "Пока"], "togri": 1, "izoh": "Спасибо — rahmat. Javobi: Пожалуйста (arzimaydi)."},
    ],
    "lugat_a2": [
        {"savol": "«Путешествие» so'zining ma'nosi nima?", "variantlar": ["Sayohat", "Uchrashuv", "Bayram", "Dam olish"], "togri": 0, "izoh": "Путешествие — sayohat. Путь — yo'l so'zidan."},
        {"savol": "«Здоровье» so'zining ma'nosi nima?", "variantlar": ["Baxt", "Salomatlik", "Boylik", "Kuch"], "togri": 1, "izoh": "Здоровье — salomatlik. Здоровый — sog'lom."},
        {"savol": "«Мечта» so'zining ma'nosi nima?", "variantlar": ["Xotira", "Orzu", "Reja", "Maqsad"], "togri": 1, "izoh": "Мечта — orzu. Мечтать — orzu qilmoq."},
        {"savol": "«Успех» so'zining ma'nosi nima?", "variantlar": ["Omad", "Muvaffaqiyat", "G'alaba", "Baxt"], "togri": 1, "izoh": "Успех — muvaffaqiyat. Успешный — muvaffaqiyatli."},
        {"savol": "«Опаздывать» fe'lining ma'nosi nima?", "variantlar": ["Shoshilmoq", "Kechikmoq", "Kutmoq", "Yugurmoq"], "togri": 1, "izoh": "Опаздывать — kechikmoq. Я опаздываю — kechikyapman."},
        {"savol": "«Удивляться» fe'lining ma'nosi nima?", "variantlar": ["Xafa bo'lmoq", "Hayron qolmoq", "Quvonmoq", "Qo'rqmoq"], "togri": 1, "izoh": "Удивляться — hayron qolmoq. -ся — o'zlik qo'shimchasi."},
        {"savol": "«Приходить» fe'lining ma'nosi nima?", "variantlar": ["Ketmoq", "Kelmoq", "Qolmoq", "Chiqmoq"], "togri": 1, "izoh": "При- old qo'shimchasi yaqinlashishni bildiradi: приходить — kelmoq."},
        {"savol": "«Вспоминать» fe'lining ma'nosi nima?", "variantlar": ["Unutmoq", "Eslamoq", "O'ylamoq", "Bilmoq"], "togri": 1, "izoh": "Вспоминать — eslamoq. Unutmoq esa — забывать."},
    ],
    "gram_a1": [
        {"savol": "Rus tilida nechta jins (род) bor?", "variantlar": ["2 ta", "3 ta", "4 ta", "Jins yo'q"], "togri": 1, "izoh": "3 ta: мужской (erkak), женский (ayol), средний (o'rta)."},
        {"savol": "«Книга» so'zi qaysi jinsda?", "variantlar": ["Мужской", "Женский", "Средний", "Jinsi yo'q"], "togri": 1, "izoh": "-а bilan tugagan so'zlar odatda женский род: книга, вода, школа."},
        {"savol": "«Окно» so'zi qaysi jinsda?", "variantlar": ["Мужской", "Женский", "Средний", "Ko'plik"], "togri": 2, "izoh": "-о/-е bilan tugagan so'zlar средний род: окно, молоко, море."},
        {"savol": "«Я студент» gapining to'g'ri tarjimasi qaysi?", "variantlar": ["Men talabaman", "U talaba", "Men talaba edim", "Men talaba bo'laman"], "togri": 0, "izoh": "Hozirgi zamonda «быть» tushib qoladi: Я студент = Men talabaman."},
        {"savol": "«Вы» qachon ishlatiladi?", "variantlar": ["Faqat ko'plikda", "Hurmat va rasmiylikda (hamda ko'plikda)", "Faqat do'stlarga", "Faqat bolalarga"], "togri": 1, "izoh": "Вы — «siz»: notanish/katta odamlarga va ko'plikda. Ты — yaqinlarga."},
        {"savol": "«Книга» so'zining ko'pligi qaysi?", "variantlar": ["Книгы", "Книги", "Книгов", "Книгалар"], "togri": 1, "izoh": "г, к, х dan keyin ы emas, и yoziladi: книга → книги."},
        {"savol": "«Mening kitobim» ruschada qanday?", "variantlar": ["Мой книга", "Моя книга", "Моё книга", "Мои книга"], "togri": 1, "izoh": "Книга — женский род, shuning uchun моя: моя книга."},
        {"savol": "«Молоко» o'rniga qaysi olmosh qo'yiladi?", "variantlar": ["Он", "Она", "Оно", "Они"], "togri": 2, "izoh": "Средний род so'zlar — оно: молоко → оно."},
    ],
    "gram_b": [
        {"savol": "Rus tilida nechta kelishik bor?", "variantlar": ["4 ta", "5 ta", "6 ta", "7 ta"], "togri": 2, "izoh": "6 ta: именительный, родительный, дательный, винительный, творительный, предложный."},
        {"savol": "«Я читаю книгу» gapida «книгу» qaysi kelishikda?", "variantlar": ["Именительный", "Родительный", "Винительный", "Дательный"], "togri": 2, "izoh": "Винительный (tushum): книга → книгу (-а → -у)."},
        {"savol": "«Говорить» fe'li qaysi tuslanishga kiradi?", "variantlar": ["1-tuslanish", "2-tuslanish", "Noto'g'ri fe'l", "Tuslanmaydi"], "togri": 1, "izoh": "-ить fe'llari 2-tuslanish: я говорю, ты говоришь."},
        {"savol": "«Читать» va «прочитать» farqi nimada?", "variantlar": ["Zamon farqi", "Davomiy va tugallangan ish (вид)", "Jins farqi", "Farqi yo'q"], "togri": 1, "izoh": "Читать — jarayon (o'qib turish), прочитать — tugallangan (o'qib bo'lish). Bu — вид (aspekt)."},
        {"savol": "«У меня есть кот» gapining ma'nosi nima?", "variantlar": ["Men mushukman", "Menda mushuk bor", "Mushukni ko'rdim", "Mushuk yo'q"], "togri": 1, "izoh": "У меня есть... — «Menda ... bor» konstruksiyasi."},
        {"savol": "«Идти» va «ходить» farqi nimada?", "variantlar": ["Farqi yo'q", "Идти — hozir bir yo'nalishda, ходить — takroriy", "Идти — yugurish", "Ходить — faqat o'tgan zamon"], "togri": 1, "izoh": "Идти — hozir bir tomonga ketyapman; ходить — doim/takror boraman (harakat fe'llari)."},
        {"savol": "O'tgan zamonda ayol jinsida fe'l qanday tugaydi?", "variantlar": ["-л", "-ла", "-ло", "-ли"], "togri": 1, "izoh": "Он читал, она читала, оно читало, они читали."},
        {"savol": "«Если бы у меня было время...» nimani bildiradi?", "variantlar": ["Kelasi zamon", "Shart mayli (bo'lganida edi)", "Buyruq", "Savol"], "togri": 1, "izoh": "бы + o'tgan zamon = shart mayli: «Agar vaqtim bo'lganida edi...»"},
    ],
    "talaffuz": [
        {"savol": "Urg'usiz «о» harfi odatda qanday o'qiladi?", "variantlar": ["«о» kabi", "«а» kabi", "«у» kabi", "O'qilmaydi"], "togri": 1, "izoh": "Urg'usiz «о» — «а» kabi: молоко → «malako»."},
        {"savol": "Qaysi undoshlar HAR DOIM qattiq talaffuz qilinadi?", "variantlar": ["Б, В, Г", "Ж, Ш, Ц", "Ч, Щ, Й", "Л, М, Н"], "togri": 1, "izoh": "Ж, Ш, Ц har doim qattiq: жить → «jыt'»."},
        {"savol": "«Молоко» so'zi qanday talaffuz qilinadi?", "variantlar": ["moloko", "malako", "muluko", "meleko"], "togri": 1, "izoh": "Urg'u oxirida: мо-ло-КО́ → «malako»."},
        {"savol": "So'z oxiridagi jarangli undoshlar qanday aytiladi?", "variantlar": ["Jarangli qoladi", "Jarangsiz aytiladi", "Tushib qoladi", "Cho'ziq aytiladi"], "togri": 1, "izoh": "друг → «druk», хлеб → «xlep»."},
        {"savol": "«ь» (myagkiy znak) belgisi nima vazifa bajaradi?", "variantlar": ["Unlini cho'zadi", "Undoshni yumshatadi", "Urg'uni ko'rsatadi", "Hech narsa"], "togri": 1, "izoh": "ь — oldingi undoshni yumshatadi: говорить → «т'» yumshoq."},
        {"savol": "Rus tilida urg'u (ударение) qanday?", "variantlar": ["Doim oxirgi bo'g'inda", "Doim birinchi bo'g'inda", "Erkin — istalgan bo'g'inda", "Urg'u yo'q"], "togri": 2, "izoh": "Urg'u erkin va ma'noni o'zgartiradi: за́мок (qal'a) — замо́к (qulf)."},
        {"savol": "«Хлеб» so'zi qanday aytiladi?", "variantlar": ["xleb", "xlep", "xlyob", "xlip"], "togri": 1, "izoh": "So'z oxirida б → п: «xlep»."},
        {"savol": "«Ч» harfi qanday talaffuz qilinadi?", "variantlar": ["Doim qattiq", "Doim yumshoq", "Ba'zan qattiq, ba'zan yumshoq", "O'qilmaydi"], "togri": 1, "izoh": "Ч va Щ har doim yumshoq (Ж, Ш, Ц esa har doim qattiq)."},
    ],
    "suhbat": [
        {"savol": "«Как дела?» nimani bildiradi?", "variantlar": ["Ismingiz nima?", "Ishlaring qalay?", "Qayerdansiz?", "Necha yoshdasiz?"], "togri": 1, "izoh": "Как дела? — Qalaysan? Javob: Нормально / Хорошо / Отлично."},
        {"savol": "Xayrlashayotganda «Давай!» nimani bildiradi?", "variantlar": ["Ber!", "Xayr / ko'rishguncha", "Tezroq!", "Boshla!"], "togri": 1, "izoh": "Давай ko'p ma'noli: «xayr», «kelishdik», «boshladik». Suhbat oxirida — xayr."},
        {"savol": "«Ладно» nimani bildiradi?", "variantlar": ["Yo'q", "Xo'p / mayli", "Bilmayman", "Kutib tur"], "togri": 1, "izoh": "Ладно — rozilik: «xo'p, mayli». Juda ko'p ishlatiladi."},
        {"savol": "«Короче» so'zlashuvda nimani bildiradi?", "variantlar": ["Qisqasi / xullas", "Kaltaroq", "Tezroq", "Ozroq"], "togri": 0, "izoh": "Короче — «xullas, qisqasi». Ruslar gapni shu bilan boshlashni yaxshi ko'radi."},
        {"savol": "«Чуть-чуть» nimani bildiradi?", "variantlar": ["Juda ko'p", "Ozgina", "Tez-tez", "Hech qachon"], "togri": 1, "izoh": "Чуть-чуть — ozgina. Я чуть-чуть говорю по-русски — ruschada ozgina gapiraman."},
        {"savol": "«Спасибо» ga qanday javob beriladi?", "variantlar": ["Привет", "Не за что / Пожалуйста", "Пока", "Давай"], "togri": 1, "izoh": "Не за что — arzimaydi. Пожалуйста ham bo'ladi."},
        {"savol": "«Ну» so'zi nutqda qanday vazifa bajaradi?", "variantlar": ["Savol beradi", "To'ldiruvchi so'z («xo'sh» kabi)", "Inkor qiladi", "Buyruq beradi"], "togri": 1, "izoh": "Ну — слово-паразит: «xo'sh, eee» kabi. Nutqni tabiiy qiladi."},
        {"savol": "«Блин!» undovi nimani bildiradi?", "variantlar": ["Quymoq (taom)", "Attang! / Eh! (yumshoq afsus)", "Salom", "Juda zo'r"], "togri": 1, "izoh": "So'zma-so'z «quymoq», lekin undov sifatida «attang!». Yumshoq, lekin rasmiy joyda ishlatmang."},
    ],
}
