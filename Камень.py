from tkinter import *
import random as rdm

#4 - Функция для нажатия кнопок
def btn_click(x):
        global win, drow, lose, iso #iso обязательно глобальная    
        comp_choise = rdm.randint(1, 3) #выбор компа
        
        if comp_choise == 1: #рисуем предметы, которые выбрал комп
            iso=PhotoImage(file="1.gif")
            im = Label(root, image=iso)
            im.place(x=150, y=200)
        elif comp_choise == 2:
            iso=PhotoImage(file="2.gif")
            im = Label(root, image=iso)
            im.place(x=150, y=200)
        else:
            iso=PhotoImage(file="3.gif")
            im = Label(root, image=iso)
            im.place(x=150, y=200)          
        
        if x == comp_choise:
            drow += 1 
            lbl.configure(text="Ничья")
        elif x == 1 and comp_choise == 2 \
                or x == 2 and comp_choise == 3 \
                or x == 3 and comp_choise == 1:
            win += 1
            lbl.configure(text="Победа")
        else:
            lose += 1
            lbl.configure(text="Проигрыш")
        lb2.configure(text=f"Побед: {win}\nПроигрышей:"
                              f" {lose}\nНичей: {drow}")
       
root = Tk() #1 - Создаем окно
root.geometry("500x500")
root.title("Камень, ножницы, бумага")
root.resizable(False, False)
root["bg"] = "#FFF"

#2 - Создаем кнопки
btn1 = Button(root, text="Камень", font=("Times New Roman", 15),
                      command=lambda x=1: btn_click(x))
btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15), bg='pink', fg='blue',
                      command=lambda x=2: btn_click(x))
btn3 = Button(root, text="Бумага", font=("Times New Roman", 15),
                      command=lambda x=3: btn_click(x))
btn1.place(x=15, y=100, width=120, height=50)
btn2.place(x=160, y=100, width=120, height=50)
btn3.place(x=305, y=100, width=120, height=50)

#3 - Создаем надписи
lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
lbl.place(x=150, y=25)
win = drow = lose = 0
lb2 = Label(root, justify="left", font=("Times New Roman", 13),
                         text=f"Побед: {win}\nПроигрышей: {lose}\nНичей: {drow}",
                         bg="#FFF")
lb2.place(x=5, y=5)
lb3 = Label(root, text="Выбор ИИ:", bg="#FFF", font=("Times New Roman", 14, "bold"))
lb3.place(x=5, y=250)

root.mainloop()
