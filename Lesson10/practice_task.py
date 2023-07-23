import datetime

def add_time_two_weeks(time):
    time2 = datetime.timedelta(14)
    return time+time2
print(add_time_two_weeks(datetime.datetime.now()))




'''
приложение которое считает количество 
до твоего дня рождения
'''