from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo
import time
import threading

from pyexpat.errors import messages

#Ввод библиотек

#Ввод переменных
a = 99999999 #Количество очков
b = 0  #На сколько прибавляется(автоклик)
c = 100#Цена обновления автоклика
d = 0  #Количество обновлений автоклика
e = 1  #На сколько прибавляется(клик)
f = 50 #Цена за обновление клика
g = 1  #Количество обновлений клика
h = 10  #Время автоклика
i = 500#Цена обновления времени
j = 0  #Количество обновлений времени


class Options(Toplevel):


    def __init__(options):
        super().__init__()

        options.title("Window options")
        options.geometry("400x900")
        options.attributes("-alpha", 0.7)
        options.grab_set()

        ttk.Button(options, text="Exit", command=options.ext).pack(anchor=NE)
        ttk.Button(options, text=f"Fullscreen {"On" if root.attributes("-fullscreen") else "Off"}", command=options.flscrn).pack(anchor=NW)

    def flscrn(options):
        if root.attributes("-fullscreen"):
            root.attributes("-fullscreen", False)
        else:
            root.attributes("-fullscreen", True)

    def ext(options):
        print("Закрытие окна настроек")
        options.grab_release()
        options.destroy()


def num():  #Функция по автоматическому прибавлению очков
    global a, d, h
    while True:
        if d >= 1:
            time.sleep(h/10)
            a += b #Прибаление очков
            label1["text"] = a #Изменение текста на счётчике
def exit():  #Функция для выхода
    result = askyesno(title="Подтверждение выхода", message="Точно выйти?")
    if result: print("Выход"); root.destroy()
def update():#Функция отвечающая за обновления
    global a, b, c, d
    if a >= c:
        a -= c #Вычитание цены из кол-ва очков
        b += 1 #Прибавление к ежесекундной прибавке очков
        d += 1 #Общее кол-во обновление +1
        c *= 2 #Увеличение цены
        Button1["text"] = f"Update(autoclick) - {c}" #Изменение текста на кнопке обновления
        label1["text"] = a  # Изменение текста на счётчике
def click(): #Функция отвечающая за клик
    global a, e
    a += e
    label1["text"] = a
    label2["text"] = f"AutoClick - {d} ( +{b}; {h/10}sec ); Click - {g}( +{e} )" #Обновление информации о доходе
def updk():
    global a, e, f, g
    if a >= f:
        a -= f
        e += 1
        f *= 2
        g += 1
        Button3["text"] = f"Update(click) - {f}"
        label1["text"] = a  # Изменение текста на счётчике
def updt():
    global a, h, i, j, b
    if a >= i:
        a -= i
        i *= 2
        if h <= 1:
            b += 1
            h /= 10
        elif h > 1:
            h -= 1
        j += 1
        label1["text"] = a
        Button4["text"] = f"Update time autoclick - {i}"
def opt():
    Options()
    print("Открытие окна настроек")

thread = threading.Thread(target=num, daemon=True)
thread.start() #Автоматическое параллельное прибавление очков(включение парралельности)

root = Tk()
root.minsize(1000,500)
root.attributes("-fullscreen", True)  #Включение полного экрана
root.attributes("-alpha", 1)   #Полупрозрачность окна

root.title("Dark Axe 3K")     #Название окна
icon = PhotoImage(file="img.png")#Переменная иконки окна
root.iconphoto(True, icon)#Подключение иконки окна

exitB = ttk.Button(text="Exit", command=exit)
exitB.pack(anchor="ne")#Добавление кнопки выхода(+расположение)
Button4 = ttk.Button(text="Options", command=opt)
Button4.pack(anchor=NE)#Добавление кнопки настроек
label1 = ttk.Label(text=a)
label1.place(relx=.5, rely=.5, anchor="center")#Добавление счётчика очков(+расположение)
Button3 = ttk.Button(text=f"Update click! - {f}", command=updk)
Button3.pack(anchor=NW)#Добавление кнопки улучшения клика
Button1 = ttk.Button(text=f"Buy autoclick!! - {c}", command=update)
Button1.pack(anchor=NW)#Добавление кнопки улучшения автоклика
Button4 = ttk.Button(text=f"Update time autoclick - {i}", command=updt)
Button4. pack(anchor=NW)#Добавление кнопки улучшения времени автоклика
Button2 = ttk.Button(text="Click", command=click)
Button2.place(relx=.5, rely=.6, anchor="center")#Добавление кнопки клика
label2 = ttk.Label(text=f"AutoClick - {d} ( +{b}; {h/10}sec ); Click - {g}( +{e} )")
label2.place(relx=.5, rely=.55, anchor="center")#Добавление информации о доходе

root.mainloop()