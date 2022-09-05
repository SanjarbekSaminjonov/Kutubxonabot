from aiogram import types
from keyboards.default.buttons import murojaat_buttons , jonatish_buttons, ortga_buttons

from loader import dp, bot
from states.holatlar import Holatlar
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="🔹Dastur yozuvchisi")
async def bot_help(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    text = f"Dastur yozuvchi: <b>Asadbek Muxtorov</b>\n" \
            f"Lavozimi: <b>Farg'ona davlat universiteti Amaliy matematika yo'nalishi 3-bosqich talabasi. Marg'ilon Raqamli texnalogiyalari markazi Python kursi o'quvchisi.</b>\n\n" \
            f"<b>Telegram:</b> @asadbek_muxtorov\n<b>Github:</b> <a href='https://github.com/bekmuxtorov'>@bekmuxtorov</a>\n<b>Sayt:</b> <a href='https://bekmuxtorov.netlify.app'>bekmuxtorov.uz</a>" 

    await bot.send_message(chat_id=user_id, text=text, reply_markup=murojaat_buttons)
    
@dp.message_handler(text="Murojaat yo'llash")
async def bot_help(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Marhamat murojaatingizni yo'llang:")
    await Holatlar.adminga_murojaat_holati.set()

@dp.message_handler(state=Holatlar.adminga_murojaat_holati)
async def bot_help(message: types.Message, state: FSMContext):
    matn = message.text
    user_id = message.from_user.id
    await state.update_data({'matn':matn})
    malumot = await state.get_data()
    send_message = malumot.get('matn')
    
    await bot.send_message(chat_id=user_id, text=send_message)
    await bot.send_message(chat_id=user_id, text="<b>Barchasi to'g'rimi,\nAdminga jo'natilsinmi?</b>", reply_markup=jonatish_buttons)

                    
    await Holatlar.jonatish_holati.set()

@dp.message_handler(text="Ha, jo'natilsin", state=Holatlar.jonatish_holati)
async def bot_help(message: types.Message, state: FSMContext):
    malumot = await state.get_data()
    send_message = malumot.get('matn')
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    user_name = message.from_user.username

    malumot = await state.get_data()
    send_message = f"Ismi: {full_name}" \
                    f"User ID: {user_id}" \
                    f"Username: {user_name}" \
                    f"{malumot.get('matn')}"

    await bot.send_message(chat_id='1603330179', text=send_message)
    await state.finish()
    await bot.send_message(chat_id=user_id, text='<b>✔Murojjat muaffaqiyatli jo\'natildi, Tez orada javob qaytariladi.</b>', reply_markup=ortga_buttons)
    

@dp.message_handler(text="Yo'q, jo'natilmasin", state=Holatlar.jonatish_holati)
async def bot_help(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.finish()
    await bot.send_message(chat_id=user_id, text='<b>✔Murojjat bekor qilindi.</b>', reply_markup=ortga_buttons)
    
                    