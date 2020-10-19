from telegram import Update, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    name=update.message.chat.first_name
    text=f'👋assalomu alekum {name} kompyuter extiyot qisimlari va 🖥kompyuterlar buyurtma qiling!!!(unutmang eng yaxshi va hamyonbop maxsulotlarni bizning botdan topasiz 😊)'
    bot.sendMessage(chat_id,text)
    pc=InlineKeyboardButton('🖥stol kompyuter🖥',callback_data='pc')
    laptop=InlineKeyboardButton('💻noutbook💻',callback_data='laptop')
    qisim=InlineKeyboardButton('💾kompyuter qisimlari💾',callback_data='qisim')
    akses=InlineKeyboardButton('🕹aksesuarlar🕹',callback_data='akses')
    reply_markup=InlineKeyboardMarkup([[pc],[laptop],[qisim],[akses]],resize_keyboard=True)
    text2='o\'zingizga kerakli kategoriyani tanlang.'
    bot.sendMessage(chat_id,text2,reply_markup=reply_markup)



updater = Updater('1350095960:AAFCZqFU2pKAJ9JS_WcllRgiD6yNAPxqFJc')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()