from tkinter import *
from TicketMachine import *

class Gui:
    def __init__(self):
        pass

    def Interface(self):


        window = Tk()
        window.geometry('350x300')
        l = Label(window, text="Wybierz rodzaj biletu")
        l.place(x=0, y=0)

        suma = TicketMachine()
        self.wrzucone = 0

        s = Label(window, text="Suma do zaplaty "+str(suma.suma))
        s.place(x=0, y= 180)
        w = Label(window, text="Wrzucone pieniadze "+str(self.wrzucone))
        w.place(x=0, y=200)

        # przyciski od biletow
        b1 = Button(window, text='bilet 20 minut ulgowy', width=20, command = lambda: [suma.buyTicket(2), s.configure(text="Suma do zaplaty "+str(suma.suma))])
        b1.place(x=0, y=20)
        b2 = Button(window, text='bilet 20 minut normalny', width=20,command = lambda: [suma.buyTicket(4), s.configure(text="Suma do zaplaty "+str(suma.suma))])
        b2.place(x=0, y=45)
        b3 = Button(window, text='bilet 40 minut ulgowy', width=20,command = lambda: [suma.buyTicket(3.50), s.configure(text="Suma do zaplaty "+str(suma.suma))])
        b3.place(x=0, y=70)
        b4 = Button(window, text='bilet 40 minut normalny', width=20,command = lambda: [suma.buyTicket(7), s.configure(text="Suma do zaplaty "+str(suma.suma))])
        b4.place(x=0, y=95)
        b5 = Button(window, text='bilet godzinny ulgowy', width=20,command = lambda: [suma.buyTicket(4), s.configure(text="Suma do zaplaty "+str(suma.suma))])
        b5.place(x=0, y=120)
        b6 = Button(window, text='bilet godzinny normalny', width=20,command = lambda: [suma.buyTicket(8), s.configure(text="Suma do zaplaty "+str(suma.suma))])
        b6.place(x=0, y=145)

        l1 = Label(window, text='Wrzuc pieniadze')
        l1.place(x=200, y=0)



        # przyciski od monet

        p1 = Button(window, text='1gr', width=5,command = lambda: [self.dodaj(0.01), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p1.place(x=200, y=20)
        p2 = Button(window, text='2gr', width=5,command = lambda: [self.dodaj(0.02), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p2.place(x=200, y=45)
        p3 = Button(window, text='5gr', width=5,command = lambda: [self.dodaj(0.05), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p3.place(x=200, y=70)
        p4 = Button(window, text='10gr', width=5,command = lambda: [self.dodaj(0.1), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p4.place(x=200, y=95)
        p5 = Button(window, text='20gr', width=5,command = lambda: [self.dodaj(0.2), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p5.place(x=200, y=120)
        p6 = Button(window, text='50gr', width=5,command = lambda: [self.dodaj(0.5), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p6.place(x=200, y=145)
        p7 = Button(window, text='1zł', width=5,command = lambda: [self.dodaj(1), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p7.place(x=200, y=170)
        p8 = Button(window, text='2zł', width=5,command = lambda: [self.dodaj(2), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p8.place(x=200, y=195)
        p9 = Button(window, text='5zł', width=5,command = lambda: [self.dodaj(5), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p9.place(x=200, y=220)

        # przyciski od banknotow

        p10 = Button(window, text='10zl', width=5,command = lambda: [self.dodaj(10), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p10.place(x=245, y=20)
        p10 = Button(window, text='20zl', width=5,command = lambda: [self.dodaj(20), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p10.place(x=245, y=45)
        p10 = Button(window, text='50zl', width=5,command = lambda: [self.dodaj(50), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p10.place(x=245, y=70)
        p10 = Button(window, text='100zl', width=5,command = lambda: [self.dodaj(100), w.configure(text="Wrzucone pieniadze "+str(self.wrzucone))])
        p10.place(x=245, y=95)

        # przycisk zakoncz
        zakoncz = Button(window, text='Zakoncz transakcje', width=20, bg='red', command = lambda: suma.endOfTransaction())
        zakoncz.place(x=190, y=270)

        window.mainloop()

    def dodaj(self,value):
        self.wrzucone += value


my_gui = Gui()
my_gui.Interface()