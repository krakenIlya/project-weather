

from requests import get

import matplotlib.pyplot as plt

# base_url = "http://api.openweathermap.org/data/2.5/forecast?"
# key = "e5a82cc25aab76a4a063eaa840c55fbd"
# 
# complete_url = base_url + "appid=" + key + "&q=" + "Каир"
# 
# a = 0
# 
# for hour in get(complete_url).json()['list']:
#     temp = hour['main']['temp'] - 273.15
#     print(hour, end = "\n\n")
#     a += 1
# 
# print(a)


a =[ round(hour['main']['temp'] - 273.15) for hour in get("http://api.openweathermap.org/data/2.5/forecast?appid=e5a82cc25aab76a4a063eaa840c55fbd&q=Каир").json()['list'] ]
plt.show(a)