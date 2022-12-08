import tkinter as tk
from tkinter.ttk import Entry
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = tk.Tk()
root.title('PyFlora Posude')




def create_prijavi_me():
    new_prijavi_me_window = tk.Toplevel(root)
    new_prijavi_me_window('Moj profil')
    new_prijavi_me_window.focus()
    
    biljka_1_var = tk.StringVar()
    biljka_1_label = tk.Label(new_prijavi_me_window, text='naziv biljke 1')
    biljka_1_label.grid(row=0, column=0, padx=20, pady=20)
    biljka_1_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_1_var)
    biljka_1_entry.grid(row=0, column=1, padx=20, pady=20)

    biljka_2_var = tk.StringVar()
    biljka_2_label = tk.Label(new_prijavi_me_window, text='naziv biljke 2')
    biljka_2_label.grid(row=1, column=0, padx=20, pady=20)
    biljka_2_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_2_var)
    biljka_2_entry.grid(row=1, column=1, padx=20, pady=20)

    biljka_3_var = tk.StringVar()
    biljka_3_label = tk.Label(new_prijavi_me_window, text='naziv biljke 3')
    biljka_3_label.grid(row=2, column=0, padx=20, pady=20)
    biljka_3_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_3_var)
    biljka_3_entry.grid(row=2, column=1, padx=20, pady=20)

    biljka_4_var = tk.StringVar()
    biljka_4_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_4_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_4_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_4_entry.grid(row=3, column=1, padx=20, pady=20)
    
    biljka_5_var = tk.StringVar()
    biljka_5_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_5_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_5_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_5_entry.grid(row=4, column=1, padx=20, pady=20)

    biljka_6_var = tk.StringVar()
    biljka_6_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_6_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_6_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_6_entry.grid(row=5, column=1, padx=20, pady=20)

    biljka_7_var = tk.StringVar()
    biljka_7_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_7_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_7_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_7_entry.grid(row=6, column=1, padx=20, pady=20)

    biljka_8_var = tk.StringVar()
    biljka_8_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_8_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_8_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_8_entry.grid(row=7, column=1, padx=20, pady=20)

    biljka_9_var = tk.StringVar()
    biljka_9_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_9_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_9_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_9_entry.grid(row=8, column=1, padx=20, pady=20)

    biljka_10_var = tk.StringVar()
    biljka_10_label = tk.Label(new_prijavi_me_window, text='naziv biljke 4')
    biljka_10_label.grid(row=3, column=0, padx=20, pady=20)
    biljka_10_entry = tk.Entry(new_prijavi_me_window, textvariable=biljka_4_var)
    biljka_10_entry.grid(row=9, column=1, padx=20, pady=20)



frame = tk.LabelFrame (root, width=800, height=600, text= 'Prijava') #Frame
frame.grid(column=0, row=0, padx=10, pady=10)

frame_user_name = tk.Label (frame, text= 'user name').grid(row=1) 
frame_user_name =Entry(frame)
frame_user_name.grid(column=1, row=1, padx=10, pady=10)

frame_password = tk.Label(frame, text= 'password').grid(row=2)
frame_password =Entry(frame)
frame_password.grid(column=1, row=2, padx=10, pady=10)

prijava = tk.Button(frame, text='Prijavi me', command=create_prijavi_me)
prijava.grid(column=1, row=3, padx=30, pady=30)


    



root.mainloop()