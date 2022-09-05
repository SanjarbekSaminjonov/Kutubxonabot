from aiogram import types

from loader import dp, bot


@dp.message_handler(text="🔹Rivojlanish uchun xissa qo'shish")
async def bot_help(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    text = f"<b>Bot sizga foyda berayotgan bo'lsa men bundan hursandman!</b>\n\n" \
            f"Marhamat sizga foyda berayotgan ushbu botni yanada rivojlanishi uchun xissangizni qo'shing, do'stlaringiz, tanishlarinigizga bot haqida so'zlab bering." \
            f" {user_name} sog'- omon bo'ling, ilm olishdan hech charchamang.\n\n" \
            f"<i>🖋Fikr-mulohazalaringizni <b>Dastur yozuvchisi</b> bo'limida qoldirishingiz mumkin.</i>"
    
    await bot.send_message(chat_id=user_id, text=text)
