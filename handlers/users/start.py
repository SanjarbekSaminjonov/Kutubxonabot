from email import message
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import start_buttons
from aiogram.types import CallbackQuery


from loader import dp, base, bot


@dp.message_handler(CommandStart(),state = '*')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    lname = message.from_user.last_name
    username = message.from_user.username
    tg_id = message.from_user.id
    try:
        base.foydalanuvchi_qoshish(name=name, username=username, tg_id=tg_id, lastname=lname)
    except Exception:
        pass
    await message.answer(f"<b>Assalomu alekum, {message.from_user.full_name}!</b>\n\nKutubxona kanalining rasmiy botiga xush kelibsiz.\n\n/help buyrug'i yordamida nimalarga qodir ekanligimni bilib oling!")
    await message.answer(text="O'zingizni kerakli bo'limni tanglang:", reply_markup=start_buttons)

@dp.callback_query_handler(text='tekshirish')
async def bot_univer(matn: CallbackQuery):
    message_id = matn.message.message_id 

    name = matn.from_user.full_name
    lname = matn.from_user.last_name
    username = matn.from_user.username
    tg_id = matn.from_user.id
    try:
        base.foydalanuvchi_qoshish(name=name, username=username, tg_id=tg_id, lastname=lname)
    except Exception:
        pass    

    await bot.delete_message(chat_id=tg_id,message_id=message_id)
    await matn.message.answer(f"<b>Assalomu alekum! {matn.from_user.full_name}</b>\n\nKutubxona kanalining rasmiy botiga xush kelibsiz.\n\n/help buyrug'i yordamida nimalarga qodir ekanligimni bilib oling!")
    await matn.message.answer(text="O'zingizni kerakli bo'limni tanglang:", reply_markup=start_buttons)


    
