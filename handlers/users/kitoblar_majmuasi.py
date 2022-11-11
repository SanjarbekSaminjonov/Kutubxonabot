from aiogram import types
from keyboards.default.buttons import start_buttons, uzbek_buttons, majmua_buttons, jahon_buttons
from keyboards.inline.inline_buttons import share_buttons
from aiogram.dispatcher import FSMContext

from loader import dp, bot, base


@dp.message_handler(text='📚Kitoblar majmuasi')
async def bot_start(message: types.Message):
    await message.answer(text="<b>Yaxshi. Siz Kitoblar majmuasini tanladingiz.</b>\n\nKerakli bo'limni tanlang:  ", reply_markup=majmua_buttons)

@dp.message_handler(text="O'zbek adabiyoti")
async def bot_start(message: types.Message):
    await message.answer(text="Yozuvchini tanlang: ", reply_markup=uzbek_buttons)

uzbek_yozuvchilar = base.select_all_uzbek()
print('*'*10)
print(f'uzbek_yozuvchilari: {uzbek_yozuvchilar}')
print('*'*10)
for uzbek_yozuvchi in uzbek_yozuvchilar: 
    @dp.message_handler(text=f'{uzbek_yozuvchi[1]}')
    async def bot_univer(message: types.Message):
        uzbek_yozuvchi = message.text
        print('*'*10)
        print(uzbek_yozuvchi)
        print('*'*10)
        kitoblar = base.select_uzbek(nomi=uzbek_yozuvchi)[2]
        kitob_items = kitoblar.split(',')
        user_id = message.from_user.id

        for kitob_item in kitob_items:
            manzil = f"{kitob_item.strip()}"
            print(manzil)
            caption = f"Muallif: <b>{uzbek_yozuvchi}</b>\n\n👉🏻@asadbek_muxtorov"
            await bot.send_document(chat_id=user_id, document=manzil,caption=caption, reply_markup=share_buttons(manzil))


@dp.message_handler(text="Jahon adabiyoti")
async def bot_start(message: types.Message):
    await message.answer(text="Yozuvchini tanlang: ", reply_markup=jahon_buttons)

jahon_yozuvchilari = base.select_all_jahon()
for jahon_yozuvchi in jahon_yozuvchilari: 
    @dp.message_handler(text=f'{jahon_yozuvchi[1]}')
    async def bot_univer(message: types.Message):
        jahon_yozuvchi = message.text       
        user_id = message.from_user.id
        kitoblar = base.select_jahon(nomi=jahon_yozuvchi)[2]
        kitob_items = kitoblar.split(',')

        for kitob_item in kitob_items:
            manzil = f"{kitob_item.strip()}"
            print(manzil)
            caption = f"Muallif: <b>{jahon_yozuvchi}</b>\n\n👉🏻@asadbek_muxtorov"
            await bot.send_document(chat_id=user_id, document=manzil,caption=caption, reply_markup=share_buttons)

@dp.message_handler(text='📕Mashhur kitoblar')
async def bot_univer(message: types.Message):
    user_id = message.from_user.id
    kitoblar = base.select_mashhur(id=1)[1]
    kitob_items = kitoblar.split(',')
    for kitob_item in (kitob_items):
        caption = f"Foyda olgan bo'lsangiz xursandmiz.\n\n👉🏻@asadbek_muxtorov"
        manzil = f"{kitob_item.strip()}"
        await bot.send_document(chat_id=user_id, document=manzil,caption=caption, reply_markup=share_buttons)
        




@dp.message_handler(text='🔙Ortga' , state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Yaxshi. Ortga qaytamiz.", reply_markup=start_buttons)

