import requests

s_city="MOSCOW, RU"
appid="95cef399101e88272f9bda3a8c33cc96"

res=requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q':s_city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print("Город",s_city)
print("Погодные условия",data['weather'][0]['description'])
print("Температура", data['main']['temp'])
print("Мин. температура",data['main']['temp_min'])
print("Макс. температура",data['main']['temp_max'])
print("Скорость ветра",data['wind']['speed'])
print("Видимость",data['visibility'])

print("___________________________________")
print("___________________________________")
print("___________________________________")


res=requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q':s_city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print("Прогноз погоды на неделю")
for i in data['list']:
    print("Дата<",i['dt_txt'],">\r\nТемпература<",'{0:+3.0f}'.format(i['main']['temp']),">\r\nПогодные условия<", format(i['weather'][0]['description']),">r\nВидимость<", format(i['visibility']),">\r\nСкорость ветра<", format(i['wind']['speed']),">")
    print("___________________________________")
