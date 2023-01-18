from datetime import datetime

class Time(object):
    """represents the time of day.
    attributes: hour, minute, second"""

#Exercise 16.1
def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour,time.minute,time.second))

#Exercise 16.2
def is_after(t1,t2):
    return (t1.hour>t2.hour) or (t1.hour==t2.hour and (t1.minute>t2.minute or (t1.minute==t2.minute and t1.second>t2.second)))

#Exercise 16.3
def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.minute += time.second/60
        time.second = time.second%60
    if time.minute >= 60:
        time.hour += time.minute/60
        time.minute = time.minute/60

#Exercise 16.4
def increment2(time, seconds):
    res = Time()
    res.second = time.second + seconds
    res.minute = time.minute
    res.hour = time.hour
    if res.second >= 60:
        res.minute += res.second/60
        res.second = res.second%60
    if res.minute >= 60:
        res.hour += res.minute/60
        res.minute = res.minute/60
    return res
start = Time()
start.hour = 9
start.minute = 45
start.second = 0
increment(start, 1132)
print_time(start)

#Exercise 16.5
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
def increment3(time,seconds):
    return int_to_time(time_to_int(time) + seconds)

#Exercise 16.6
def mul_time(time,number):
    return int_to_time(time_to_int(time)*number)

def pace(time,distance):
    return mul_time(time,1/distance)

#Exercise 16.7
class Date(object):
    """repredent the date
    attributes:
    year,month,day
    """
def date_to_days(date):
    res = date.day
    month = date.month - 1
    year = date.year
    while month != 0:
        if month in [1,3,5,7,8,10,11]:
            res += 31
        elif month != 2:
            res+= 30
        else:
            if year%4 == 0 and ((year%100==0 and year%400==0) or year%100!=0):
                res += 29
            else:
                res += 28
        month = month-1
    return (year,res)
def days_to_date(year,days):
    months = 0
    d = days
    y = year
    if year%4 == 0 and ((year%100==0 and year%400==0) or year%100!=0):
        l = 29
    else:
        l = 28
    while(d>30):
        for i in [31,l,31,30,31,30,31,31,30,31,30,31]:
            if d<i:
                break
            else:
                months += 1
                d = d-i
    y += months/12
    months = months%12
    date = Date()
    date.year = y
    date.month = months
    date.day = d
    return date
def increment_date(date,n):
    temp = Date()
    temp.year = date.year
    temp.month = date.month
    temp.day = date.day + n
    (year,days) = date_to_days(temp)
    res = days_to_date(year,days)
    return res
def print_date(date):
    print("%d/%.2d/%.2d" %(date.day,date.month,date.year))

#Exercise 16.8
#1
def current_day():
    today = datetime.now().date()
    weekday = today.weekday()
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print('today is '+week[weekday])
#2
def age(date):
    today = datetime.now().date()
    day = today.day 
    month = today.month
    year = today.year
    age  = Date()
    if month in [4,6,9,11]:
        age.day = 30 - abs(day - date.day)
    if month == 2:
        if year%4 == 0 and ((year%100==0 and year%400==0) or year%100!=0):
            age.day = 29 - abs(day - date.day)
        else:
            age.day = 28 - abs(day - date.day)
    else:
        age.day = 31 - abs(day - date.day)
    age.month = 12 - abs(month - date.month - 1)
    age.year = year - date.year - 1
    print("Your age is: %d years,%d months,and %s days."%(age.year,age.month,age.day))
    (year,n) = date_to_days(date)
    (year,n2) = date_to_days(today)
    next_birth = days_to_date(0,abs(n - n2))
    next_birth.day = next_birth.day - 1
    hour = 11 - datetime.now().hour
    minute = 59 - datetime.now().minute
    seconds = 60 - datetime.now().second
    print("Your next birthday is in:%d months,%d days,%d hours,%d minutes,%d seconds"%(next_birth.month,next_birth.day,hour,minute,seconds))
birthday = Date()
birthday.year = 2004
birthday.month = 2
birthday.day = 22
age(birthday)