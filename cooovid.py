from covid import Covid
from telegram import Update, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext,CallbackQueryHandler
import os
TOKEN=os.environ['TOKEN']
covid=Covid()

def start(update, context):
    bot=context.bot
    name=update.message.chat.first_name
    chat_id=update.message.chat.id
    text=f'👋assalomu alekum {name} qaysi biri haqdagi statistikani bilmoqchimisiz o\'sha tugamni bosing'
    pc=InlineKeyboardButton('zararlanganlar',callback_data='zarar')
    laptop=InlineKeyboardButton('vafot etganlar',callback_data='olgan')
    qisim=InlineKeyboardButton('tuzalganlar',callback_data='tuzalgan')
    reply_markup=InlineKeyboardMarkup([[pc],[laptop],[qisim]],resize_keyboard=True)
    bot.sendMessage(chat_id,text,reply_markup=reply_markup)
def bosh(update, context):
    query=update.callback_query
    text=f'qaysi biri haqdagi statistikani bilmoqchimisiz o\'sha tugamni bosing'
    zararlanganlar=InlineKeyboardButton('😷zararlanganlar😷',callback_data='zarar')
    olgan=InlineKeyboardButton('😷vafot etganlar😷',callback_data='olgan')
    tuzalgan=InlineKeyboardButton('😷tuzalganlar😷',callback_data='tuzalgan')
    reply_markup=InlineKeyboardMarkup([[zararlanganlar],[olgan],[tuzalgan]],resize_keyboard=True)
    query.edit_message_text(text,reply_markup=reply_markup)
def zarar(update,context):
    query=update.callback_query
    zararlanganlar=covid.get_total_active_cases()
    text=f"hozirgi kunda dunyo bo'yicha covid bilan zararlanganlar😷 soni {zararlanganlar}ga teng."
    bosh=InlineKeyboardButton('🏠bosh menyuga qaytish🏠',callback_data='bosh')
    reply_markup=InlineKeyboardMarkup([[bosh]],resize_keyboard=True)
    query.edit_message_text(text,reply_markup=reply_markup)
def olgan(update,context):    
    query=update.callback_query
    olgan=covid.get_total_deaths()
    text=f"hozirgi kunda dunyo bo'yicha coviddan vafot etganlar soni {olgan}ga teng."
    bosh=InlineKeyboardButton('🏠bosh menyuga qaytish🏠',callback_data='bosh')
    reply_markup=InlineKeyboardMarkup([[bosh]],resize_keyboard=True)
    query.edit_message_text(text,reply_markup=reply_markup)
def tuzalgan(update,context):    
    query=update.callback_query
    tuzalgan=covid.get_total_confirmed_cases()
    text=f"hozirgi kunda dunyo bo'yicha coviddan sog'ayib😊 ketganlar soni {tuzalgan}ga teng."
    bosh=InlineKeyboardButton('🏠bosh menyuga qaytish🏠',callback_data='bosh')
    reply_markup=InlineKeyboardMarkup([[bosh]],resize_keyboard=True)
    query.edit_message_text(text,reply_markup=reply_markup)


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(zarar, pattern='zarar'))
updater.dispatcher.add_handler(CallbackQueryHandler(olgan, pattern='olgan'))
updater.dispatcher.add_handler(CallbackQueryHandler(tuzalgan, pattern='tuzalgan'))
updater.dispatcher.add_handler(CallbackQueryHandler(bosh, pattern='bosh'))
updater.start_polling()
updater.idle()