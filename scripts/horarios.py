from datetime import datetime
from datetime import date
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

a = True
lista = []
current = date.today()
currentDay = datetime.strftime(current, "%A")

aula1 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=8, minute=30, second=00), "%H,%M,%S")
aula2 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=00, second=00), "%H,%M,%S")
aula3 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=9, minute=30, second=00), "%H,%M,%S")
aula4 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=10, second=00), "%H,%M,%S")
aula5 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=10, minute=40, second=00), "%H,%M,%S")
aula6 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=13, minute=30, second=00), "%H,%M,%S")
aula7 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=14, minute=00, second=00), "%H,%M,%S")
aula8 = datetime.strftime(datetime(year=current.year, month=current.month, day=current.day, hour=15, minute=10, second=00), "%H,%M,%S")

historia = ''
geografia = ''
portugues = ''
ingles = ''
matematica = ''
marketing = ''
contabilidade = ''
gfo = ''
fisica = ''
sociologia = ''
biologia = ''
direito = ''
filosofia = ''
quimica = ''
historia = ''
edfisica = ''
espanhol = ''
projeto = ''

def getCurrent():
    time.sleep(1)
    now = datetime.now()
    timeNow = datetime.strftime(now, "%H,%M,%S")
    print(timeNow)
    return timeNow
def setDay():
    if currentDay == 'Monday':
        lista.append(aula1), lista.append(ingles), lista.append(aula2), lista.append(portugues), lista.append(aula4), lista.append(marketing)
        return lista
    elif currentDay == 'Tuesday':
        lista.append(aula1), lista.append(matematica), lista.append(aula3), lista.append(sociologia), lista.append(aula4), lista.append(geografia), lista.append(aula5), lista.append(ingles), lista.append(aula6), lista.append(biologia), lista.append(aula7), lista.append(direito), lista.append(aula8), lista.append(gfo)
        return lista
    elif currentDay == "Wednesday":
        lista.append(aula1), lista.append(filosofia), lista.append(aula2), lista.append(contabilidade), lista.append(aula4), lista.append(quimica)
        return lista
    elif currentDay == "Thursday":
        lista.append(aula1), lista.append(historia), lista.append(aula3), lista.append(filosofia), lista.append(aula4), lista.append(edfisica), lista.append(aula5), lista.append(sociologia), lista.append(aula6), lista.append(fisica), lista.append(aula7), lista.append(projeto), lista.append(aula8), lista.append(matematica)
        return lista
    elif currentDay == 'Friday':
        lista.append(aula1), lista.append(geografia), lista.append(aula2), lista.append(espanhol), lista.append(aula4), lista.append(portugues), lista.append(aula5), lista.append(fisica)
        return lista
lista = setDay()
c = int(0)
print(lista)
print(lista[c])
print(lista[c+1])
while c <= int(len(lista)):
    timeNow = getCurrent()
    if timeNow == lista[c]:
        webbrowser.open(lista[c+1])
        c += 2
        print(c)
    else:
        c = c
        print(c)