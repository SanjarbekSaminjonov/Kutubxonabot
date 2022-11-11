from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("text", 'url_manzil')

# share_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Do'stlarga ulashish",switch_inline_query="\n\nBot yordamida siz istalgan kitobni sifatli qidirib topishingiz mumkin.\n\nMarhamat botdan foydalaning:\n👉🏻@kutubxonakitoblarbot")
#         ]
#     ]
# )

def share_buttons(url_manzil):
    share = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(
                    text = "Do'stlarga ulashish",
                    url = url_manzil
                )
            ]
        ]
    )

    return share

tekshirish_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Tekshirish', callback_data='tekshirish')
        ]
    ]
)

def alohida_inline(text, url_manzil):
    alohida = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Google maps orqali ko\'rish',
                    url = url_manzil,

                )
            ]
        ]
    )

    return alohida
