from aiogram import types
from keyboards.default.buttons import admin_buttons, start_buttons
from loader import dp, base, bot


# Echo bot
@dp.message_handler(commands='admin', chat_id='1603330179')
async def bot_echo(message: types.Message):
    text='<b>Asadbek Muxtorov boshqaruvga xush kelibsiz!</b>'
    await message.answer(text=text, reply_markup=admin_buttons)

@dp.message_handler(commands='count_user')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    count_user = base.count_user()[0]
    if message.from_user.id == 1603330179:
        await bot.send_message(chat_id=user_id, text=f"Foydalanuvchlar soni: {count_user} ta", reply_markup=admin_buttons)
    else:
        await bot.send_message(chat_id=user_id, text=f"Foydalanuvchlar soni: {count_user} ta", reply_markup=start_buttons)
    


@dp.message_handler(commands='list_users', chat_id = '1603330179')
async def bot_echo(message: types.Message):
    text = ''
    user_id = message.from_user.id
    list_users = base.select_users()
    for i in range(len(list_users)):
        text += f"\n<b>{i+1}-user</b>\n" \
                f"<b>Ismi:</b> {list_users[i][1]}\n" \
                f"<b>ID:</b> {list_users[i][3]}\n" \
                f"<b>Username:</b> @{list_users[i][4]}\n" \
                f"{'➖'*10}"
    
    await bot.send_message(chat_id=user_id, text=text, reply_markup=admin_buttons)











