import telebot
from telebot import types

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 Kurslar")
    btn2 = types.KeyboardButton("📞 Admin")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id,
    "Assalomu alaykum!\nKurslarni ko‘rish uchun tugmani bosing.",
    reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📚 Kurslar")
def kurslar(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Python kursi - 50 000 so'm", callback_data="python")
    btn2 = types.InlineKeyboardButton("SMM kursi - 40 000 so'm", callback_data="smm")

    markup.add(btn1)
    markup.add(btn2)

    bot.send_message(message.chat.id, "Kerakli kursni tanlang:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "python":
        bot.send_message(call.message.chat.id,
        "💳 To‘lov uchun karta:\n8600 1234 5678 9012\n\nTo‘lovdan keyin chekni yuboring.")

    if call.data == "smm":
        bot.send_message(call.message.chat.id,
        "💳 To‘lov uchun karta:\n8600 1234 5678 9012\n\nTo‘lovdan keyin chekni yuboring.")

@bot.message_handler(content_types=['photo'])
def check(message):
    bot.send_message(message.chat.id,
    "✅ To‘lov qabul qilindi.\n\nMana kurs linki:\nhttps://t.me/yourkurs")