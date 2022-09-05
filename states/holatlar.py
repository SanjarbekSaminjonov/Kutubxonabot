from  aiogram.dispatcher.filters.state import State, StatesGroup

class Holatlar(StatesGroup):
    kutubxona_joylashuv_qabul_qilish_holati = State()
    kitobdokon_joylashuv_qabul_qilish_holati = State()

    adminga_murojaat_holati = State()
    jonatish_holati = State()