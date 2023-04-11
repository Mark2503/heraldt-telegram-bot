import datetime
import calendar

from threading import Thread

date = datetime.datetime.now().strftime('%Y:%m:%d').split(':')

year, month, days = int(date[0]), int(date[1]), int(date[2])


# Оповещение за неделю
def weekly_notification():

    text = 'Через неделю будет вечеря Господня'
    # список для хранения индексов число месяца дня недели
    result = list()

    try:
        for day in calendar.Calendar().itermonthdays2(year, month):

            if day[1] == 6:
                result.append(day[0])

        return text if result[-1] == 0 else text

    except Exception as e:
        return e


# Оповещение за день
def notification_for_the_day():

    text = 'Завтра будет вечеря Господня'
    # список для хранения индексов число месяца дня недели

    result = list()

    try:
        for day in calendar.Calendar().itermonthdays2(year, month):

            if day[1] == 5:
                result.append(day[0])

        if result[0] == 0:
            return text

        elif result[0] == days:
            return text

    except Exception as e:

        return e





