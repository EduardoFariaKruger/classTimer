from datetime import datetime
from datetime import date
import time
import webbrowser

current_time = str()
deactivator = False
today = date.today()
time1 = datetime(year=today.year, month=today.month, day=today.day, hour=11, minute=52, second=30)
now = datetime

hr1 = datetime.strftime(time1, "%H,%M,%S")
def SetTime():
    time.sleep(1)
    timeNow = datetime.now()
    now = datetime.strftime(timeNow, "%H,%M,%S")
    return now

while deactivator == False:
    now = SetTime()
    print(now)
    print(type(now))
    print(type(hr1))
    if now == hr1:
        webbrowser.open("https://github.com/EduardoFariaKruger/classTimer")
        deactivator = True
        break
    