import datetime


def current_time():
    return datetime.datetime.now().strftime('%H-%M-%S-%m-%d-%Y')