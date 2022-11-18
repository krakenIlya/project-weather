from tkinter import *
from weatherApi import *
from tkinter import messagebox
from PIL import ImageTk, Image

# настройка окна
window = Tk()
window.geometry("1200x900")
window.title(" Akiv weather")
window.iconbitmap("ico.ico")
window.resizable(0, 0)
my_img = ImageTk.PhotoImage(Image.open("bg1.jpg"))
bgLabel = Label(image=my_img)
bgLabel.place(x = -5,y = -5)



def showWheaterNow():
	global currentWeatherLabel
	try:
		data = CurrentWeatherParser().GetCurrentWeather(str(cityEdit.get("1.0","end")).strip(), CurrentWeather)
		weather_str = "{}\n\nТемпература: {}°C\nВетер: {} км/ч\nВлажность: {}%".format(data.description, data.temp, data.wind_speed, data.humidity)
		currentWeatherLabel['font'] = ('Segoe print', 30)
		currentWeatherLabel['text'] = weather_str
	except ValueError:
		messagebox.showinfo("Ошибка", "Введенный город не найден!")
	except:
		messagebox.showinfo("Ошибка", "Проверьте подключение к интернету!")


def showForecastWheaterNow():
	global currentWeatherLabel
	try:
		data_list = ForecastWeatherParser().GetForecastWeather(str(cityEdit.get("1.0","end")).strip(), ForecastWeather)
		weather_str = "\n\n".join(["Дата: {}\n{}\nТемпература: {}°C\nВетер: {} км/ч\nВлажность: {}%".format(data.date, data.description, data.temp, data.wind_speed, data.humidity) for data in data_list])
		print(weather_str)
		currentWeatherLabel['font'] = ('Segoe print', 13)
		currentWeatherLabel['text'] = weather_str
	except ValueError:
		messagebox.showinfo("Ошибка", "Введенный город не найден!")
	except:
		messagebox.showinfo("Ошибка", "Проверьте подключение к интернету!")


# label текущая погода
currentWeatherLabel = Label(window, text = 'Погода супер!', font=('Segoe print', 25), bg = "#666a69", justify = LEFT)
currentWeatherLabel.place(x = 50, y  = 165)

# label "город"
cityLabel = Label(window, text = 'Город', font=('Segoe print', 45), justify = LEFT, bg = "black", fg = "white")
cityLabel.place(x = 50, y  = -5)

# Edit для ввода города
cityEdit = Text(window, height=0.3, width =10, font=('Segoe print', 30), bg = "black", fg = "white")
cityEdit.place(x=270, y=18)

# получить текущую погоду
currentWeatherButton = Button(text="Текущая  погода", font=('Segoe print', 19), bg = "black", fg = "white", command = showWheaterNow)
currentWeatherButton.place(x = 630, y = 18)

# # получить прогноз 4 дня
forecastWeatherButton = Button(text="Прогноз погоды", font=('Segoe print', 19), bg = "black", fg = "white", command = showForecastWheaterNow)
forecastWeatherButton.place(x = 930, y = 18)


if __name__ == "__main__":
	window.mainloop()