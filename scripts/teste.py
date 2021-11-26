from datetime import datetime
from datetime import date
import time
import webbrowser

lista = []
current = date.today()
a = True

alarm1 = str(datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00))
link1 = 'meet.google.com/utf-egzc-gbk'
lista.append(alarm1)
lista.append(link1)
alarm2 = str(datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=00, second=00))
link2 = 'https://meet.google.com/bhm-jtod-anb'
lista.append(alarm2)
lista.append(link2)
alarm3 = str(datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00))
link3 = 'meet.google.com/nze-nwkb-dut'
lista.append(alarm3)
lista.append(link3)

print(lista)
def getCurrent():
        time.sleep(1)
        now = datetime.now()
        timeNow = datetime.strftime(now, "%H,%M,%S")
        print(timeNow)
        return timeNow
print(type(int(len(lista)/2)))