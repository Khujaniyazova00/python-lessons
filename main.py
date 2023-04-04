from telebot import TeleBot, types
token = "6081857047:AAGpzlgaTLaq38Rh1iqH2RjiqVRvJ1fmST4"
mybot = TeleBot(token)

# @mybot.message_handler(commands=['start'])
# def boshlash(message):
#     tugmalar = types.ReplyKeyboardMarkup(True)
#     tugmalar.row("Dushanba", "Seshanba", "Chorshanba")
#     tugmalar.row("Payshanba", "Juma", "Shanba")
#     mybot.send_message(message.chat.id, "qaysi kun kerak ", reply_markup=tugmalar)


# @mybot.message_handler(content_types=['text'])
# def matn(message):
#     if message.text == "Dushanba":
#         info = "Bioinformatika 213-xona ass R.Baltayev"
#         info += "Geomalumotlar 109-xona ass Z.Hakimov"
#         mybot.reply_to(message, info)
#     elif message.text == "Seshanba":
#             info = "Bioinformatika 213-xona ass R.Baltayev"
#             info += "Geomalumotlar 109-xona ass Z.Hakimov"
#             mybot.reply_to(message, info)
#
# @mybot.message_handler(content_types=['text'])
# def matn(message):
#     tugma1 = types.InlineKeyboardMarkup()
#     tugma2 = types.InlineKeyboardButton("Bioinformatika", callback_data="Bio")
#     tugmalar = types.InlineKeyboardButton("Geomalumotlar", callback_data="Geo")
#     tugmalar.add(tugma1)
#     tugmalar.add(tugma2)
#
#     if message.text == "Dushanba":
#         mybot.reply_to(message,"Fanlar",reply_markup=tugmalar)


@mybot.message_handler(commands=['start'])
def boshlash(message):
    info = "familiyasi:" + str(message.chat.last_name) + "\n"
    info += "ismi:" + str(message.chat.first_name) + "\n"
    info += "username:" + str(message.chat.username) + "\n"
    info += "id:" + str(message.chat.id) + "\n"

    mybot.send_message(message.chat.id,info)
    mybot.send_message(message.chat.id, message)


mybot.polling()
