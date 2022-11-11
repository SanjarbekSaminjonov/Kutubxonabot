from aiogram import types
from keyboards.default.buttons import start_buttons, uzbek_buttons, majmua_buttons, jahon_buttons, joylashuv_buttons
from states.holatlar import Holatlar
from aiogram.dispatcher import FSMContext
from loader import dp, bot, base
from data import config
from keyboards.inline.inline_buttons import alohida_inline
import math
import time


import googlemaps


def distance(lat1, lon1, lat2, lon2):
    f1 = lat1 * math.pi/180
    f2 = lat2 * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180
    R = 6371e3
    d = math.acos( math.sin(f1)*math.sin(f2) + math.cos(f1)*math.cos(f2) * math.cos(Δλ) ) * R
    natija = float(format(d / 1000, '.2f'))
    if natija < 1:
        return f"{natija*1000} m"
    
    return  f"{natija} km"

def miles_to_meter(miles):
    try:
        return miles * 1_609.344
    except:
        return 0

def aniqla(lat, lng):
    API_KEY = open('API_KEY.txt', 'r').read()
    map_client = googlemaps.Client(API_KEY)
    location = (float(lat), float(lng))
    search_string = 'kitob do\'koni'
    radius = miles_to_meter(10)

    response = map_client.places_nearby(
        location = location,
        keyword = search_string,
        name = 'kitob do\'koni',
        radius = radius
    )

    kutubxona_data = []
    for i in range(len(response['results'])):
        kutubxona_nomi = response['results'][i]['name']
        kutubxona_place_id = response['results'][i]['place_id']
        kutubxona_location_lat = response['results'][i]['geometry']['location']['lat']
        kutubxona_location_lng = response['results'][i]['geometry']['location']['lng']
        # kutubxona_opening_hours = response['results'][i]['opening_hours']['open_now']
        kutubxona_user_ratings_total = response['results'][i]['user_ratings_total']
        #Place photo
        try:
            kutubxona_reference = response['results'][i]['photos'][0]['photo_reference']
        except Exception:
            kutubxona_reference = None
        kutubxona_data.append({'name':kutubxona_nomi, 
                            'lat':kutubxona_location_lat, 
                            'lng': kutubxona_location_lng,
                            'user_ratings_total' : kutubxona_user_ratings_total,
                            'photo_reference': kutubxona_reference,
                            'place_id': kutubxona_place_id
                            })
    return kutubxona_data 


@dp.message_handler(text="❇️Kitob do'kon manzillari",)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="<b>Yaxshi. Siz kitob do'kon manzillari tanladingiz.</b>\n\nMenga sizning joylashuvingiz kerak: ", reply_markup=joylashuv_buttons)
    await Holatlar.kitobdokon_joylashuv_qabul_qilish_holati.set()

@dp.message_handler(state=Holatlar.kitobdokon_joylashuv_qabul_qilish_holati,  content_types='location')
async def loaction(message: types.Message, state: FSMContext):
    await state.update_data({
        'latitude': message.location.latitude,
        'longitude': message.location.longitude
    })

    joylashuv = await state.get_data()
    user_location_lat = joylashuv.get('latitude')
    user_location_lng = joylashuv.get('longitude')
    user_id = message.from_user.id
    
    kutubxona_items = aniqla(user_location_lat, user_location_lng)
    print('*'*1000)
    print(kutubxona_items)
    await bot.send_message(chat_id=user_id, text='<b>🍳Atrofdagi manzillar qidirilmoqda...</b>')
    await bot.send_message(chat_id=user_id, text='<b>✅Topildi</b>')

    for i in range(len(kutubxona_items)):
        masofa = distance(user_location_lat, user_location_lng, kutubxona_items[i]['lat'], kutubxona_items[i]['lng'])
        data =  f"<b>{i+1}-kitob do\'koni</b>\n\n" \
                f"Kitob dokon nomi: <b>{kutubxona_items[i]['name'].upper()}</b>" \
                f"\nFoydalanuvchilar bahosi: <b>{kutubxona_items[i]['user_ratings_total']}</b>" \
                f"\nMasofa: <b>{masofa}</b>" \
                f"\n\nDasturchi: @asadbek_muxtorov"
        photo_reverense = kutubxona_items[i]['photo_reference']
        url_manzil = f"https://www.google.com/maps/search/?api=1&query={kutubxona_items[i]['lat']}%2C{kutubxona_items[i]['lng']}&query_place_id={kutubxona_items[i]['place_id']}"
        if photo_reverense is not None:
            photo_link = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=300&photo_reference={photo_reverense}&key={config.API_KEY}'

        else:
            photo_link = 'https://t.me/Muxtorov_3Dimage/100'
        
        await bot.send_photo(chat_id=user_id, 
                            photo=photo_link, 
                            caption=data, 
                            reply_markup= alohida_inline(text='assalomu alekum', url_manzil=url_manzil)  
                        )
        
        if i == len(kutubxona_items) - 1:
            await bot.send_message(chat_id=user_id, text='<i>🔗Atrofdagi kitob do\'koni ro\'yhati bilan tanishdingiz.</i>'  )

        time.sleep(2)


    await state.finish()


