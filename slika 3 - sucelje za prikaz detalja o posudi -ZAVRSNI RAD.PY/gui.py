
from crud import get_all_users
from datetime_utils import *
from weather_api import WeatherForecast
from main import session
from tkinter.ttk import Entry
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from random import randint



root = tk.Tk()
root.title('Algebra | PyPosuda')
root.configure(bg='#282828')  # tamno siva pozadina

root.geometry('800x700')

frame = tk.Frame(root, width=600, height=600)
frame.grid(column=0, row=0, padx=10, pady=5)
frame.place(anchor='e', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open('slika_1.jpg'))
label = tk.Label(frame, image=img)
label.grid(column=0, row=1, padx=10, pady=10)

sync_image = tk.Button(root, text='Sync', bg='#282828',
                       fg='white', font=('Arial', 10))
sync_image.grid(column=2, row=5, padx=5, pady=5)

moj_profil_image = tk.Button(root, text='Moj profil' ,bg='#282828', fg='white',
font=('Arial', 10))
moj_profil_image.grid(column=2, row=6, padx=5, pady=5)

naziv_posude = tk.LabelFrame(root, width=300, height=300, text='Naziv posude:',
                             bg='#282828', fg='white', font=('Arial', 10))  # Frame
naziv_posude.grid(column=0, row=0, columnspan=15, padx=15, pady=15)
naziv_posude.place(anchor='sw', relx=0.5, rely=0.5)

biljka1 = tk.Label(naziv_posude, text='BILJKA1',
                   bg='#282828', fg='white', font=('Arial', 10))
biljka1.grid(column=2, row=2, columnspan=15, padx=15, pady=15)


vlaznost_i_tempratura = tk.LabelFrame(
    root, width=300, height=300, text='Temperatura zraka i vlažnost:', bg='#282828', fg='white', font=('Arial', 10))
vlaznost_i_tempratura.grid(column=0, row=1, columnspan=15, padx=15, pady=15)
vlaznost_i_tempratura.place(anchor='nw', relx=0.5, rely=0.5)

lux_i_ph = tk.LabelFrame(root, width=400, height=200, text='PH vrijednost i LUX vrijednost:',
                         bg='#282828', fg='white', font=('Arial', 10))
lux_i_ph.grid(column=0, row=2, columnspan=15, padx=10, pady=10)
lux_i_ph.place(anchor='nw', relx=0.5, rely=0.65)


# grafovi
vrijednost_grafova = tk.LabelFrame(
    root, width=300, height=300, text='Grafovi:', bg='#282828', fg='white', font=('Arial', 10))
vrijednost_grafova.grid(column=0, row=0, columnspan=15, padx=15, pady=15)
vrijednost_grafova.place(anchor='nw', relx=0.5, rely=0)


def create_weather_frame():
    weather_frame = tk.Frame(
        vlaznost_i_tempratura, width=200, height=100, bg='#282828'
    )
    weather_frame.grid(row=0, column=2, padx=10, pady=10)

    ph_lux_frame = tk.Frame(
        lux_i_ph, width=400, height=200, bg='#282828'
    )
    ph_lux_frame.grid(row=2, column=2, padx=10, pady=10)

    def refresh_temperature():
        zagreb_forecast = WeatherForecast("zagreb")
        temperature_data = zagreb_forecast.get_formatted_weather_data()

        temperature_label.configure(
            text=f"{temperature_data['current_temperature']} °C ({temperature_data['description']})")
        humidity_label.configure(text=temperature_data['humidity'])

    def random_ph_label():
        return f"pH vrijednost: {np.random.randint(5, 10)} "

    def random_lux_label():
        return f"Razina svjetla: {np.random.randint(700, 1200)} "

    temperature_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    temperature_label.grid(row=2, column=3, padx=5, pady=5)

    humidity_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    humidity_label.grid(row=2, column=4, padx=5, pady=5)

    ph_label = tk.Label(
        ph_lux_frame, bg='#282828', fg='white', text=random_ph_label(), font=('Arial', 10)
    )
    ph_label.grid(row=1, column=5, padx=5, pady=5)

    lux_label = tk.Label(
        ph_lux_frame, bg='#282828', fg='white', text=random_lux_label(), font=('Arial', 10)
    )
    lux_label.grid(row=2, column=5, padx=5, pady=5)

    last_refresh_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    last_refresh_label.grid(row=2, column=5, padx=5, pady=5)

    refresh_temperature()

    ph_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    ph_label.grid(row=2, column=5, padx=5, pady=5)

    lux_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    lux_label.grid(row=2, column=5, padx=5, pady=5)


def graph_line():

    fig, graf = plt.subplots()
    x = range(3, 13)
    y1 = np.random.randn(10)
    y2 = np.random.randn(10)
    y3 = np.random.randn(10)
    y4 = np.random.randn(10)

    plt.title('Podatci', fontsize=14)
    plt.xlabel('Senzor', fontsize=14)
    plt.ylabel('Vrijednosti', fontsize=14)
    plt.grid(True)

    plt.plot(x, y1, 'b', linestyle='dashed')
    plt.plot(x, y2, 'r')
    plt.plot(x, y3, 'g', linestyle='dotted')
    plt.plot(x, y4, 'g')
    plt.show()


graf1 = tk.Button(vrijednost_grafova, text='Line', bg='#282828',
                  fg='white', font=('Arial', 10), command=graph_line)
graf1.grid(column=2, row=2, columnspan=15, padx=15, pady=15)


def graph_hist():

    vrijednost_senzora = np.random.normal(1, 100, 10)
    plt.hist(vrijednost_senzora, 4)
    w = 0.4
    x = [-2, -1, 0, 1, 2]
    plt.bar(x, w)
    plt.show()


graf2 = tk.Button(vrijednost_grafova, text='Histogram', bg='#282828',
                  fg='white', font=('Arial', 10), command=graph_hist)
graf2.grid(column=2, row=3, columnspan=15, padx=15, pady=15)


def graph_pie():

    ''''def graph_scater():

    x = range(50)
    y = range(50) + np.random.randint(0, 30, 50)
    plt.scatter(x, y)
    plt.rcParams.update({'figure.figsize': (10, 8), 'figure.dpi': 100})
    plt.title('Podaci')
    plt.xlabel('Senzor')
    plt.ylabel('Vrijednosti')
    plt.show()


graf3 = tk.Button(vrijednost_grafova, text='Scater', bg='#282828',
                  fg='white', font=('Arial', 10), command=graph_scater)
graf3.grid(column=2, row=4, columnspan=15, padx=15, pady=15)'''


    y = np.random.randint(18, size=(4))
    colors = [
        "violet", # colours
        'purple', 
        "black",  
        "grey",       
     
        ]

    plt.figure(figsize=(10, 5))
    plt.pie(y, colors=colors)
    plt.show()


'''my_button=Button(root, text='Graficki prikaz', command=graph_pie, bg='#282828', fg='white')
my_button.pack()'''


graf3 = tk.Button(vrijednost_grafova, text='Pie', bg='#282828',
                  fg='white', font=('Arial', 10), command=graph_pie)
graf3.grid(column=2, row=4, columnspan=15, padx=15, pady=15)





create_weather_frame()


root.mainloop()
