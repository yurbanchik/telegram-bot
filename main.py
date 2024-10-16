import telebot
import os
from telebot import types

bot = telebot.TeleBot(os.environ.get("TOKEN"))
file_id_1 = "BAACAgIAAxkBAAICb2cPe-og9d_EDpfgeZA_NEIqV4JPAAKlWQACpEl5SOUCglxclCZENgQ"
file_id_2 = "BAACAgIAAxkBAAICcGcPfFmn3qPdEscq-m-BAAFjKnF6mAACp1kAAqRJeUhWA-NTy39Z3DYE"
file_id_3 = "BAACAgIAAxkBAAICcWcPfObK_IIyNh3okzsY0sJ7cUOfAAKrWQACpEl5SCKpYrzTaSeGNgQ"
file_id_4 = "BAACAgIAAxkBAAICcmcPfcWJRcFZyrmjLPV8vX0XOgNBAAKwWQACpEl5SMe30PY8VX7INgQ"
file_id_5 = "BAACAgIAAxkBAAICc2cPff0hyGPH10y5m_B1Rp9hsSTTAAK2WQACpEl5SB0BpAtJS3i6NgQ"
file_id_6 = "BAACAgIAAxkBAAICdGcPfli-tEQLqYkImyyxY_sCz3MgAAK6WQACpEl5SI6Uz8DLxyNeNgQ"
file_id_7 = "BAACAgIAAxkBAAICdWcPfoUKbcx-UDCDKJzivNou4MZPAAK8WQACpEl5SD0r6RMcCxRfNgQ"

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()

    if callback.data == 'introductory-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='watch-first-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '▶Для вас готовы 5 уроков с теорией и бонусный урок с практикой. Начнем!⬇')
        bot.send_video(callback.message.chat.id, file_id_1, reply_markup=markup)

    elif callback.data == 'watch-first-video':
        btn = types.InlineKeyboardButton('Перейти к следующему уроку', callback_data='first-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Отлично!👍 Теперь сделайте практическое задание по этому уроку. Когда будете готовы, нажмите на кнопку "Перейти к следующему уроку"',
                         reply_markup=markup)

    elif callback.data == 'first-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='watch-second-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '✏Теперь мы перейдем к Уроку 1. Вы узнаете, откуда получаете деньги и куда тратите, и выберете проекты, по которым будете вести учет.')
        bot.send_video(callback.message.chat.id, file_id_2, reply_markup=markup)

    elif callback.data == 'watch-second-video':
        btn = types.InlineKeyboardButton('Перейти к следующему уроку', callback_data='second-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Отлично!👍 Теперь сделайте практическое задание по этому уроку. Когда будете готовы, нажмите на кнопку "Перейти к следующему уроку"',
                         reply_markup=markup)

    elif callback.data == 'second-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='watch-third-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '✏Теперь мы перейдем к Уроку 2, где разберем ведомости поступлений и платежей.')
        bot.send_video(callback.message.chat.id, file_id_3, reply_markup=markup)

    elif callback.data == 'watch-third-video':
        btn = types.InlineKeyboardButton('Перейти к следующему уроку', callback_data='third-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Отлично!👍 Теперь сделайте практическое задание по этому уроку. Когда будете готовы, нажмите на кнопку "Перейти к следующему уроку"',
                         reply_markup=markup)

    elif callback.data == 'third-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='watch-forth-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '✏Теперь мы перейдем к Уроку 3, где поймете, сколько вы реально получили денег в месяц и сколько вы потратили.')
        bot.send_video(callback.message.chat.id, file_id_4, reply_markup=markup)

    elif callback.data == 'watch-forth-video':
        btn = types.InlineKeyboardButton('Перейти к следующему уроку', callback_data='forth-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Отлично!👍 Теперь сделайте практическое задание по этому уроку. Когда будете готовы, нажмите на кнопку "Перейти к следующему уроку"',
                         reply_markup=markup)

    elif callback.data == 'forth-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='watch-fifth-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '✏Теперь мы перейдем к Уроку 4, где вы узнаете, сколько вы реально заработали в этом месяце.')
        bot.send_video(callback.message.chat.id, file_id_5, reply_markup=markup)

    elif callback.data == 'watch-fifth-video':
        btn = types.InlineKeyboardButton('Перейти к следующему уроку', callback_data='fifth-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Отлично!👍 Теперь сделайте практическое задание по этому уроку. Когда будете готовы, нажмите на кнопку "Перейти к следующему уроку"',
                         reply_markup=markup)

    elif callback.data == 'fifth-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='watch-last-video')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '✏Теперь мы перейдем к завершающему уроку и увидим результат работы.')
        bot.send_video(callback.message.chat.id, file_id_6, reply_markup=markup)

    elif callback.data == 'watch-last-video':
        btn1 = types.InlineKeyboardButton('Получить шаблон для заполнения', url='https://docs.google.com/spreadsheets/d/1bRH70a33U8rBZ9gGLFMztwqwkmIx1EqrOiWgRe5r9oQ/edit?usp=sharing')
        btn2 = types.InlineKeyboardButton('Получить пример заполнения', url='https://docs.google.com/spreadsheets/d/1QCJWJlJNf_8FF8nDAd4E5w4QrPS8Yiy0Hv1-560xStY/edit?usp=sharing')
        btn3 = types.InlineKeyboardButton('Перейти к следующему уроку', callback_data='last-video')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)

        bot.send_message(callback.message.chat.id,
                         'Отлично!👍 Вы завершили обучение. Поздравляю вас с вашими достижениями в финансах. У меня для вас есть полезные материалы в подарок, скорее забирайте их и переходите к заключительной части',
                         reply_markup=markup)

    elif callback.data == 'last-video':
        btn = types.InlineKeyboardButton('Я посмотрел', callback_data='congratulation')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         '✏Вы отлично справились с предыдущими уроками! Теперь давай перейдем к заключительному уроку.')
        bot.send_video(callback.message.chat.id, file_id_7, reply_markup=markup)


    elif callback.data == 'congratulation':
        btn = types.InlineKeyboardButton('Продолжить', callback_data='main')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Поздравляю с завершением курса!🎉 Сделайте финальное практическое задание, и мы обсудим ваши результаты👌.',
                         reply_markup=markup)

    elif callback.data == 'main':
        btn1 = types.InlineKeyboardButton('Записаться через WhatsApp', url='https://wa.me/79069495847')
        btn2 = types.InlineKeyboardButton('Записаться через Telegram', url='https://t.me/tatiana_butakova')
        btn3 = types.InlineKeyboardButton('Нет вопросов', callback_data='feedback')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.send_message(callback.message.chat.id,
                         'Спасибо за участие в курсе!🎉 Теперь у вас есть базовое понимание состояния вашего бизнеса в цифрах!\n\n❓Остались вопросы? Что-то оказалось сложно или непонятно? Или всё-таки решили не заниматься учётом сами? ✏Запишитесь на безоплатную консультацию на 30-40 минут от Татьяны Бутаковой',
                         reply_markup=markup)

    elif callback.data == 'feedback':
        btn = types.InlineKeyboardButton('Оставить отзыв', url='https://forms.yandex.ru/u/66f2daa3d04688166975cf21')
        markup.add(btn)

        bot.send_message(callback.message.chat.id,
                         'Отлично! Оставь свой отзыв и пожелания, чтоб я могла улучшить курс, это очень важно для меня! В подарок я предложу тебе бонус😉',
                         reply_markup=markup)

    elif callback.data == 'show-info':
        btn1 = types.InlineKeyboardButton('Подписаться на канал', url='https://t.me/butakovatochkisoznaniya')
        btn2 = types.InlineKeyboardButton('Подписаться на аккаунт', url='https://www.instagram.com/butakova.ts?igsh=MTRqYTc0NTlpeTU1cA==')
        btn3 = types.InlineKeyboardButton('Вернуться к урокам', callback_data='begin')
        markup.row(btn1, btn2)
        markup.row(btn3)

        bot.send_message(callback.message.chat.id, 'Хорошо, понимаю👌. Возвращайтесь, когда будете готовы😉, и нажмите "Вернуться к урокам"▶. А пока подпишитесь на канал 📍"Точки сознания Татьяны Бутаковой" и аккаунт.', reply_markup=markup)

    elif callback.data == 'begin':
        btn = types.InlineKeyboardButton('Начать', callback_data='introductory-video')
        markup.add(btn)
        bot.send_message(callback.message.chat.id,f'{callback.message.chat.first_name}, рада вас снова видеть😊! Готовы погрузиться в мир финансового анализа? Начнем с вводного урока!⬇', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Продолжить', callback_data='introductory-video')
    btn2 = types.InlineKeyboardButton('Позже', callback_data='show-info')
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, '📌Добро пожаловать на мини-курс “Управленка за 2 часа” от консалтинговой компании “Масштаб”!', reply_markup=markup)

bot.polling(none_stop=True)