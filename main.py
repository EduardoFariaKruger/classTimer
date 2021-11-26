from datetime import datetime
import webbrowser

url = 'https://github.com/EduardoFariaKruger/classTimer'
now = datetime.now().time()

print('now =', now)
print('type(now) =', type(now))
webbrowser.open(url)
print(url)