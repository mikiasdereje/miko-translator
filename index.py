# IMPORTING NEDED LIBRARY.-----------------------------------------------

import tkinter as tk
from tkinter import Button, Canvas, Entry, Tk, ttk
from googletrans import Translator, LANGUAGES
import googletrans

# DEFFINING TRANSLATION AND DESPLAYING IT.--------------------------------

def miko():
    translator = Translator()
    src_text = entry_1.get().strip()
    src_lang = [key for key, value in LANGUAGES.items() if value == e1.get()][0]
    dest_lang = [key for key, value in LANGUAGES.items() if value == e2.get()][0]

    if src_text:
        translated = translator.translate(src_text, src=src_lang, dest=dest_lang)
        entry_2.delete(0, tk.END)
        entry_2.insert(tk.END, translated.text)

#WORKING ON USER INTERFACE---------------------------------------------------

window = Tk()

window.geometry("347x556")
window.configure(bg = "#0F1F71")
window.title('miko translator')




canvas = Canvas(
    window,
    bg = "#0F1F71",
    height = 556,
    width = 347,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    347.0,
    73.0,
    fill="#4472E9",
    outline="")

canvas.create_text(
    15.0,
    31.0,
    anchor="nw",
    text="MIKO TRANSLATOR\n",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    17.0,
    90.0,
    anchor="nw",
    text="TRANSLATE FROM :",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

# IMPORTING LANGUAGE ---------------------------------------

language=googletrans.LANGUAGES
languagev=list(language.values())
lang1=language.keys()

# SELLECTBOX 1 ----------------------------------------------

e1 =ttk.Combobox(window,
    values=languagev
)
e1.place(
    x=137,
    y=85,
    width=150.0,
    height=28.0
)
e1.set("ENGLISH")

# ENTARY BOX 1 ----------------------------------------------

entry_1 = Entry(
    bd=0,
    bg="#AFEBFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20 ),
)
entry_1.place(
    x=30.0,
    y=123.0,
    width=285.0,
    height=149.0
)

canvas.create_text(
    105.0,
    292.0,
    anchor="nw",
    text="TO  : ",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

# LEST BOX 2 ------------------------------------------

e2 =ttk.Combobox(window,values=languagev)
e2.place(
    x=137.0,
    y=287.0,
    width=150.0,
    height=28.0
)
e2.set("SELECT LANGUAGE")

# ENTARY BOX 2 -------------------------------------------

entry_2 = Entry(
    bd=0,
    bg="#AFEBFF",
    fg="#000716",
    highlightthickness=0,
    font=("bold",20),
)
entry_2.place(
    x=30.0,
    y=330.0,
    width=285.0,
    height=151.0
)

# BUTTON -------------------------------------------------

button_1 = Button(
    bd=5,bg="#4A809E",
    activebackground="#4A809E",
    text="TRANSLATE",
    command=miko
)
button_1.place(
    x=44.0,
    y=504.0,
    width=258.0,
    height=31.0
)

# SET A TEXT IN THE TWO LIST BOX ---------------------------

e1.set("select language")
e2.set("select language")
window.resizable(False, False)


window.mainloop()
