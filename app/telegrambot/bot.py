import time

from project_conf import TELEBOT, DATETIME
from moduls.WriteReadJson import write_read_json_file, read_json_file
from moduls.GodSupper import notification_for_the_day, weekly_notification

import datetime

import telebot

bot = telebot.TeleBot(TELEBOT['token_1'])


@bot.message_handler(commands=['start', 'help'])
def start(message):

    text_message = str(message.text).split('@')[0]

    if text_message == '/start':
        read_file = read_json_file('user_data.json').values()
        while True:
            time.sleep(1)
            date = datetime.datetime.now().strftime('%H:%M:%S')

            if date == DATETIME['first_time']:

                for value in read_file:

                    if notification_for_the_day() is not None:
                        bot.send_message(chat_id=value['id'], text=notification_for_the_day())

                    if weekly_notification() is not None:
                        bot.send_message(chat_id=value['id'], text=notification_for_the_day())

            elif date == DATETIME['second_time']:

                for value in read_file:

                    if notification_for_the_day() is not None:
                        bot.send_message(chat_id=value['id'], text=notification_for_the_day())

                    if weekly_notification() is not None:
                        bot.send_message(chat_id=value['id'], text=notification_for_the_day())

    elif text_message == '/help':

        bot.send_message(message.chat.id, text='commands:\n'
                                               '/GetId\n'
                                               '/GetID_Group')


@bot.message_handler(commands=['GetId'])
def get_id_user(message):
    text_message = str(message.text).split('@')[0]
    if text_message == '/GetId':
        write_read_json_file(
            'user_data.json',
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.username,
            message.from_user.last_name
        )

    bot.send_message(message.chat.id, text='Ваш ID добавлен в систему')


@bot.message_handler(commands=['GetID_Group'])
def get_id_group(message):

    text_message = str(message.text).split('@')[0]

    if text_message == '/GetID_Group':
        write_read_json_file(
            'user_data.json',
            message.chat.id,
            message.chat.title,
            'None',
            'None'
        )
    bot.send_message(message.chat.id, text=f'ID группы {message.chat.title} добавлен в систему')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    pass

