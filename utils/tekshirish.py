from typing import Union
from aiogram import Bot

async def check(user_id, kanal:Union[str, int]):
    bot = Bot.get_current()
    azo = await bot.get_chat_member(user_id=user_id, chat_id=kanal)
    return azo.is_chat_member()
