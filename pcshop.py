from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton


def start(update, context):
    name=update.message.chat.first_name
    text=f'👋assalomu alekum {name} kompyuter extiyot qisimlari va 🖥kompyuterlar buyurtma qiling!!!(unutmang eng yaxshi va hamyonbop maxsulotlarni bizning botdan topasiz 😊)'
    update.message.reply_text(text)
    button=ReplyKeyboardMarkup([['🖥stol kompyuter🖥','💻noutbook💻'],['🖨printer🖨','🕹aksesuarlar🕹'],['💾kompyuter qisimlari💾']],resize_keyboard=True)  
    text2='o\'zingizga kerakli kategoriyani tanlang.'
    update.message.reply_text(text2,reply_markup=button)
def pc(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text=update.message.text
    button=InlineKeyboardButton('ofice uchun', switch_inline_query_current_chat='pcofice')
    button2=InlineKeyboardButton('o\'yin uchun', switch_inline_query_current_chat='pco\'yin')
    reply_markup=InlineKeyboardMarkup([
        [button,button2]
    ])
    bot.sendMessage(chat_id, text, reply_markup=reply_markup)

def pcofice(update,context):
    text='ram:2g \nvga:intelHdgraphic \nhdd:500\ncpu:intel celeron 1\.80 Ghz'
    text1='ram:4g \nvga:NVIDA GEFORCE GT720 1gb \nhdd:1TB\ncpu:intel core i3 2\.80 Ghz'
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




updater = Updater('1116012218:AAHXOvZDGx3mUOBIaCD7B83r7v4eJevk8GQ')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🖥stol kompyuter🖥'), pc))
updater.dispatcher.add_handler(InlineQueryHandler(pcofice, pattern='pcofice'))


updater.start_polling()
updater.idle()
