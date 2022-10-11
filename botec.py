import telebot as tb
from telebot import types as tp

bot = tb.TeleBot("5226453773:AAGyE75AFft5OuuVlHWzg_edLzPaxNac6gQ")
bot_name = 'g'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    klava = tp.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    answ12 = tp.KeyboardButton(text='Регистрация')
    answ1 = tp.KeyboardButton(text='Регистрация')
    answ2 = tp.KeyboardButton(text='Расписание мероприятий')
    klava.add(answ2, answ12)
    bot.send_message(message.chat.id, 'Добро пожаловать в', reply_markup=klava)
    bot.send_message(1756196334, message.from_user.username)
@bot.message_handler(func= lambda message: 'Регистрация' in message.text)
def registr(message):
    klava = tp.ReplyKeyboardMarkup(resize_keyboard= True, row_width= 2)
    answ1 = tp.KeyboardButton(text='мп1')
    answ2 = tp.KeyboardButton(text='мп2')
    answ3 = tp.KeyboardButton(text='мп3')
    beck = tp.KeyboardButton(text='Назад')
    klava.add(answ1, answ2, answ3, beck)
    bot.send_message(message.chat.id, 'список мп', reply_markup=klava)
@bot.message_handler(func= lambda message: '')
@bot.message_handler(func= lambda message: 'Назад' in message.text)
def back(message):
    bot.send_message(message.chat.id, 'вы в начале')
    send_welcome(message)
    vova eblan
bot.infinity_polling()
