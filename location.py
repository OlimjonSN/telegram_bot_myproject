import os
from telegram.ext import Updater, CommandHandler ,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton
def start(update,context):               
    button=KeyboardButton(text='location',request_location=True)
    keyboard=ReplyKeyboardMarkup([[button]],resize_keyboard=True)
    bot=context.bot
    chat_id=update.message.chat.id
    print(chat_id)
    name=update.message.chat.first_name
    bot.sendMessage(chat_id, f'assalomu alekum {name}\npastdagi tugmani bosing👇👇',reply_markup=keyboard)
def get_location(update,context):
    f=open('location.txt', 'a')
    bot=context.bot
    chat_id=update.message.chat.id
    location=update.message.location
    text='Manzil uchun rahmat'
    longitude=update.message.location.longitude
    latitude=update.message.location.latitude
    f.write(str(location))
    bot.send_message(chat_id, text)
    bot.send_location(981654463,latitude, longitude)
    

updater = Updater('1312813769:AAFCnmW8tZzbN8Bd_d6RSis8KO1Kc4JfLp0')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))
updater.start_polling()
updater.idle()