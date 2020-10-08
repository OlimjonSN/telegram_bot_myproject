import requests
import random
import telegram
bot=telegram.Bot(token='1190968624:AAHSBci771kMSzJDgrJwiF4k9Dxrlp3KWwo')
def getUpdats():
    update=bot.getUpdates()[-1]
    newid=update.update_id
    txt=update.message.text
    chat_id=update.message.chat.id
    name=update.message.chat.first_name
    return newid,txt,chat_id,name
def sendMessage(chat_id,text):
    button=telegram.replymarkup.ReplyMarkup([["Tug'ilgan kun"],["8-mart"],["Navro'z"],["Hayit bayrami"],["Yangi yil"],["14-yanvar"]],resize_keyboard=True)
    bot.sendMessage(chat_id,text,reply_markup=button)
def sendphoto(chat_id,photo):
    bot.sendphoto(chat_id,photo=photo)
oldid=-1
while True:
    newid,chat_id,text,name=getUpdats()
    if text=='/start':
        txt=f'assalomu alekum {name} botga hush kelibsiz pasdagi bayramlardan birini tanlang va unga tabriklamoqchi bo\'lgan kishingizni ismini kiriting'
        oldid=newid
    if oldid != newid:
        if text=="Tug'ilgan kun":
            sendphoto(chat_id,'https://happy-birthday-quotes.com/wp-content/uploads/2019/02/Happy-Birthday.jpg')  
            txtt=f'assalomu alekum {name}. Tabriklamoqchi bo\'lgan kishingizni ismini kiriting'
            sendMessage(chat_id,txtt)
            lst=[]
            txt=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nSog'inchlardan yasay sizga guldasta\nGuldasta qilib qalbim payvasta\nOlislardan turib deyman men asta\nTug'ilgan kuningiz muborak bo'lsin {text}!!!"
            txt1=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nTilaklar ichida izlab topganim,\nAlloh nigohini sizga qaratsin.\nYagona o’tinchim Allohdan bu kun,\nSizdek insonlarni ko’proq yaratsin!\nTavallud ayyomingiz qutlug’ bo’lsin {text}!!!"
            txt2=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nShirin hayotingiz manoga to‘lsin!\nIstagan niyatingiz ijobat bo‘lsin!\nChexrangiz so‘nmasin hamisha kulsin,\nTug‘ilgan kuningiz muborak bo‘lsin {text}!!!"
            txt3=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nSizga so'g'lik so'ray xudodan,\nYaratgan asrasin balo qazodan.\nQo`lingiz tushmasin aslo duodan,\nHayotingiz nurlarga to'lsiz,\nTug'ilgan kuningiz muborak bo'lsin {text}!!!"
            lst.append(txt)
            lst.append(txt1)
            lst.append(txt2)
            lst.append(txt3)
            rand=random.choice(lst)
            sendMessage(chat_id,rand)
            lasttxt='Boshqa bayramlarni ham tanlashingiz mumkin!!!'
            sendMessage(chat_id,lasttxt)
            oldid=newid
        elif text=="8-mart":
            txtt=f'assalomu alekum {name}. Tabriklamoqchi bo\'lgan kishingizni ismini kiriting.Onangizni tabriklamoqchi bo\'lsangiz:onajonim so\'zini kiritin yoki ism'
            sendMessage(chat_id,txtt)
            sendphoto(chat_id,'http://zamonaviy.com/_ph/21/723036447.jpg?1602100767')
            lst=[]
            txt=f"Assalomu aleykum!!!\n{text} sizni bugungi 8-mart bayrami bilan chin qalbdan tabriklayman\n\nBugun o'zgacha sho'x sayrar bulbullar\nBayram shodligidan yayraydi dillar.\nO'zgacha zavq ela shodon Ko'ngillar\nBayramingiz muborak aziz ayollar\nbaxtimizga omon bo'ling ayollar. !!!"
            txt1=f"Assalomu aleykum!!!\n{text} sizni bugungi 8-mart bayrami bilan chin qalbdan tabriklayman\n\nG'am sizdan yiroq bo'lsin,\nTabassum xamrox bo'lsin\nBahordek pok umringiz,\nDoim quvonchga to'lsin\n8-Mart muborak bulsin!!!"
            txt2=f"Assalomu aleykum!!!\n{text} sizni bugungi 8-mart bayrami bilan chin qalbdan tabriklayman\n\nAzizim hayotda shodlik bor bo'lsin\nAna shu shodliklar sizga yor bo'lsin\nQalbingiz orzu va quvonchga to'lsin\nBugun tailayman sizga ko'p tilak.\n8-MART bo'lsin muborak!!!"
            txt3=f"Assalomu aleykum!!!\n{text} sizni bugungi 8-mart bayrami bilan chin qalbdan tabriklayman\n\nErta bahor gullagan binafsha misol,\nKo'nglingiz doim beg'ubor bo'lsin.\nYangi ochilgan gul 'Lola' misol,\nLablarizda doim tabassum bo'lsin.\nDildan ezgu tilaklarim sizgadir tanxo.\n'8-MART' Ayyomingiz muborak bo'lsin!!!!"
            lst.append(txt)
            lst.append(txt1)
            lst.append(txt2)
            lst.append(txt3)
            rand=random.choice(lst)
            sendMessage(chat_id,rand)
            lasttxt='Boshqa bayramlarni ham tanlashingiz mumkin!!!'
            sendMessage(chat_id,lasttxt)
            oldid=newid
        elif text=="Navro'z":
            txtt=f'assalomu alekum {name}. Tabriklamoqchi bo\'lgan kishingizni ismini kiriting.'
            sendMessage(chat_id,txtt)
            sendphoto(chat_id,'https://m.ok.ru/group/51994029654152/album/51994062946440/771490595720')
            lst=[]
            txt=f"Assalomu aleykum!!!\n{text} sizni bugungi 21-mart navro'z bayrami bilan chin qalbdan tabriklayman\n\nАйлабон лутфу-карам, наврўзи олам келдилар,\nЎсмадан қоши қалам, наврўзи олам келдилар.\nБир ажиб ҳис уйғотиб ирмоқларнинг хониши,\nКуйлашиб савту ажам, наврўзи олам келдилар.!!!"
            txt1=f"Assalomu aleykum!!!\n{text} sizni bugungi 21-mart navro'z bayrami bilan chin qalbdan tabriklayman\n\nHush kelding navruzim O'zbekistonga\nHush kurdik boychechak bodom gullaring.\nIstiqlol yuz ochgan ota makonga\nAnvorlar tashiydi toza yellaring...\nHamma forumdoshlarni Navro'zi ayyom bilan tabriklayman!!!\nSizlarni aslo baxoriy kayfiyat tark etmasin!!!!"
            txt2=f"Assalomu aleykum!!!\n{text} sizni bugungi 21-mart navro'z bayrami bilan chin qalbdan tabriklayman\n\nBaxor gullaridan guldasta sizga \nChin qalbim tabrigi payvasta sizga \nBir asr yashanggu, ya'na nim chorak \nNAVRO'ZI OLAM bo'lsin muborak !!!"
            txt3=f"Assalomu aleykum!!!\n{text} sizni bugungi 21-mart navro'z bayrami bilan chin qalbdan tabriklayman\n\nNavro'z ekan tabrik sizniki,\nYangi kunda kulgu sizniki,\nBu kun yana zamin bizniki,\nBayram bo'lsin sayyod bizniki! !!!"
            lst.append(txt)
            lst.append(txt1)
            lst.append(txt2)
            lst.append(txt3)
            rand=random.choice(lst)
            sendMessage(chat_id,rand)
            lasttxt='Boshqa bayramlarni ham tanlashingiz mumkin!!!'
            sendMessage(chat_id,lasttxt)
            oldid=newid
        elif text=="Hayit bayrami":
            txtt=f'assalomu alekum {name}. Tabriklamoqchi bo\'lgan kishingizni ismini kiriting.'
            sendMessage(chat_id,txtt)
            sendphoto(chat_id,'https://ahlisunna.uz/hayit-namozi/')
            lst=[]
            txt=f"Assalomu aleykum!!!\n{text} sizni bugungi Hayit bayrami bilan chin qalbdan tabriklayman\n\nAlloh uyingizga nur,\nqalbingizga huzur,\noilangizga baxt, \no'rningizga taxt ato etsin!\nQurbon hayit muborak bo'lsin!!!"
            txt1=f"Assalomu aleykum!!!\n{text} sizni bugungi Hayit bayrami bilan chin qalbdan tabriklayman\n\nAllohning rahmati sizga bo'lsin,\nQalbingiz yanada iymon, nurga to'lsin.\nShukurkim yetkazdi ulug' kunlarga,\nHayit ayyomingiz muborak bo'lsin.!!!"
            txt2=f"Assalomu aleykum!!!\n{text} sizni bugungi Hayit bayrami bilan chin qalbdan tabriklayman\n\nIymoning nuridan qalbingiz to'lsin\nKo'ngil shodligidan ko'zingiz to'lsin\nShunday qutlug' kunda ey birodarim\nQurbon hayitingiz muborak bo'lsin.!!!"
            txt3=f"Assalomu aleykum!!!\n{text} sizni bugungi Hayit bayrami bilan chin qalbdan tabriklayman\n\nTortiq bo'lsin sizga duo salomlar,\nDuoga eng go'zal shirin kalomlar.\nIloho uyingiz nurlarga to'lsin,\nQurbon hayit ayyomingiz muborak bo'lsin!!!!"
            lst.append(txt)
            lst.append(txt1)
            lst.append(txt2)
            lst.append(txt3)
            rand=random.choice(lst)
            sendMessage(chat_id,rand)
            lasttxt='Boshqa bayramlarni ham tanlashingiz mumkin!!!'
            sendMessage(chat_id,lasttxt)
            oldid=newid
        elif text=="Yangi yil":
            txtt=f'assalomu alekum {name}. Tabriklamoqchi bo\'lgan kishingizni ismini kiriting.'
            sendMessage(chat_id,txtt)
            sendphoto(chat_id,'https://en.wikipedia.org/wiki/Chinese_New_Year#/media/File:Kung_Hei_Fat_Choi!_(6834861529).jpg')
            lst=[]
            txt=f"Assalomu aleykum!!!\n{text} sizni bugungi yangi yil bayrami bilan chin qalbdan tabriklayman\n\nY-angi yil sizga,\nA-rmonsiz hayot,\nN-iyatlar röyobi,\nG-özal xotiralar,\nI-shlariz rivoji,\nY-akuni yo'q baxt,\nI-lohiy mojiza va\nL-atif damlarni olib kelsin!!!!"
            txt1=f"Assalomu aleykum!!!\n{text} sizni bugungi yangi yil bayrami bilan chin qalbdan tabriklayman\n\nTabassumga burkansin dunyo,\nQordek oppoq bo’lsin dilingiz.\nBo’lsin qordek tozа, musaffo\nQadam qo’ygan YANGI YILINGIZ!!!"
            txt2=f"Assalomu aleykum!!!\n{text} sizni bugungi yangi yil bayrami bilan chin qalbdan tabriklayman\n\nYangi kun keltirsin baht, omad, quvonch,\nHech qachon do'stlardan ketmasin ishonch,\nSamimiy bo'lsin suhbatda so'zlar,\nYoshlansa quvonchdan yoshlansin ko'zlar.\nYahshi so'z maqtovlar yangrasin doim,\nOmad yaqin do'stingiz bo'lsin ilohim!!!"
            txt3=f"Assalomu aleykum!!!\n{text} sizni bugungi yangi yil bayrami bilan chin qalbdan tabriklayman\n\n​Yangi kun keltirsin baht, omad, quvonch,\nHech qachon do’stlardan ketmasin ishonch,\nSamimiy bo’lsin suhbatda so’zlar,\nYoshlansa quvonchdan yoshlansin ko’zlar.!!!"
            lst.append(txt)
            lst.append(txt1)
            lst.append(txt2)
            lst.append(txt3)
            rand=random.choice(lst)
            sendMessage(chat_id,rand)
            lasttxt='Boshqa bayramlarni ham tanlashingiz mumkin!!!'
            sendMessage(chat_id,lasttxt)
            oldid=newid
        elif text=="14-yanvar":
            txtt=f'assalomu alekum {name}. Tabriklamoqchi bo\'lgan kishingizni ismini kiriting.'
            sendMessage(chat_id,txtt)
            sendphoto(chat_id,'http://sherlaruz.com/news/bajram_muborak_14_yanvar_uchun_sher_tabriklar/2020-01-17-5302')
            txt=f"Assalomu aleykum!!!\n{text} sizni bugungi 14-yanvar vatan himoyachilar kuni bilan chin qalbdan tabriklayman\n\n-Эркаклар бўлмаса айтилмас азон,\n-Эркаклар бўлмаса қайнамас қозон,\n-Эркаклар бўлмаса чақалоқ қайда,\n-Эркаклар бўлмаса шапалоқ қайда,\n-Эркаклар бўлмаса мўйлов қайдадир,\n-Эркаклар бўлмаса куёв қайдадир,\n-Дунё тургунча турсин эркаклар,\n-Доимо хурматда юрсин эркаклар! \nБайрам муборак!!!"
            sendMessage(chat_id,txt)
            lasttxt='Boshqa bayramlarni ham tanlashingiz mumkin!!!'
            sendMessage(chat_id,lasttxt)
            oldid=newid
        else:
            continue