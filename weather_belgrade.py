from tkinter import *
import requests
import json

root = Tk()
root.title('Air Quality')
root.geometry('500x250')


url = "https://aerisweather1.p.rapidapi.com/observations/44.6585512,20.2063274"

headers = {
    'x-rapidapi-key': "314f1912c4msha88769150db9ab4p1762eejsn46bc3688eb18",
    'x-rapidapi-host': "aerisweather1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

print(response)
city = response['response']['place']['city'][:8]
temp = response['response']['ob']['tempC']
feels_like_temp = response['response']['ob']['feelslikeC']
pressure = response['response']['ob']['pressureMB']
wind = response['response']['ob']['windKPH']
visibility = response['response']['ob']['visibilityKM']
weather = response['response']['ob']['weather']


label = Label(root, text='' + 'City: ' + city + '\nTemp: ' + str(temp)+' C' + '\nReal Feel: ' + str(int(feels_like_temp))+' C' +\
 	'\nVisibility: ' + str(int(visibility * 1000))+' m' + '\nPressure: ' + str(pressure)+' mbar' +\
 	'\nWind: ' + str(wind)+' km/h' + '\nWeather: ' + weather, font=('Arial', 20))
label.pack()


root.mainloop()