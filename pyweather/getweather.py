#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib, json
import urllib.request
from tkinter import *

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = 'e847eb3ef3b7c01883912d77994cca6b'

def callweather():
	textLable = Label(frame1, text=())
	easapedQuery = e.get()
	url = BASE_URL+'?APPID='+API_KEY+'&units=metric&q='+easapedQuery
	res_data = urllib.request.urlopen(url).read()

	mainDict = json.loads(res_data)
	weatherList = mainDict['weather']
	weatherDict = weatherList[0]
	city = mainDict['name']
	currentTemp = mainDict['main']['temp']

	conditions = weatherList[0]['main']
	if conditions == 'Clear':
		con = '多云'
	elif conditions == 'Rain':
		con = '有雨'
	else:
		con = conditions
	textLable = Label(frame1, text=(city,'今日天气',currentTemp,'℃',con))
	textLable.grid(row=0, column=0)
	return e.get()

root = Tk()
root.title('天气预报')
frame1 = Frame(root)
frame2 = Frame(root)
v1 = StringVar()

b1=Button(root, text='查询城市',padx= 20, command=callweather)
b1.grid(row=1, column=1)
e = Entry(root, textvariable=v1)
e.grid(row=1, column=0, padx=0)

theButton = Button(frame2, text='退出', command=root.quit)
theButton.grid(row=1, column=0)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

mainloop()


