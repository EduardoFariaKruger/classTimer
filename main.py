from datetime import datetime
import time
import webbrowser

current_time = str()
deactivator = False
time1 = datetime(year=2021, month=11, day=25, hour=23, minute=17, second=0)
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
    if now == hr1:
        webbrowser.open("https://github.com/EduardoFariaKruger/classTimer")
        deactivator = True
        break
    