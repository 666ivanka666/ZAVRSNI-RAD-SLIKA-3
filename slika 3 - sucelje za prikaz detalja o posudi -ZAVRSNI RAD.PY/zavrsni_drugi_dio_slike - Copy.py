import tkinter as tk
from tkinter.ttk import Entry
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = tk.Tk()
root.title(' Posude')





root.geometry("700x500")

frame = Frame(root, width=600, height=400)
frame.grid(column=0, row=0, padx=10, pady=5)
frame.place(anchor='e', relx=0.5, rely=0.5)


img = ImageTk.PhotoImage(Image.open("ljiljan_zuta.jpg"))
label = Label(frame, image=img)
label.grid(column=0, row=1, padx=10, pady=10)
next_image = Button(root, text="Next image")
next_image.grid(column=1, row=3, padx=10, pady=10)


naziv_posude = LabelFrame (root, width=300, height=300, text= 'Naziv posude') #Frame
naziv_posude.grid(column=0, row=0, columnspan=15, padx=15, pady=15)
naziv_posude.place(anchor='sw',relx=0.5, rely=0.5)

biljka1 = Label(naziv_posude, text="BILJKA1")
biljka1.grid(column=2, row=2, columnspan=15, padx=15, pady=15)

status = LabelFrame (root, width=300, height=300, text= 'status') #Frame
status.grid(column=3, row=3, columnspan=15, padx=15, pady=15)
status.place(anchor='nw',relx=0.5, rely=0.5)


zaljevanje =[
    ('1', ' treba zaliti'),
    ('2', 'ne treba zaliti')
]
  

voda = StringVar()
voda.set('da')

for text, zaliti in zaljevanje:
    Radiobutton(status, text=text, variable=voda, value=zaljevanje).pack(anchor=W) #ancor centrira na lijevo


def clicked(value):
    my_label= Label(status, text=value)
    my_label.pack()


my_button = Button(status, text='dodati vode', command=lambda: clicked(voda.get()))
my_button.pack()


# vlaznost
#ph vrijedost
#razina svijetla
#temperatura zraka u prostoriji

#---

    



root.mainloop()