from tkinter import *
from tkinter import ttk
import time
import threading
#Ввод библиотек

#Ввод переменных
a = 0  #Количество очков
b = 0  #На сколько прибавляется(автоклик)
c = 100#Цена обновления автоклика
d = 0  #Количесвто обновлений
e = 1  #На сколько прибавляется(клик)
f = 50 #Цена за обновление клика
g = 1
def num():  #Функция по автоматическому прибавлению очков
    global a, d
    while True:
        if d >= 1:
            time.sleep(1)
            a += b #Прибаление очков
            label1["text"] = a #Изменение текста на счётчике
def exit():  #Функция для выхода
    root.destroy()
def update():#Функция отвечающая за обновления
    global a, b, c, d
    if a >= c:
        a -= c #Вычитание цены из кол-ва очков
        b += 1 #Прибавление к ежесекундной прибавке очков
        d += 1 #Общее кол-во обновление +1
        c *= 2 #Увеличение цены
        Button1["text"] = f"Update - {c}" #Изменение текста на кнопке обновления
        label1["text"] = a  # Изменение текста на счётчике
def click(): #Функция отвечающая за клик
    global a, e
    a += e
    label1["text"] = a
    label2["text"] = f"AutoClick - {d} ( +{b} ); Click - {g}( +{e} )" #Обновление информации о доходе
def updk():
    global a, e, f, g
    if a >= f:
        a -= f
        e += 1
        f *= 2
        g += 1
        Button3["text"] = f"Update(click) - {f}"
        label1["text"] = a  # Изменение текста на счётчике

thread = threading.Thread(target=num, daemon=True)
thread.start() #Автоматическое параллельное прибавление очков(включение парралельности)

root = Tk()
root.attributes("-fullscreen", True)  #Включение полного экрана
root.attributes("-alpha", 0.5)   #Полупрозрачность окна

root.title("AxeDarkEpstein")     #Название окна
icon = PhotoImage(file="img.png")#Переменная иконки окна
root.iconphoto(True, icon)#Подключение иконки окна

exitB = ttk.Button(text="Exit", command=exit)
exitB.pack(anchor="ne")#Добавление кнопки выхода(+расположение)
label1 = ttk.Label(text=a)
label1.place(relx=.5, rely=.5, anchor="center")#Добавление счётчика очков(+расположение)
Button1 = ttk.Button(text=f"Buy autoclick!!( {c} )", command=update)
Button1.pack(anchor=NW)#Добавление кнопки улучшения автоклика
Button2 = ttk.Button(text="Click", command=click)
Button2.place(relx=.5, rely=.6, anchor="center")#Добавление кнопки клика
Button3 = ttk.Button(text=f"Update click!( {f} )", command=updk)
Button3.pack(anchor=NW)#Добавление кнопки улучшения клика
label2 = ttk.Label(text=f"AutoClick - {d} ( +{b} ); Click - {g}( +{e} )")
label2.place(relx=.5, rely=.55, anchor="center")#Добавление информации о доходе

root.mainloop()