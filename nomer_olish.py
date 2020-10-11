import os
from telegram.ext import Updater, CommandHandler ,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton
TOKEN = os.environ['TOKEN']   
print(TOKEN)  
def start(update,context):               
    button=KeyboardButton(text='let\'s go',request_contact=True)
    keyboard=ReplyKeyboardMarkup([[button]],resize_keyboard=True)
    bot=context.bot
    chat_id=update.message.chat.id
    name=update.message.chat.first_name
    bot.sendMessage(chat_id, f'assalomu alekum {name}\npastdagi tugmani bosing👇👇',reply_markup=keyboard)
def get_contact(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    firstname=update.message.chat.first_name
    lastname=update.message.chat.last_name
    contact=update.message.contact
    text=f'contact:{contact}\n'
    bot.sendMessage(chat_id,'nomer uchun raxmat 😂😜!!!')
    f=open('save_contact.txt','a')
    f.write(text)
    f.close()

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.contact,get_contact))
updater.start_polling()
updater.idle()