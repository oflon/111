import datetime
import time
from random import randint
import telebot
from telebot import types


# ПОДКЛЮЧЕНИЕ API БОТА
bot = telebot.TeleBot('1922640558:AAE78lWj1mYC6uT-jp303jLo8OXFxFJRn0k')

#1922640558:AAE78lWj1mYC6uT-jp303jLo8OXFxFJRn0k

# ФУНКЦИЯ ДЛЯ СТАРТА ОБЩЕНИЯ
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
    btn1 = types.KeyboardButton('📜 АССОРТИМЕНТ 📜')
    btn2 = types.KeyboardButton('🥰 ОТЗЫВЫ 🥰')
    markup.add(btn1, btn2)

#---------------------------------------------------------------------------------------
    # ПРИВЕТСТВИЕ ПОЛЬЗОВАТЕЛЯ
    send_mess = f"<b> Приветсвую вас, {message.from_user.first_name}</b>!\n\nЯ - бот по продаже медицинских справок📃 Все подскажу, объясню и помогу с выбором справки\n\nНажав на кнопку 'ОТЗЫВЫ' вы можете посмотреть отзывы наших покупателей.\n\n☑️<b>По всем вопросам обращаться к главному администратору - @COVIDMEN</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

#----------------------------------------------------------------------------------------
@bot.message_handler(content_types=['sticker'])
def stick(message):
    send_mess = 'Ты тупой ?'
    bot.send_message(message.chat.id, send_mess)

#----------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == '📜 ассортимент 📜':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('👶 РЕБЕНКУ 👶')
        btn2 = types.KeyboardButton('👱 СТУДЕНТУ 👱')
        btn3 = types.KeyboardButton('👨 ВЗРОСЛОМУ 👨')
        btn4 = types.KeyboardButton('🦠 КОРОНАВИРУС 🦠')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = 'КОМУ НУЖНА СПРАВКА ?'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)

    elif get_message_bot == '🥰 отзывы 🥰':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('📜 АССОРТИМЕНТ 📜')
        btn2 = types.KeyboardButton('🥰 ОТЗЫВЫ 🥰')
        markup.add(btn1, btn2)
        send_mess = "↘️  КАНАЛ С ОТЗЫВАМИ ↙ \n➡  <a href='t.me/vaccine_free'>ПЕРЕЙТИ </a>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)

    elif get_message_bot == '👶 ребенку 👶':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('🔥 НЕОБХОДИМЫЕ ДОКУМЕНТЫ 🔥')
        btn2 = types.KeyboardButton('🔄 НАЗАД 🔄')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = '🔸Медицинская карта ребенка\n(форма 026/y)\n➖ <b>5000₽</b>\n\n🔸Карта профилактических прививок \n(форма 063/y)\n➖ <b>2500₽</b>\n\n🔸Справка об опеке и попечительстве \n(форма 164/ y-96)\n➖ <b>2500₽</b> \n\n🔸Справка для оформления\nребенка на усыновление\n(форма 160) \n ➖ <b>2500₽</b>'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)

    elif get_message_bot == '👱 студенту 👱':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('🔥 НЕОБХОДИМЫЕ ДОКУМЕНТЫ 🔥')
        btn2 = types.KeyboardButton('🔄 НАЗАД 🔄')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = '🔸Справка о временной нетрудоспособности учащегося \n(форма 095/у)\n➖ <b>800₽</b>\n\n 🔸Справка на закрытие пропусков от 14 дней \n(формы095/y+027/y)\n➖ <b>2500₽</b>\n\n🔸Академический отпуск\n ➖ <b>3500₽</b>\n\n🔸Справка для выхода из\n академического отпуска\n➖ <b>1500₽</b>\n\n🔸Справка-вызов на сессию \n ➖ <b>5000₽</b>'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '👨 взрослому 👨':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('🔥 НЕОБХОДИМЫЕ ДОКУМЕНТЫ 🔥')
        btn2 = types.KeyboardButton('🔄 НАЗАД 🔄')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = "🔸Паспорт здоровья \n(приказ 302н)\n➖ <b>1500₽</b>\n\n🔸Справка на госслужбу \n(форма 001 ГС/у)\n➖ <b>1400₽</b>\n\n🔸Справка о беременности \n(из женской консультации)\n➖ <b>1000₽</b>\n\n🔸Медицинская справка для работы на высоте \n(форма 405)\n➖ <b>1200₽</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '🦠 коронавирус 🦠':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('🔥 НЕОБХОДИМЫЕ ДОКУМЕНТЫ 🔥')
        btn2 = types.KeyboardButton('🔄 НАЗАД 🔄')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = "🔸Сертификат о полной вакцинации с внесением в реестр госуслуг  \n➖<b> 3500₽</b>\n о перенесенном заболевании \n➖ <b>2500₽</b>\n\n🔸Сертификат в бумажной форме \nО прохождении вакцинации \n➖ <b>2200₽</b>\n O перенесенной болезни \n➖ <b>2000₽</b>\n\n🔸QR- код, свидетельствующий о прохождении вакцинации \n➖ <b>1500₽</b>\n\n🔸ПЦР-тест \n(положительный/отрицательный) \n➖ <b>2000₽</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '🔥 необходимые документы 🔥':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('💵 ОПЛАТИТЬ 💵')
        btn2 = types.KeyboardButton('🔄 НАЗАД 🔄')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = "Для приобретения документов требуется:\n1⃣ ФИО\n2⃣ Серия и номер паспорта\n3⃣ Дата рождения\n4⃣ Прописка\n5⃣ СНИЛС\n––––––––––––––––––––––––––––––––––––––––––––––––––––\nДля приобретения документов на ребенка требуется:\n1⃣ ФИО\n2⃣ Свидетельство о рождении\n3⃣ Дата рождения\n4⃣ Прописка\n5⃣ СНИЛС"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)
        send_mess = "<b>⚠️Ваши данные присылайте главному администратору @Covidmen с УКАЗАНИЕМ ДОКУМЕНТА, который хотите приобрести</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)


    elif get_message_bot == '🔄 назад 🔄':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('👶 РЕБЕНКУ 👶')
        btn2 = types.KeyboardButton('👱 СТУДЕНТУ 👱')
        btn3 = types.KeyboardButton('👨 ВЗРОСЛОМУ 👨')
        btn4 = types.KeyboardButton('🦠 КОРОНАВИРУС 🦠')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = 'КОМУ НУЖНА СПРАВКА ?'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '🔙️ на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('📜 АССОРТИМЕНТ 📜')
        btn2 = types.KeyboardButton('🥰 ОТЗЫВЫ 🥰')
        markup.add(btn1, btn2)
        send_mess = 'Вернулись в главное меню'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)

    elif get_message_bot == '💵 оплатить 💵':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('🔥 QIWI 🔥')
        btn2 = types.KeyboardButton('💴 ЮMONEY 💴')
        btn3 = types.KeyboardButton('💎 WEBMONEY 💎')
        btn4 = types.KeyboardButton('💸 КРИПТОВАЛЮТА 💸')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = '🗣 Уважаемый клиент, у магазина существует четыре вида ОПЛАТЫ:\n\n1)Перевод по никнейму на кошелек QIWI\n\n2)Перевод на электронный кошелек WebMoney\n\n3)Оплата криптовалютой \n\n4)Перевод на виртуальную карту YooMoney с карты Сбербанка или карты YooMoney'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif get_message_bot == '🔥 qiwi 🔥':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=2)
        btn1 = types.KeyboardButton('💰 ВЫБОР ОПЛАТЫ')
        btn2 = types.KeyboardButton('☑ ОПЛАТИЛ')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = '✅ Перевод по никнейму:\n➖➖➖➖➖➖➖➖➖\n --- WOVES2016 ---\n➖➖➖➖➖➖➖➖➖\n⚠️ После оплаты жмите кнопку ОПЛАТИЛ. '
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '💴 юmoney 💴':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=2)
        btn1 = types.KeyboardButton('💰 ВЫБОР ОПЛАТЫ')
        btn2 = types.KeyboardButton('☑ ОПЛАТИЛ')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = '✅ Перевод на Юмани кошелек\n➖➖➖➖➖➖➖➖➖➖\n--- 4100116900360920 ---\n➖➖➖➖➖➖➖➖➖➖\n⚠️ После оплаты жмите кнопку ОПЛАТИЛ.'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif get_message_bot == '💎 webmoney 💎':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=2)
        btn1 = types.KeyboardButton('💰 ВЫБОР ОПЛАТЫ')
        btn2 = types.KeyboardButton('☑ ОПЛАТИЛ')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = '✅ Перевод по номеру кошелька:\n➖➖➖➖➖➖➖➖➖\n --- R543594603335 ---\n➖➖➖➖➖➖➖➖➖\n⚠️ После оплаты жмите кнопку ОПЛАТИЛ.'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '💸 криптовалюта 💸':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=2)
        btn1 = types.KeyboardButton('💰 ВЫБОР ОПЛАТЫ')
        btn2 = types.KeyboardButton('☑ ОПЛАТИЛ')
        btn3 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2, btn3)
        send_mess = '✅ Перевод на Биткойн кошелек\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖ 3KwfZg9brjfNf3QHHRsAqsKEQkoJU9Qymu\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n⚠️ После оплаты жмите кнопку ОПЛАТИЛ.'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '💰 выбор оплаты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('🔥 QIWI 🔥')
        btn2 = types.KeyboardButton('💴 ЮMONEY 💴')
        btn3 = types.KeyboardButton('💎 WEBMONEY 💎')
        btn4 = types.KeyboardButton('💸 КРИПТОВАЛЮТА 💸')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = 'Выберите подходящий способ оплаты'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)

    elif get_message_bot == '☑ оплатил':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('💰 ВЫБОР ОПЛАТЫ ')
        btn2 = types.KeyboardButton('🔙️ НА ГЛАВНУЮ')
        markup.add(btn1, btn2)
        time.sleep(1)
        send_mess = 'ПРОВЕРКА ОПЛАТЫ ⏳'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        time.sleep(randint(3, 8))
        send_mess = '❌ ИЗВИНИТЕ , НО ОПЛАТА НЕ НАЙДЕНА \n\nЕсли Вы совершили перевод , то приложите скрин чека и отправьте администратору.\nАдминистратор рассмотрит проблему в течении 24 часов'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)
        send_mess = '<b>Cсылка на админа @Covidmen</b>'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)

    elif get_message_bot == 'прощай':
        send_mess = 'Ты был лучшим хозяином'
        bot.send_message(message.chat.id, send_mess, parse_mode='html',disable_web_page_preview=True)

    elif get_message_bot == 'нет':
        send_mess = 'Пидора ответ))0)'
        bot.send_message(message.chat.id, send_mess, parse_mode='html',disable_web_page_preview=True)

    elif get_message_bot == 'да':
        send_mess = 'Пизда)'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', disable_web_page_preview=True)

    elif get_message_bot == 'ага':
        send_mess = 'Ладно'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', disable_web_page_preview=True)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
        btn1 = types.KeyboardButton('📜 АССОРТИМЕНТ 📜')
        btn2 = types.KeyboardButton('🥰 ОТЗЫВЫ 🥰')
        markup.add(btn1, btn2)
        send_mess = 'НАЖИМАЙ НА КНОПКИ❗️'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview=True)



# БОТ АКТИВЕН ВСЕГДА
bot.polling(none_stop=True)