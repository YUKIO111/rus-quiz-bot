# questions.py
# Savollar bazasi. Yangi savol qo'shish uchun shunchaki ro'yxatga yangi dict qo'shing.

QUESTIONS = {
    "lugat": [
        {
            "savol": "«Молоко» so'zining ma'nosi nima?",
            "variantlar": ["Suv", "Sut", "Non", "Choy"],
            "togri": 1,
            "izoh": "Молоко — sut. Talaffuzi: «malako» (urg'usiz «о» — «а» kabi o'qiladi).",
        },
        {
            "savol": "«Книга» so'zining ma'nosi nima?",
            "variantlar": ["Deraza", "Stol", "Kitob", "Eshik"],
            "togri": 2,
            "izoh": "Книга — kitob. Urg'u birinchi bo'g'inda: КНИ́-га.",
        },
        {
            "savol": "«Окно» so'zining ma'nosi nima?",
            "variantlar": ["Deraza", "Devor", "Shift", "Pol"],
            "togri": 0,
            "izoh": "Окно — deraza. Urg'u oxirgi bo'g'inda: ок-НО́, shuning uchun «akno» deb o'qiladi.",
        },
        {
            "savol": "«Говорить» fe'lining ma'nosi nima?",
            "variantlar": ["O'qimoq", "Yozmoq", "Gapirmoq", "Tinglamoq"],
            "togri": 2,
            "izoh": "Говорить — gapirmoq. Bu 2-tuslanish fe'li (-ить bilan tugaydi).",
        },
        {
            "savol": "«Читать» fe'lining ma'nosi nima?",
            "variantlar": ["O'qimoq", "Yugurmoq", "Uxlamoq", "Ichmoq"],
            "togri": 0,
            "izoh": "Читать — o'qimoq. Bu 1-tuslanish fe'li (-ать bilan tugaydi).",
        },
        {
            "savol": "«Talaba» so'zi ruschada qanday aytiladi?",
            "variantlar": ["Учитель", "Студент", "Врач", "Друг"],
            "togri": 1,
            "izoh": "Студент — talaba. «Я студент» — Men talabaman (ruschada «man» qo'shilmaydi).",
        },
        {
            "savol": "«Вода» so'zining ma'nosi nima?",
            "variantlar": ["Suv", "Olov", "Havo", "Tuproq"],
            "togri": 0,
            "izoh": "Вода — suv. Urg'u oxirida: во-ДА́, shuning uchun «vada» deb eshitiladi.",
        },
        {
            "savol": "«Друг» so'zining ma'nosi nima?",
            "variantlar": ["Dushman", "Qo'shni", "Do'st", "Aka"],
            "togri": 2,
            "izoh": "Друг — do'st. So'z oxirida «г» jarangsiz aytiladi: «druk».",
        },
    ],
    "grammatika": [
        {
            "savol": "Rus tilida nechta kelishik bor?",
            "variantlar": ["4 ta", "5 ta", "6 ta", "7 ta"],
            "togri": 2,
            "izoh": "Rus tilida 6 ta kelishik bor: именительный, родительный, дательный, винительный, творительный, предложный.",
        },
        {
            "savol": "«Книга» so'zi qaysi jinsda?",
            "variantlar": ["Мужской (erkak)", "Женский (ayol)", "Средний (o'rta)", "Jinsi yo'q"],
            "togri": 1,
            "izoh": "-а bilan tugagan so'zlar odatda женский род (ayol jinsi): книга, вода, школа.",
        },
        {
            "savol": "«Окно» so'zi qaysi jinsda?",
            "variantlar": ["Мужской", "Женский", "Средний", "Ko'plik"],
            "togri": 2,
            "izoh": "-о/-е bilan tugagan so'zlar средний род (o'rta jins): окно, молоко, море.",
        },
        {
            "savol": "«Говорить» fe'li qaysi tuslanishga kiradi?",
            "variantlar": ["1-tuslanish", "2-tuslanish", "Noto'g'ri fe'l", "Tuslanmaydi"],
            "togri": 1,
            "izoh": "-ить bilan tugagan fe'llar 2-tuslanish: говорить → я говорю, ты говоришь.",
        },
        {
            "savol": "«Я читаю книгу» gapida «книгу» qaysi kelishikda?",
            "variantlar": ["Именительный", "Родительный", "Винительный", "Дательный"],
            "togri": 2,
            "izoh": "Винительный (tushum kelishigi) — nimani o'qiyapman? Книга → книгу (-а → -у).",
        },
        {
            "savol": "«Я студент» gapining to'g'ri tarjimasi qaysi?",
            "variantlar": ["Men talabaman", "U talaba", "Men talaba edim", "Men talaba bo'laman"],
            "togri": 0,
            "izoh": "Hozirgi zamonda «быть» (bo'lmoq) fe'li tushib qoladi: Я студент = Men talabaman.",
        },
        {
            "savol": "Rus tilida nechta jins (род) bor?",
            "variantlar": ["2 ta", "3 ta", "4 ta", "Jins yo'q"],
            "togri": 1,
            "izoh": "3 ta: мужской (erkak), женский (ayol), средний (o'rta).",
        },
    ],
    "talaffuz": [
        {
            "savol": "Urg'usiz «о» harfi odatda qanday o'qiladi?",
            "variantlar": ["«о» kabi", "«а» kabi", "«у» kabi", "O'qilmaydi"],
            "togri": 1,
            "izoh": "Urg'usiz «о» — «а» kabi o'qiladi: молоко → «malako».",
        },
        {
            "savol": "Qaysi undoshlar HAR DOIM qattiq talaffuz qilinadi?",
            "variantlar": ["Б, В, Г", "Ж, Ш, Ц", "Ч, Щ, Й", "Л, М, Н"],
            "togri": 1,
            "izoh": "Ж, Ш, Ц har doim qattiq: жить → «jыt'», keyin и kelsa ham ы kabi o'qiladi.",
        },
        {
            "savol": "«Молоко» so'zi qanday talaffuz qilinadi?",
            "variantlar": ["moloko", "malako", "muluko", "meleko"],
            "togri": 1,
            "izoh": "Urg'u oxirgi bo'g'inda: мо-ло-КО́. Urg'usiz ikkala «о» — «а» bo'lib ketadi: «malako».",
        },
        {
            "savol": "So'z oxiridagi jarangli undoshlar qanday aytiladi?",
            "variantlar": ["Jarangli qoladi", "Jarangsiz aytiladi", "Tushib qoladi", "Cho'ziq aytiladi"],
            "togri": 1,
            "izoh": "So'z oxirida jarangli undoshlar jarangsizlashadi: друг → «druk», хлеб → «xlep».",
        },
        {
            "savol": "«ь» (myagkiy znak) belgisi nima vazifa bajaradi?",
            "variantlar": ["Unlini cho'zadi", "Undoshni yumshatadi", "Urg'uni ko'rsatadi", "Hech narsa"],
            "togri": 1,
            "izoh": "ь — oldingi undoshni yumshatadi: говорить oxiridagi «т'» yumshoq aytiladi.",
        },
        {
            "savol": "Rus tilida urg'u (ударение) qanday?",
            "variantlar": ["Doim oxirgi bo'g'inda", "Doim birinchi bo'g'inda", "Erkin — istalgan bo'g'inda", "Urg'u yo'q"],
            "togri": 2,
            "izoh": "Urg'u erkin va so'z ma'nosini o'zgartirishi mumkin: за́мок (qal'a) — замо́к (qulf).",
        },
    ],
}
