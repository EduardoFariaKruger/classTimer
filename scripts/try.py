from datetime import datetime
from datetime import date
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

a = True
lista = []
dia = str()
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


diviser = int(2)
quantity = int()
def getCurrent():
    time.sleep(1)
    now = datetime.now()
    timeNow = datetime.strftime(now, "%H,%M,%S")
    print(timeNow)
    return timeNow
def setDay():
    dia = int(input('Que dia da semana é hoje? '))
    if dia == 'Monday':
        lista.append(aula1), lista.append(ingles), lista.append(aula2), lista.append(portugues), lista.append(aula4), lista.append(marketing)
        return lista
    else:
        lista.append(aula1), lista.append(ingles), lista.append(aula2), lista.append(portugues), lista.append(aula4), lista.append(marketing)
        return lista 

print(currentDay == 'Tuesday')