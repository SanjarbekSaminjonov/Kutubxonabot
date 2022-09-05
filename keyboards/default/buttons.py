from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import bot, base

start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        # [
        #     KeyboardButton(text="Kitob qidirish")
        # ],
        [
            KeyboardButton(text='📚Kitoblar majmuasi'),
            KeyboardButton(text="📕Mashhur kitoblar"),
        ],
        [
            KeyboardButton(text='❇️Kutubxona manzillari'),
            KeyboardButton(text="❇️Kitob do'kon manzillari"),
        ],
        [
            KeyboardButton(text="🔹Rivojlanish uchun xissa qo'shish"),
            KeyboardButton(text='🔹Dastur yozuvchisi')

        ],
    ],
    resize_keyboard=True
)

majmua_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbek adabiyoti"),
            KeyboardButton(text="Jahon adabiyoti"),
        ],
        [
            KeyboardButton(text='🔙Ortga')
        ]
    ],
    resize_keyboard=True
)


def baza_tugma(yozuvchilar):
    index, i = 0, 0
    keys = []
    for yozuvchi in yozuvchilar:
        yozuvchi_nomi = yozuvchi[1]
        if i % 2 == 0 and i != 0:
            index += 1

        if i % 2 == 0:
            keys.append([KeyboardButton(text=f'{yozuvchi_nomi}')])
        else:
            keys[index].append(KeyboardButton(text=f'{yozuvchi_nomi}'))
        i += 1

    keys.append([KeyboardButton(text='🔙Ortga')])
    return ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)


# UZBEK ADABIYOTI
uzbek_yozuvchilar = base.select_all_uzbek()
uzbek_buttons = baza_tugma(uzbek_yozuvchilar)

# JAHON ADABIYOTI
jahon_yozuvchilar = base.select_all_jahon()
jahon_buttons = baza_tugma(jahon_yozuvchilar)

# KUTUBXONA MANZILLARI
joylashuv_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📍Joylashuv', request_location=True)
        ],
        [
            KeyboardButton(text='🔙Ortga')
        ]
    ],
    resize_keyboard=True
)

# MUROJAAT BUTTONS
murojaat_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Murojaat yo'llash")
        ],
        [
            KeyboardButton(text='🔙Ortga')
        ]
    ],
    resize_keyboard=True
)

jonatish_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha, jo'natilsin"),
            KeyboardButton(text="Yo'q, jo'natilmasin")
        ]
    ],
    resize_keyboard=True
)

ortga_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙Ortga')
        ]
    ],
    resize_keyboard=True
)

# ADMIN BOSHQARUVI UCHUN
admin_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/count_user'),
            KeyboardButton(text='/list_users'),
        ],
        [
            KeyboardButton(text='/reklama'),
        ]
    ],
    resize_keyboard=True

)
