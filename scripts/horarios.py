from datetime import datetime
from datetime import date
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

class Horarios:
    a = True
    driver = webdriver.Firefox('/usr/local/bin')
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
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=38, second=30)
            link1 = ''
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=2, second=00)
            link2 = ''
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = ''
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            return lista
        elif dia == 2:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
            link1 = ''
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=30, second=00)
            link2 = ''
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = ''
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            alarm4 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00)
            link4 = ''
            lista.append(datetime.strftime(alarm4, "%H,%M,%S"))
            lista.append(link4)
            alarm5 = datetime(year=current.year, month=current.month, day=current.day, hour=13, minute=30, second=00)
            link5 = ''
            lista.append(datetime.strftime(alarm5, "%H,%M,%S"))
            lista.append(link5)
            alarm6 = datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=00, second=00)
            link6 = ''
            lista.append(datetime.strftime(alarm6, "%H,%M,%S"))
            lista.append(link6)
            alarm7 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=10, second=00)
            link7 = ''
            lista.append(datetime.strftime(alarm7, "%H,%M,%S"))
            lista.append(link7)
            return lista
        elif dia == 3:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
            link1 = ''
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=00, second=00)
            link2 = ''
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = ''
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            return lista
        elif dia == 4:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=50, second=00)
            link1 = ''
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=30, second=00)
            link2 = ''
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = ''
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            alarm4 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00)
            link4 = ''
            lista.append(datetime.strftime(alarm4, "%H,%M,%S"))
            lista.append(link4)
            alarm5 = datetime(year=current.year, month=current.month, day=current.day, hour=13, minute=30, second=00)
            link5 = ''
            lista.append(datetime.strftime(alarm5, "%H,%M,%S"))
            lista.append(link5)
            alarm6 = datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=00, second=00)
            link6 = ''
            lista.append(datetime.strftime(alarm6, "%H,%M,%S"))
            lista.append(link6)
            alarm7 = datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=10, second=00)
            link7 = ''
            lista.append(datetime.strftime(alarm7, "%H,%M,%S"))
            lista.append(link7)
            return lista
        elif dia == 5:
            alarm1 = datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00)
            link1 = '
            lista.append(datetime.strftime(alarm1, "%H,%M,%S"))
            lista.append(link1)
            alarm2 = datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=00, second=00)
            link2 = ''
            lista.append(datetime.strftime(alarm2, "%H,%M,%S"))
            lista.append(link2)
            alarm3 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00)
            link3 = ''
            lista.append(datetime.strftime(alarm3, "%H,%M,%S"))
            lista.append(link3)
            alarm4 = datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00)
            link4 = ''
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
            driver.get(lista[c+1])
            button = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]')
            button.click()
            c = c + 1
            print(c)
        else:
            c = c
            print(c)

        