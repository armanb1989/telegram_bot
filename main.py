# первая попытка написать скрипт для бота

import telebot
import constants

bot = telebot.TeleBot(constants.token)

print(bot.get_me())

# Логирование чата -----------------------------------------------------------------------------
def log(message, answer):
    print("\n -----------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

# Кастомная клавиатура чата -------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Контакты', 'Информация', 'Нефтебазы')
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

# Декораторы команд ---------------------------------------------------------------------------
@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Мои возможности весьма специфичны. 
Но ты посмотри! Все работает!""")

# Декораторы автоответов ----------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "контроль" or message.text == "качество" \
            or message.text == "контроль качества" or message.text == "Контроль" \
            or message.text == "Качество" or message.text == "Контроль качества"\
            or message.text == "Бирюкова" or message.text == "бирюкова":
        answer = constants.control
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "метролог" or message.text == "метрология" or message.text == "Метролог" \
            or message.text == "Метрология" or message.text == "Дворецкий" \
            or message.text == "дворецкий":
        answer = constants.metrolog
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "апб" or message.text == "административная поддержка бизнеса" \
            or message.text == "поддержка" or message.text == "бизнес" or message.text == "Колонтай" \
            or message.text == "Апб" or message.text == "Поддержка" or message.text == "Бизнес" \
            or message.text == "колонтай" or message.text == "АПБ":
        answer = constants.apb
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "директор" or message.text == "Ощепков" or message.text == "Директор" \
            or message.text == "ощепков":
        answer = constants.director
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "мто" or message.text == "МТО" or message.text == "снабжение" \
        or message.text == "Едиханов" or message.text == "едиханов" or message.text == "Мто":
        answer = constants.mto
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    # Меню Контакты
    elif message.text == "Контакты":
        user_markup_contacts = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup_contacts.row('Директор', 'АПБ', 'IT')
        user_markup_contacts.row('МТО', 'Отдел эксплуатации')
        user_markup_contacts.row('Отдел ком.учета', '/back')
        bot.send_message(message.from_user.id, 'Выберите нужный контакт', reply_markup=user_markup_contacts)
    else:
        bot.send_message(message.chat.id, constants.answer)
        log(message, constants.answer)


bot.polling(none_stop=True, interval=0)