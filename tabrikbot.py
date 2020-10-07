import requests
import random
import telegram
# def getUpdats():
bot=telegram.Bot(token='1190968624:AAHSBci771kMSzJDgrJwiF4k9Dxrlp3KWwo')
update=bot.getUpdates()[-1]
newid=update.update_id
print(newid)
# a=getUpdats()
# print(a)
# oldid=-1
# while True:
#     newid=getUpdats()
#     chat_id,text=get()
#     if text!='/start':
#         if oldid != newid:
#             lst=[]
#             txt=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nSog'inchlardan yasay sizga guldasta\nGuldasta qilib qalbim payvasta\nOlislardan turib deyman men asta\nTug'ilgan kuningiz muborak bo'lsin {text}!!!"
#             txt1=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nTilaklar ichida izlab topganim,\nAlloh nigohini sizga qaratsin.\nYagona o’tinchim Allohdan bu kun,\nSizdek insonlarni ko’proq yaratsin!\nTavallud ayyomingiz qutlug’ bo’lsin {text}!!!"
#             txt2=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nShirin hayotingiz manoga to‘lsin!\nIstagan niyatingiz ijobat bo‘lsin!\nChexrangiz so‘nmasin hamisha kulsin,\nTug‘ilgan kuningiz muborak bo‘lsin {text}!!!"
#             txt3=f"Assalomu aleykum!!!\n{text} sizni bugungi ulug' kun tavvalud ayomingiz bilan chin qalbdan tabriklab qolaman va siz uchun 4 misra sh'er\n\nSizga so'g'lik so'ray xudodan,\nYaratgan asrasin balo qazodan.\nQo`lingiz tushmasin aslo duodan,\nHayotingiz nurlarga to'lsiz,\nTug'ilgan kuningiz muborak bo'lsin {text}!!!"
#             lst.append(txt)
#             lst.append(txt1)
#             lst.append(txt2)
#             lst.append(txt3)
#             rand=random.choice(lst)
#             send(chat_id,rand)
#             oldid=newid
#         else:
#             continue