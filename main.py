# l1 = [1,2,3,4,5,6] #dostepne monety
# l3 = [1,5,6] #wydane monety
#
#
# for el in l1:
#     if el in l3:
#         l1.remove(el)
#
#
#
#
# from tkinter import *
# window = Tk()
# window.geometry('350x300')
# l= Label(window, text="Wybierz rodzaj biletu")
# l.place(x=0, y=0)
#
# #przyciski od biletow
# b1 = Button(window, text = 'bilet 20 minut ulgowy', width=20)
# b1.place(x=0,y=20)
# b2 = Button(window, text = 'bilet 20 minut normalny', width=20)
# b2.place(x=0,y=45)
# b3 = Button(window, text = 'bilet 40 minut ulgowy', width=20)
# b3.place(x=0,y=70)
# b4 = Button(window, text = 'bilet 40 minut normalny', width=20)
# b4.place(x=0,y=95)
# b5 = Button(window, text = 'bilet godzinny ulgowy', width=20)
# b5.place(x=0,y=120)
# b6 = Button(window, text = 'bilet godzinny normalny', width=20)
# b6.place(x=0,y=145)
#
# l1= Label(window, text='Wrzuc pieniadze')
# l1.place(x= 200, y=0)
#
# monety= [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]
# i=0
#
# for nominal in monety:
#     p = Button(window, text = str(nominal), width=5)
#     p.place(x=200, y = y1)
#     y1 += 25
#
# banknoty = [10,20,50,100]
# j=0
# y2=20
# for nominal in banknoty:
#     p = Button(window, text = str(nominal), width=5)
#     p.place(x=245, y = y2)
#     y2 += 25
#
#
# przyciski od monet
#
# p1 = Button(window, text = '1gr',width=5)
# p1.place(x=200, y=20)
# p2 = Button(window, text = '2gr',width=5)
# p2.place(x=200, y=45)
# p3 = Button(window, text = '5gr',width=5)
# p3.place(x=200, y=70)
# p4 = Button(window, text = '10gr',width=5)
# p4.place(x=200, y=95)
# p5 = Button(window, text = '20gr',width=5)
# p5.place(x=200, y=120)
# p6 = Button(window, text = '50gr',width=5)
# p6.place(x=200, y=145)
# p7 = Button(window, text = '1zł',width=5)
# p7.place(x=200, y=170)
# p8 = Button(window, text = '2zł',width=5)
# p8.place(x=200, y=195)
# p9 = Button(window, text = '5zł',width=5)
# p9.place(x=200, y=220)
#
# #przyciski od banknotow
#
# p10 = Button(window, text = '10zl', width=5)
# p10.place(x=245,y=20)
# p10 = Button(window, text = '20zl', width=5)
# p10.place(x=245,y=45)
# p10 = Button(window, text = '50zl', width=5)
# p10.place(x=245,y=70)
# p10 = Button(window, text = '100zl', width=5)
# p10.place(x=245,y=95)
#
# #przycisk zakoncz
# zakoncz = Button(window, text = 'Zakoncz transakcje',  width = 20, bg='red')
# zakoncz.place(x=190,y=270)
#
#
# window.mainloop()

# from tkinter import Tk, Label, Button
#
# class A_GUI:
#     def __init__(self, master):
#         self.x = 0
#
#         self.master = master
#         master.title("Tytulik")
#
#         self.label = Label(master, text="Tekst startowy")
#         self.label.pack()
#
#         self.greet_button = Button(master, text="Zmiana", command=self.zmiana)
#         self.greet_button.pack()
#
#     def zmiana(self):
#         self.x += 1
#         self.label.configure(text="Nowa wartość: "+str(self.x))
#
# root = Tk()
# my_gui = A_GUI(root)
# root.mainloop()

