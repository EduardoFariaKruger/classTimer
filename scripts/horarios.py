from datetime import datetime
from datetime import date
import time
import webbrowser

class Horarios:
    a = True
    lista = []
    dia = int()
    current = date.today()
    timeNow = datetime
    aula1 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=00), "%H,%M,%S")
    aula2 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=10), "%H,%M,%S")
    aula3 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=15), "%H,%M,%S")
    aula4 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=20), "%H,%M,%S")
    aula5 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=25), "%H,%M,%S")
    aula6 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=30), "%H,%M,%S")
    aula7 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=40, second=35), "%H,%M,%S")
    link1 = str
    link2 = str
    link3 = str
    link4 = str
    link5 = str
    link6 = str
    link7 = str
    alarm1 = str
    alarm2 = str
    alarm7 = str
    alarm3 = str
    alarm4 = str
    alarm5 = str
    alarm6 = str
    diviser = int(2)
    quantity = int()
    def getCurrent():
        time.sleep(1)
        now = datetime.now()
        timeNow = datetime.strftime(now, "%H,%M,%S")
        print(timeNow)
        return timeNow
    def setDay(current, dia, lista):
        dia = int(input('Que dia da semana é hoje? '))
        if dia == 1:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=4, second=00)
            link1 = 'https://classroom.google.com/w/MzEzNDE4OTc5ODgy/t/allmeet.google.com/ope-upvh-coe'
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=2, second=00)
            link2 = 'https://meet.google.com/bhm-jtod-anb'
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = 'meet.google.com/nze-nwkb-dut'
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            return lista
        elif dia == 2:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
            link1 = 'meet.google.com/wvj-vkzx-fjp'
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=30, second=00)
            link2 = 'https://meet.google.com/dwf-txfd-ixc'
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = 'https://meet.google.com/okv-gzxk-sim'
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            alarm4 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00)
            link4 = 'meet.google.com/utf-egzc-gbk'
            lista.append(datetime.strftime(alarm4, "%H,%M,%S"))
            lista.append(link4)
            alarm5 = datetime(year=current.year, month=current.month, day=current.day, hour=13, minute=30, second=00)
            link5 = 'meet.google.com/ryh-kovi-big'
            lista.append(datetime.strftime(alarm5, "%H,%M,%S"))
            lista.append(link5)
            alarm6 = datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=00, second=00)
            link6 = 'meet.google.com/iog-bxfv-eas'
            lista.append(datetime.strftime(alarm6, "%H,%M,%S"))
            lista.append(link6)
            alarm7 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=10, second=00)
            link7 = 'http://meet.google.com/zzm-aqps-eab'
            lista.append(datetime.strftime(alarm7, "%H,%M,%S"))
            lista.append(link7)
            return lista
        elif dia == 3:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
            link1 = 'https://meet.google.com/smz-rzhc-hhe'
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=00, second=00)
            link2 = 'https://meet.google.com/vnh-cvij-tac'
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = 'https://meet.google.com/vnh-cvij-tac'
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            return lista
        elif dia == 4:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=50, second=00)
            link1 = 'https://classroom.google.com/w/MzEzNDE4OTc5ODgy/t/allmeet.google.com/ope-upvh-coe'
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=30, second=00)
            link2 = 'https://meet.google.com/smz-rzhc-hhe'
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = 'https://meet.google.com/kow-uwok-gbg'
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            alarm4 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00)
            link4 = 'https://meet.google.com/dwf-txfd-ixc'
            lista.append(datetime.strftime(alarm4, "%H,%M,%S"))
            lista.append(link4)
            alarm5 = datetime(year=current.year, month=current.month, day=current.day, hour=13, minute=30, second=00)
            link5 = 'meet.google.com/zzh-qpzc-tjd'
            lista.append(datetime.strftime(alarm5, "%H,%M,%S"))
            lista.append(link5)
            alarm6 = datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=00, second=00)
            link6 = 'meet.google.com/kgh-ozmv-nbo'
            lista.append(datetime.strftime(alarm6, "%H,%M,%S"))
            lista.append(link6)
            alarm7 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=10, second=00)
            link7 = 'meet.google.com/wvj-vkzx-fjp'
            lista.append(datetime.strftime(alarm7, "%H,%M,%S"))
            lista.append(link7)
            return lista
        elif dia == 5:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
            link1 = 'https://meet.google.com/okv-gzxk-sim'
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=00, second=00)
            link2 = 'meet.google.com/ueu-hexs-yzk'
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = 'https://meet.google.com/bham-jtod-anb'
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            alarm4 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00)
            link4 = 'meet.google.com/zzh-qpzc-tjd'
            lista.append(datetime.strftime(alarm4, "%H,%M,%S"))
            lista.append(link4)
            return lista[alarm1, link1, alarm2, link2, alarm3, link3, alarm4, link4]
    lista = setDay(current, dia, lista)
    c = int(0)
    print(lista)
    print(lista[c])
    print(lista[c+1])
    while c <= int(len(lista)/2):
        timeNow = getCurrent()
        if timeNow == lista[c] or timeNow == aula2 or timeNow == aula3 or timeNow == aula4 or timeNow == aula5 or timeNow == aula6 or timeNow == aula7:
            webbrowser.open(lista[c+1])
            c += 1
            print(c)
        else:
            c = c
            print(c)

        