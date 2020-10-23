from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton


def start(update, context):
    name=update.message.chat.first_name
    text=f'👋assalomu alekum {name} kompyuter extiyot qisimlari va 🖥kompyuterlar buyurtma qiling!!!(unutmang eng yaxshi va hamyonbop maxsulotlarni bizning botdan topasiz 😊)'
    update.message.reply_text(text)
    button=ReplyKeyboardMarkup([['🖥stol kompyuter🖥','💻noutbook💻'],['🖨printer🖨','🕹aksesuarlar🕹'],['💾kompyuter qisimlari💾'],['🙎‍♂️admin','🚗yetkazib berish']],resize_keyboard=True)  
    text2='O\'zingizga kerakli kategoriyani tanlang.'
    update.message.reply_text(text2,reply_markup=button)
def pc(update, context):
    text=update.message.text
    button=InlineKeyboardButton('ofice uchun', switch_inline_query_current_chat='pcofice')
    button2=InlineKeyboardButton('o\'yin uchun', switch_inline_query_current_chat='pco\'yin')
    reply_markup=InlineKeyboardMarkup([
        [button,button2]
    ])
    update.message.reply_text(text, reply_markup=reply_markup)

def pcofice(update,context):
    text='ram: 2gb \nvga: intelHdgraphic \nhdd: 500\ncpu: intel celeron 1\.80 Ghz'
    text1='ram: 4gb \nvga: NVIDA GEFORCE GT720 1gb \nhdd: 1TB\ncpu:intel core i3 2\.80 Ghz'
    of='https://image.shutterstock.com/image-photo/desctop-computer-on-wooden-desk-260nw-1170846982.jpg'
    of1='http://1.bp.blogspot.com/_zVkfb2MIt4A/Sw4AuwRlQGI/AAAAAAAAAgw/6WuEuJF2qUc/s1600/Lenovo+A58+Desktop+Computer.jpg'
    o1=InputTextMessageContent(
        message_text=f'[samsung]({of1}) {text1}',
        parse_mode='MarkdownV2'
    )
    o=InputTextMessageContent(
        message_text=f'[avtech]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='avtech',
        input_message_content=o,
        thumb_url=of,
        description='$250.99',
        hide_url=True,
        id=1
    )
    result2=InlineQueryResultArticle(
        title='samsung',
        input_message_content=o1,
        thumb_url=of1,
        description='$350.99',
        hide_url=True,
        id=2
    )
    result=[result1,result2]
    update.inline_query.answer(result)
def pcoyin(update,context):
    text='ram: 8gb \nvga: amd Radeon RX 5000 series \nhdd: 1TB\nSSD: 250GB\ncpu: 3rd Gen AMD Ryzen™ Processor 3\.80 Ghz'
    text1='ram: 16gb \nvga: NVIDA GEFORCE RTX 3070 6gb \n hdd: 2TB \nSSD: 500GB \ncpu: intel core i7 3\.60 Ghz'
    of='https://m.media-amazon.com/images/I/51JCfx4F+8L.jpg'
    of1='https://sc02.alicdn.com/kf/UTB8Ge8_FWrFXKJk43Ovq6ybnpXaw.jpg'
    o1=InputTextMessageContent(
        message_text=f'[Gaming pc]({of1}) {text1}',
        parse_mode='MarkdownV2'
    )
    o=InputTextMessageContent(
        message_text=f'[GAMING PC]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='GAMING DESKTOP',
        input_message_content=o,
        thumb_url=of,
        description='$800.99',
        hide_url=True,
        id=1
    )
    result2=InlineQueryResultArticle(
        title='GAMING PC',
        input_message_content=o1,
        thumb_url=of1,
        description='$900.99',
        hide_url=True,
        id=2
    )
    result=[result1,result2]
    update.inline_query.answer(result)

def laptop(update, context):
    text=update.message.text
    button=InlineKeyboardButton('ofice uchun', switch_inline_query_current_chat='laptopofice')
    button2=InlineKeyboardButton('o\'yin uchun', switch_inline_query_current_chat='laptopo\'yin')
    reply_markup=InlineKeyboardMarkup([
        [button,button2]
    ])
    update.message.reply_text(text, reply_markup=reply_markup)
def lpcofice(update,context):
    text='ram: 4GB \nvga: intelHdgraphic \nhdd: 500\ncpu: Intel Celeron N4000'
    text1='ram: 4GB \nvga: Intel HD Graphics 500 \nhdd: 1TB\ncpu: Intel Dual\-Core Celeron N3350 up to 2\.4GHz'
    of='https://images-na.ssl-images-amazon.com/images/I/71idFa2cEuL._AC_SL1500_.jpg'
    of1='https://images-na.ssl-images-amazon.com/images/I/81ZT2avFJ3L._AC_SL1500_.jpg'
    o1=InputTextMessageContent(
        message_text=f'[ASUS]({of1}) {text1}',
        parse_mode='MarkdownV2'
    )
    o=InputTextMessageContent(
        message_text=f'[HP]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='HP',
        input_message_content=o,
        thumb_url=of,
        description='$250.99',
        hide_url=True,
        id=1
    )
    result2=InlineQueryResultArticle(
        title='ASUS',
        input_message_content=o1,
        thumb_url=of1,
        description='$350.99',
        hide_url=True,
        id=2
    )
    result=[result1,result2]
    update.inline_query.answer(result)
def lpcoyin(update,context):
    text='ram: 16gb \nvga: NVIDIA GeForce GTX 1650 \nhdd: 1TB\nSSD: 512GB\ncpu: Intel Hexa\-Core i7\-9750H Up to 4\.5GHz'
    text1='ram: 8gb \nvga: NVIDIA GeForce GTX 1650 \n hdd: 2TB \nSSD: 256GB NVMe \ncpu: 9th Gen Intel Core i5\-9300H'
    of='https://images-na.ssl-images-amazon.com/images/I/51uMBnr431L._AC_SL1000_.jpg'
    of1='https://images-na.ssl-images-amazon.com/images/I/71s1LRpaprL._AC_SL1500_.jpg'
    o1=InputTextMessageContent(
        message_text=f'[Acer Nitro 5 Gaming Laptop]({of1}) {text1}',
        parse_mode='MarkdownV2'
    )
    o=InputTextMessageContent(
        message_text=f'[2019 ASUS ROG]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='2019 ASUS ROG',
        input_message_content=o,
        thumb_url=of,
        description='$1\.100.99',
        hide_url=True,
        id=1
    )
    result2=InlineQueryResultArticle(
        title='Acer Nitro 5 Gaming Laptop',
        input_message_content=o1,
        thumb_url=of1,
        description='$975.19',
        hide_url=True,
        id=2
    )
    result=[result1,result2]
    update.inline_query.answer(result)
def printer(update, context):
    text=update.message.text
    button=InlineKeyboardButton('Epson', switch_inline_query_current_chat='Epson')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    update.message.reply_text(text, reply_markup=reply_markup)
def epson(update,context):
    text='nomi: Epson WorkForce ET\-3750 \n printer \nscaner \n nusxalash '
    of='https://images-na.ssl-images-amazon.com/images/I/81yfQjv7PZL._AC_SL1500_.jpg'
    o=InputTextMessageContent(
        message_text=f'[Epson ET\-3750]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='Epson ET\-3750',
        input_message_content=o,
        thumb_url=of,
        description='$530.99',
        hide_url=True,
        id=1
    )
    result=[result1]
    update.inline_query.answer(result)

def akses(update, context):
    text=update.message.text
    button=InlineKeyboardButton('web kamera', switch_inline_query_current_chat='web kamera')
    button2=InlineKeyboardButton('naushnik', switch_inline_query_current_chat='naushnik')
    reply_markup=InlineKeyboardMarkup([
        [button,button2]
    ])
    update.message.reply_text(text, reply_markup=reply_markup)
def kamera(update,context):
    text='nomi: Logitech C920x Pro HD Webcam \nseries: C920X \nvideo: 720p'
    of='https://images-na.ssl-images-amazon.com/images/I/71iNwni9TsL._AC_SL1500_.jpg'    
    o=InputTextMessageContent(
        message_text=f'[logitech]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='logitech',
        input_message_content=o,
        thumb_url=of,
        description='$130.99',
        hide_url=True,
        id=1
    )
    result=[result1]
    update.inline_query.answer(result)
def naushnik(update,context):
    text='nomi: Sony L600 Wireless  \nseries: L600 \nrangi: qora'
    of='https://images-na.ssl-images-amazon.com/images/I/71MOz5-k2nL._AC_SL1500_.jpg'    
    o=InputTextMessageContent(
        message_text=f'[Sony]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='Sony',
        input_message_content=o,
        thumb_url=of,
        description='$240.99',
        hide_url=True,
        id=1
    )
    
    result=[result1]
    update.inline_query.answer(result)
def qism(update, context):
    text=update.message.text
    button=InlineKeyboardButton('blok pitaniya', switch_inline_query_current_chat='blok pitaniya')
    button2=InlineKeyboardButton('qatiq disk', switch_inline_query_current_chat='qatiq disk')
    reply_markup=InlineKeyboardMarkup([
        [button],[button2]
    ])
    update.message.reply_text(text, reply_markup=reply_markup)
def blok(update,context):
    text='nomi: HUNTKEY  \nБлок питания HUNTKEY 550w Green Power'
    of='https://apollo-olx.cdnvideo.ru/v1/files/5mpfutimsoyd-UZ/image;s=1000x700'    
    o=InputTextMessageContent(
        message_text=f'[Block pitaniya]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='Block pitaniya',
        input_message_content=o,
        thumb_url=of,
        description='$30.99',
        hide_url=True,
        id=1
    )
    
    result=[result1]
    update.inline_query.answer(result)
def hdd(update,context):
    text='nomi:Seagate \nhajmi: 3TB \nSATA 6Gb/s'
    of='https://images-na.ssl-images-amazon.com/images/I/71%2BrT7TY2DL._AC_SL1500_.jpg'    
    o=InputTextMessageContent(
        message_text=f'[HDD]({of}) {text}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='HDD',
        input_message_content=o,
        thumb_url=of,
        description='$100.99',
        hide_url=True,
        id=1
    )
    
    result=[result1]
    update.inline_query.answer(result)
def zakaz(update, context):
    text='zakaz qilish uchun pastdagi 👉admin👈  tugamasini bosing'
    button=InlineKeyboardButton(text='👉admin👈 ',url='https://t.me/JHON_uk')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    update.message.reply_text(text, reply_markup=reply_markup)
def dastavka(update,context):
    text2='🏣O\'z hududingizni tanlang'
    button=ReplyKeyboardMarkup([['☎️Kontakt','💶Bizning narxlarimiz'],['🏢1. Filial (Savatchi-1)','🏢2. Filial (Glinka)'],['🏢3. Filial (Malika)','🏢4. Filial (Chilonzor)'],['🏣 Hududiy filiallar'],['⬅️ orqaga qaytish']],resize_keyboard=True)  
    update.message.reply_text(text2,reply_markup=button)
def kontakt(update,context):
    text='FARGO Parcel Service\nOffice Bosh ofis:\n📱 71 200 00 37\n📱 71 207 20 30\n📧 info@fargo.uz\n🌐www.fargo.uz'
    update.message.reply_text(text)
def narx(update,context):
    text='1. 🏣 "FARGO nuqtasidan 🏣 FARGO nuqtasigacha"\n (5000 so\'m  1 kg gacha)\n2. 🏣 "FARGO punktidan 🚪 qabul qiluvchi eshigigacha":\n (25000 so\'m 1 kg gacha)\n3. 🚪 "Yuboruvchining eshigidan - FARGO nuqtasigacha"\n (25000 so\'m 1 kg gacha)\n4. 🚪 "Eshikdan 🚪 eshikgacha" (FARGO vakolatxonalari joylashgan barcha shahar va viloyatlarda):\n (30 000 so\'m 1 kg gacha)\n5. 🌆 "Shahar atrofida"\n (20 000 so\'m 3 kg gacha)'
    update.message.reply_text(text)
def filial1(update,context):
    text='Bosh ofis\n🏣 Sergeli tumani, Savatchi ko\'chasi, 1-uy\n📱 71 207 20 30\n📍Joylashuv:\n📍https://goo.gl/maps/d6JnvAUzcoFGdnMq6'
    update.message.reply_text(text)
def filial2(update,context):
    text='Yakkasaroy filiali\n🏣 Yakkasaroy tumani, st. Kichik Beshogoch, 70-uy\n📱 71 200 00 37\n📍Joylashuv:\n📍https://g.page/fargo-uz?share'
    update.message.reply_text(text)
def filial3(update,context):
    text='Shayxontoxur filiali\n🏣 Shayxontoxur tumani, Kichik xalqa yuli 57, A12 do\'kon\n📱 +998 71 200 00 37\n📱 +998 95 198 41 14\n📍Joylashuv:\n📍https://yandex.uz/maps/-/CCQhbJdVOB'
    photo='AgACAgIAAxkBAAIELl-RbGNb9wN_F0MLVB4F4P905SUOAAKmrjEbmI2JSEh5m_WD0XMm0IZGli4AAwEAAwIAA20AAzBiAwABGwQ'
    update.message.reply_photo(photo,caption=text)
def filial4(update,context):
    text='Chilonzor filiali\n🏣 Uchtetinskiy tumani, Chilonzor massivi, 21A 12-kvartal\n📱 + 998 71 200 00 37\n📱 + 998 71 207 20 20\n📍Joylashuv:\n📍https://maps.google.com/maps?q=41.285871,69.186257&ll=41.285871,69.186257&z=16'
    photo='AgACAgIAAxkBAAIETl-RbvJYZOQq-SoR0zfD0kIkt6FfAAKsrjEbmI2JSIvJj1smiFEHuolGli4AAwEAAwIAA20AA4JuAwABGwQ'
    update.message.reply_photo(photo,caption=text)
def filialhudud(update,context):
    text2='🏣O\'z hududingizni tanlang'
    button=ReplyKeyboardMarkup([['🏢Namangan','🏢Andijon'],['🏢Farg\'ona','🏢Qo\'qon'],['🏢Angren','🏢Samarqand'],['🏢Buxoro','🏢Jizzax'],['🏢Guliston','🏢Navoiy'],['🏢Xorazm','🏢Nukus'],['🏢Surxondaryo','🏢Qarshi'],['🏢Chirchiq'],['⬅️ bosh menyuga qaytish']],resize_keyboard=True)  
    update.message.reply_text(text2,reply_markup=button)
def boshmenyu(update,context):
    text='Bosh menyuga qaytingiz!!!'
    button=ReplyKeyboardMarkup([['🖥stol kompyuter🖥','💻noutbook💻'],['🖨printer🖨','🕹aksesuarlar🕹'],['💾kompyuter qisimlari💾'],['🙎‍♂️admin','🚗yetkazib berish']],resize_keyboard=True)  
    update.message.reply_text(text,reply_markup=button)

def namangan(update,context):
    text='🏤 Filialni tanlang'
    button=ReplyKeyboardMarkup([['Namangan shaxri'],['Kosonsoy'],['⬅️ ortga qaytish']],resize_keyboard=True)
    update.message.reply_text(text,reply_markup=button)
def namangan1(update,context):
    text='Namangan filiali\n🏣 Namangan ko\'chasi A. Navoiy, 47, kv. 3\n📱 +998 93 400 48 08\n🚩 Belgilangan joy: "Shodlik" supermarketi\n📍 Manzil:\nhttps://goo.gl/maps/eeYeVKSPqkQ37wuC7'
    photo='AgACAgIAAxkBAAIEiV-RgqPIzm7OPSVZHsGb4DoppuA8AALZrjEbmI2JSFEbASTCFGbSXWUWmC4AAwEAAwIAA20AA7cbAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def kosonsoy(update,context):
    text='Kosonsoy filiali\n🏣 Kosonsoy, st. Navoiy (4-ofis)\n📱 +998946606053\n📱 +998712000037\n🚩 Belgilangan joy: "MURODIM BIZNES MARKAZI (KOSONSOYLIKLAR OFFIS) yonida\n📍https://maps.google.com/maps?q=41.25485'
    photo='AgACAgIAAxkBAAIEq1-Rg2JY9logDiirT5f0ezFV5v9eAALbrjEbmI2JSDA-Hknie-t9WwFFli4AAwEAAwIAA20AA3BpAwABGwQ'
    update.message.reply_photo(photo,caption=text)
def andijon(update,context):
    text='Andijon filiali\🏣 Andijon shahri, O\'zbekiston ko\'chasi, 95-bino,\ndiqqatga sazovor joy: Dynamosport do\'koni biznes markazi\n📱 +998 94 660 60 51\n📍 Manzil:\nhttps://goo.gl/maps/bPCE8rAzR8RpsBXs7'
    photo='AgACAgIAAxkBAAIEw1-RiO5KYhP1ZA776oc6F8LMSLf0AALhrjEbmI2JSP-z85wYXWgBzggglS4AAwEAAwIAA20AA6yoBQABGwQ'
    update.message.reply_photo(photo,caption=text)
def fargona(update,context):
    text='Farg\'ona filiali\n🏣 Farg\'ona shahri, st. Koraniyoziy uy-20\n📱 +998 94 660 60 52\n🚩 Belgilangan joy: "Uz Invest Avto Sug\'urta" yaqinida, hayvonot bog\'i, Farg\'ona muzeyi\n📍 Manzil:\nhttps://goo.gl/maps/CQUc39krp6Rpo9pj7'
    photo='AgACAgIAAxkBAAIEzV-RiXVUtXAkHzBlK7qa6LiYd1VhAALirjEbmI2JSHc0qJY-dF_MH-8XmC4AAwEAAwIAA20AA5YWAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def qoqon(update,context):
    text='Qo\'qon filiali\n🏣 Kukand shahri, Sarboz ko\'chasi 1, 1-bino, 2-kvartira\n📱 +998 94 660 60 11\n🚩 Belgilangan joy:\n📍 Manzil: "Anor" kafesi\nhttps://maps.google.com/maps?q=40.536720,70.941840&ll=40.536720,70.941840&z=16'
    photo='AgACAgIAAxkBAAIE0F-RivOhwe18YSBEp0wgDweZ9IQyAALjrjEbmI2JSGO9Tu6k1cJWS2gYlS4AAwEAAwIAA20AAxirBQABGwQ'
    update.message.reply_photo(photo,caption=text)
def angren(update,context):
    text='Angren filiali\n🏣 Angren shahri, 2/2 tuman, 7-bino\n📱 +998 93 969 03 03\n📱 +998 93 388 90 04\n🚩 Belgilangan joy: "KAPITAL SUG\'URTA"\n📍https://goo.gl/maps/hx9JzSULCBRh5LY49'
    photo='AgACAgIAAxkBAAIE01-Ri9aFCN6vRoOVAVOGyCN6VldmAALkrjEbmI2JSDV3KxqQ4sxmOsYOmC4AAwEAAwIAA20AAxYZAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def samarqand(update,context):
    text='Samarqand filiali\n🏣 Samarqand, st. Mir Sayyid Barak 32-bino.\n📱 +998 93 720 47 48\n 🚩 Malumot: "Samarkand Dream" mehmonxonasi.\n📍 Manzil:\nhttps://g.page/Fargosamarqand?share'
    photo='AgACAgIAAxkBAAIE1l-RjhlBE-hjgnnXVvSOCAvkQHn0AALqrjEbmI2JSDe2bconG0JxfqFMli4AAwEAAwIAA20AAwdoAwABGwQ'
    update.message.reply_photo(photo,caption=text)
def buxoro(update,context):
    text='🏤 Filialni tanlang'
    button=ReplyKeyboardMarkup([['Buxoro.'],['G\'ijduvon'],['⬅️ ortga qaytish']],resize_keyboard=True)
    update.message.reply_text(text,reply_markup=button)
def buxoro1(update,context):
    text='Buxoro filiali\n🏣g Buxoro, st. B Naqshbandiy, 153-bino\n📱 +998 93 960 60 97\n🚩Mo\'ljal: "SEZAM" restorani\n📍 Manzil:\nhttps://maps.google.com/maps?q=39.770821,64.447733&ll=39.770821,64.447733&z=16'
    photo='AgACAgIAAxkBAAIE41-Rn3lHDl1fVyDarDygiecAAd_dFgACE68xG5iNiUh8q38tTdYGgj5nFpguAAMBAAMCAANtAAOyFQIAARsE'
    update.message.reply_photo(photo,caption=text)
def gijduvon(update,context):
    text='G\'ijduvon filiali\n g.G\'ijduvon ko\'chasi Yusuf Hamadoniy Kuchasi\n📱 +998 94 660 60 62\n🚩 Mo\'ljal: "Bek" restorani\n📍Manzil:https://maps.google.com/maps?q=40.095579,64.682081&ll=40.095579,64.682081&z=16'
    photo='AgACAgIAAxkBAAIE5F-RpS3r3cPCLtL8v0ozRDJ-RaKxAAKDrjEbmKiJSGM3ohRemtwlJW5Ali4AAwEAAwIAA20AAyZrAwABGwQ'
    update.message.reply_photo(photo,caption=text)
def jizzax(update,context):
    text='Джизакский филиал\n🏣 г.Джизак,  ул Узбекистан Ц2а \n📱 +998 71 200 00 37 \n📱 +998 93 940 60 46 \n📍Manzil:\nhttps://goo.gl/maps/85eeSSCFkJ7pfRnj7'
    photo='AgACAgIAAxkBAAIE_l-RvsRqMzyXTGKyN_UNcLXd16GjAAI4rzEbmI2JSCxG6Ax6Xw3pnA3kly4AAwEAAwIAA20AA8ofAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def guliston(update,context):
    text='Guliston filiali\n🏣 Guliston, st. A.Navoiy, 14-bino\n📱 +998 71 200 00 37\n📱 +998 94 660 60 54\n🚩 Mo\'ljal: "DINAMO" sport majmuasiga qarshi\n📍 Manzil:\nhttps://goo.gl/maps/4zjBRSqLvJXL7Mnt5'
    photo='AgACAgIAAxkBAAIFAV-Rv0yLV2d1IzT1fjEGxJ9OZoFSAAI6rzEbmI2JSBz5yoSzginTMoFrly4AAwEAAwIAA20AA2MvAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def navoiy(update,context):
    text='🏤 Filialni tanlang'
    button=ReplyKeyboardMarkup([['Navoiy.'],['Zarafshon'],['Uchquduq'],['⬅️ ortga qaytish']],resize_keyboard=True)
    update.message.reply_text(text,reply_markup=button)
def navoiy1(update,context):
    text='Navoiy viloyati\n🏣 Navoiy, st. O\'zbekiston, 14-uy\n📱 + 998 94 660 60 74\n📱 + 998 71 200 00 37\n📍https://goo.gl/maps/TrfVy15Mn6k1LmPg6'
    photo='AgACAgIAAxkBAAIFAV-Rv0yLV2d1IzT1fjEGxJ9OZoFSAAI6rzEbmI2JSBz5yoSzginTMoFrly4AAwEAAwIAA20AA2MvAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def zarafshon(update,context):
    text='Zarafshon filiali\n🏣 Zarafshon shahri, 3-mikrorayon, 17 A 5\n📱 +998 93 950 05 33\n🚩Mo\'ljal: "Gribok" restorani\n📍Manzil:\nhttps://goo.gl/maps/dQ23kyXskxkmSPRSA'
    photo='AgACAgIAAxkBAAIFA1-RxC7kaQh9OjyxM4vEheEK9OnBAAJfrzEbmI2JSAuJRXlWJunlq4dGli4AAwEAAwIAA20AAxxnAwABGwQ'
    update.message.reply_photo(photo,caption=text)
def uchquduq(update,context):
    text='Uchquduq filiali\n🏣 Uchquduq shahri, Istiqlol 3-blok\n📱 +998 94 660 60 34\n📱 +998 71 200 00 37\n📍 Manzil:\nhttps://maps.google.com/maps?q=42.153156,63.574609&ll=42.153156,63.574609&z=16'
    photo='AgACAgIAAxkBAAIFAl-RxA-4uXG0b0zBjfqyfYy8M2suAAJVrzEbmI2JSG2uIx6mN_eOe-sXmC4AAwEAAwIAA20AA8UYAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def xorazm(update,context):
    text='Xorazm filiali\n🏣 Urganch shahri, Al-Xorazmiy ko\'chasi, 83/2\n📱 +998 94 230 47 48\n 🚩 Mo\'ljal: "ZHAVOHHIR FURNITURE" do\'koniga yoki "BIOKIMYO" binosiga qarshi\n📍Manzil:\nhttps://goo.gl/maps/TgVJWKijHwG6h9V96'
    photo='AgACAgIAAxkBAAIFU1-RxW9G_FyOuGVUqrCSO2fn02WQAAJjrzEbmI2JSL2x8RLYPZobHcQOmC4AAwEAAwIAA20AAx8hAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def nukus(update,context):
    text='Nukus filiali\n🏣 Nukus, st. A.Dosnazarova, 72-uy\n📱 +998 94 900 48 47\n📍https://goo.gl/maps/RC5ucDJ6pd8vjqc6A'
    photo='AgACAgIAAxkBAAIFVF-RxXXj_X8IhMQ_5BVpFI1TJBOIAAJkrzEbmI2JSLH1C-wpGym2i65sli4AAwEAAwIAA20AA9n5AgABGwQ'
    update.message.reply_photo(photo,caption=text)
def surxandaryo(update,context):
    text='🏤 Filialni tanlang'
    button=ReplyKeyboardMarkup([['Termiz'],['Denov'],['⬅️ ortga qaytish']],resize_keyboard=True)
    update.message.reply_text(text,reply_markup=button)
def termiz(update,context):
    text='Termiz filiali\n🏣 Termiz shahri, at-Termiziy ko\'chasi, 2-bino\n📱 +998 93 526 26 16\n🚩 Mo\'ljal: "Surhon hotel" ga qarshi\n📍 Manzil:https://goo.gl/maps/Jx3yWcy89u1654eq8'
    photo='AgACAgIAAxkBAAIFfV-RzBhQNl_w9iNDdnlE4mJyOwaAAAJrrzEbmI2JSPbdsr2A9eaMd59pli4AAwEAAwIAA20AA2P-AgABGwQ'
    update.message.reply_photo(photo,caption=text)
def denov(update,context):
    text='Denov filiali\ng Denov st. Sharof Rashidov 243-bino\n📱 +998 94 660 60 25\n🚩 Mo\'ljal: Uzbegim kafesi\n📍 Manzil:\nhttps://goo.gl/maps/kU5USJHnmriUG6i18'
    photo='AgACAgIAAxkBAAIFfl-RzBzR4cH-RI3td1UvM63pfG0LAAJsrzEbmI2JSJziplI4YszkCxVwly4AAwEAAwIAA20AAz8xAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def qarshi(update,context):
    text='Qarshi filiali\n🏣 Qarshi shahri, O\'zbekiston ko\'chasi, 219-bino\n📱 +998 93 900 48 47\n🚩Mo\'ljal: "Oltin Xurozcha" restorani\n📍Manzil:\nhttps://goo.gl/maps/JPVzdJQrGB6UhNKa6'
    photo='AgACAgIAAxkBAAIFf1-RzGv9uxpB6kVPXIrUdJoX514eAAJtrzEbmI2JSOTI8i5pKvU3-wmfli4AAwEAAwIAA20AAxv7AgABGwQ'
    update.message.reply_photo(photo,caption=text)
def chirchiq(update,context):
    text='Chirchiq filiali\n🏣 Chirchiq shahri, Arancha ko\'chasi Tiklanish 107 bino\n📱 +998 97 444 60 65\n🚩 Mo\'ljal: "Qaldirg\'och" do\'koni\n📍Manzil:\nhttps://goo.gl/maps/XRKdxkDkWYcZ25cW8'
    photo='AgACAgIAAxkBAAIFgl-RzRroRlMTVSlLCNWgV8LonSyiAAJvrzEbmI2JSKZ6T8UJgwsY-uAUmC4AAwEAAwIAA20AA_YgAgABGwQ'
    update.message.reply_photo(photo,caption=text)
def idg(update,context):
    photo=update.message.photo[0]
    print(photo)

updater = Updater('1116012218:AAHXOvZDGx3mUOBIaCD7B83r7v4eJevk8GQ')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, idg))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🖥stol kompyuter🖥'), pc))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🖨printer🖨'), printer))
updater.dispatcher.add_handler(MessageHandler(Filters.text('💻noutbook💻'), laptop))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🕹aksesuarlar🕹'), akses))
updater.dispatcher.add_handler(MessageHandler(Filters.text('💾kompyuter qisimlari💾'), qism))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🙎‍♂️admin'), zakaz))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🚗yetkazib berish'), dastavka))
updater.dispatcher.add_handler(MessageHandler(Filters.text('☎️Kontakt'), kontakt))
updater.dispatcher.add_handler(MessageHandler(Filters.text('💶Bizning narxlarimiz'), narx))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢1. Filial (Savatchi-1)'), filial1))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢2. Filial (Glinka)'), filial2))
updater.dispatcher.add_handler(MessageHandler(Filters.text('⬅️ bosh menyuga qaytish'), boshmenyu))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢3. Filial (Malika)'), filial3))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢4. Filial (Chilonzor)'), filial4))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏣 Hududiy filiallar'), filialhudud))

updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Namangan'), namangan))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Namangan shaxri'), namangan1))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Kosonsoy'), kosonsoy))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Andijon'), andijon))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Farg\'ona'), fargona))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Qo\'qon'), qoqon))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Angren'), angren))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Samarqand'), samarqand))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Buxoro'), buxoro))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Buxoro.'), buxoro1))
updater.dispatcher.add_handler(MessageHandler(Filters.text('G\'ijduvon.'), gijduvon))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Jizzax'), jizzax))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Guliston'), guliston))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Navoiy'), navoiy))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Navoiy.'), navoiy1))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Zarafshon'), zarafshon))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Uchquduq'), uchquduq))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Xorazm'), xorazm))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Nukus'), nukus))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Surxondaryo'), surxandaryo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Termiz'), termiz))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Denov'), denov))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Qarshi'), qarshi))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏢Chirchiq'), chirchiq))
updater.dispatcher.add_handler(MessageHandler(Filters.text('⬅️ ortga qaytish'), filialhudud))

updater.dispatcher.add_handler(InlineQueryHandler(pcofice, pattern='pcofice'))
updater.dispatcher.add_handler(InlineQueryHandler(pcoyin, pattern='pco\'yin'))
updater.dispatcher.add_handler(InlineQueryHandler(lpcofice, pattern='laptopofice'))
updater.dispatcher.add_handler(InlineQueryHandler(lpcoyin, pattern='laptopo\'yin'))
updater.dispatcher.add_handler(InlineQueryHandler(epson, pattern='Epson'))
updater.dispatcher.add_handler(InlineQueryHandler(kamera, pattern='web kamera'))
updater.dispatcher.add_handler(InlineQueryHandler(naushnik, pattern='naushnik'))
updater.dispatcher.add_handler(InlineQueryHandler(blok, pattern='blok pitaniya'))
updater.dispatcher.add_handler(InlineQueryHandler(hdd, pattern='qatiq disk'))
updater.start_polling()
updater.idle()
