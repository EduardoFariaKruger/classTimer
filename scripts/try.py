from datetime import datetime
from datetime import date
import time
import webbrowser

current = date.today()
aula1 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=00), "%H,%M,%S")
aula2 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=10), "%H,%M,%S")
aula3 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=15), "%H,%M,%S")
aula4 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=20), "%H,%M,%S")
aula5 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=25), "%H,%M,%S")
aula6 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=30), "%H,%M,%S")
aula7 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=35), "%H,%M,%S")
lista = []
current = date.today()
dia = int()
def getCurrent():
    time.sleep(1)
    now = datetime.now()
    timeNow = datetime.strftime(now, "%H,%M,%S")
    print(timeNow)
    return timeNow
def setDay(current, dia, lista):
    dia = int(input('Que dia da semana é hoje? '))
    if dia == 1:
        alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
        link1 = 'meet.google.com/utf-egzc-gbk'
        lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
        lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
        alarm2 = datetime(year=current.year, month=current.month, day=current).
        lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
        alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
        link3 = 'meet.google.com/nze-nwkb-dut'
        lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
        lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
        return lista
lista = setDay(current, dia, lista)
c = int(0)
data = lista[0]
link = lista[1]
print(data, link)
print(lista)