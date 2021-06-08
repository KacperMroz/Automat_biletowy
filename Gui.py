from tkinter import *
from TicketMachine import *
from MoneyStore import *
from decimal import *

class Gui:

    def __init__(self):
        """Konstruktor klasy GUI"""
        self.machine = TicketMachine()
        self.store = MoneyStore()

    def Interface(self):
        """Główne okno interfejsu"""
        okno_wyboru = Tk()
        okno_wyboru.geometry('350x350')

        #napis na górze ekranu
        powitanie = Label(okno_wyboru, text = "Automat Biletowy")
        powitanie.place(x=125, y=0)

        #rodzaje biletów

        #20m
        ulgowy_20m = Label(okno_wyboru, text = "Bilet 20 minutowy ulgowy")
        ulgowy_20m.place(x=0, y=30)

        cena_u_20m = Label(okno_wyboru, text="2zł")
        cena_u_20m.place(x=200, y=30)

        normalny_20m = Label(okno_wyboru, text="Bilet 20 minutowy normalny")
        normalny_20m.place(x=0, y=60)

        cena_n_20m = Label(okno_wyboru, text="4zł")
        cena_n_20m.place(x=200, y=60)

        #40m
        ulgowy_40m = Label(okno_wyboru, text="Bilet 40 minutowy ulgowy")
        ulgowy_40m.place(x=0, y=90)

        cena_u_40m = Label(okno_wyboru, text="3.50zł")
        cena_u_40m.place(x=200, y=90)

        normalny_40m = Label(okno_wyboru, text="Bilet 40 minutowy normalny")
        normalny_40m.place(x=0, y=120)

        cena_n_40m = Label(okno_wyboru, text="7zł")
        cena_n_40m.place(x=200, y=120)

        #60m
        ulgowy_60m = Label(okno_wyboru, text="Bilet 60 minutowy ulgowy")
        ulgowy_60m.place(x=0, y=150)

        cena_u_60m = Label(okno_wyboru, text="4zł")
        cena_u_60m.place(x=200, y=150)

        normalny_60m = Label(okno_wyboru, text="Bilet 60 minutowy normalny")
        normalny_60m.place(x=0, y=180)

        cena_n_60m = Label(okno_wyboru, text="8zł")
        cena_n_60m.place(x=200, y=180)

        #ilosc danego biletu
        val1 = IntVar()
        val2 = IntVar()
        val3 = IntVar()
        val4 = IntVar()
        val5 = IntVar()
        val6 = IntVar()


        ile1 = Label(okno_wyboru, textvar = str(val1))
        ile1.place(x=300, y=30)

        ile2 = Label(okno_wyboru, textvar=str(val2))
        ile2.place(x=300, y=60)

        ile3 = Label(okno_wyboru, textvar=str(val3))
        ile3.place(x=300, y=90)

        ile4 = Label(okno_wyboru, textvar=str(val4))
        ile4.place(x=300, y=120)

        ile5 = Label(okno_wyboru, textvar=str(val5))
        ile5.place(x=300, y=150)

        ile6 = Label(okno_wyboru, textvar=str(val6))
        ile6.place(x=300, y=180)

        #przyciski do dodawania biletu
        b1 = Button(okno_wyboru, text='+',
                    command=lambda : [self.machine.buyTicket(2), s.configure(text="Suma do zaplaty " + str(self.machine.suma)), val1.set(val1.get() + 1)])
        b1.place(x=320, y=30)

        b2 = Button(okno_wyboru, text='+',
                    command=lambda : [self.machine.buyTicket(4), s.configure(text="Suma do zaplaty " + str(self.machine.suma)), val2.set(val2.get() + 1)])
        b2.place(x=320, y=60)

        b3 = Button(okno_wyboru, text='+',
                    command=lambda : [self.machine.buyTicket(3.50), s.configure(text="Suma do zaplaty " + str(self.machine.suma)), val3.set(val3.get() + 1)])
        b3.place(x=320, y=90)

        b4 = Button(okno_wyboru, text='+',
                    command=lambda : [self.machine.buyTicket(7), s.configure(text="Suma do zaplaty " + str(self.machine.suma)), val4.set(val4.get() + 1)])
        b4.place(x=320, y=120)

        b5 = Button(okno_wyboru, text='+',
                    command=lambda : [self.machine.buyTicket(4), s.configure(text="Suma do zaplaty " + str(self.machine.suma)), val5.set(val5.get() + 1)])
        b5.place(x=320, y=150)

        b6 = Button(okno_wyboru, text='+',
                    command=lambda : [self.machine.buyTicket(8), s.configure(text="Suma do zaplaty " + str(self.machine.suma)), val6.set(val6.get() + 1)])
        b6.place(x=320, y=180)


        #napis wyswitlajacy sume

        s = Label(okno_wyboru, text="Suma do zaplaty: " + str(self.machine.suma))
        s.place(x=0, y=220)

        #przycisk od zaplaty

        zaplac = Button(okno_wyboru, text='Zaplac', width=20, bg='red', command = lambda: [self.otworz_okno_zaplaty(), s.configure(text="Suma do zaplaty: 0"),val1.set(0),val2.set(0), val3.set(0), val4.set(0), val5.set(0), val6.set(0)])
        zaplac.place(x=190, y=270)



        okno_wyboru.mainloop()

    def otworz_okno_zaplaty(self):
        """Okno z wpłatami"""
        okno_zaplaty = Tk()
        okno_zaplaty.geometry('350x100')

        self.wrzucone = 0
        transakcja = MoneyStore()

        w = Label(okno_zaplaty, text="Wrzucone pieniadze " + str(self.wrzucone))
        w.place(x=0, y=80)
        s = Label(okno_zaplaty, text="Suma do zaplaty: " + str(self.machine.suma))
        s.place(x=0, y=65)


        p1 = Button(okno_zaplaty, text='1gr', width=3, command=lambda : [self.dodaj(0.01), transakcja.addMoney(0.01),
                                                                   w.configure(text="Wrzucone pieniadze " + str(
                                                                       self.wrzucone))])
        p1.place(x=0, y=10)

        p2 = Button(okno_zaplaty, text='2gr', width=3, command=lambda : [self.dodaj(0.02), transakcja.addMoney(0.02),
                                                                   w.configure(text="Wrzucone pieniadze " + str(
                                                                       self.wrzucone))])
        p2.place(x=30, y=10)

        p3 = Button(okno_zaplaty, text='5gr', width=3, command=lambda : [self.dodaj(0.05), transakcja.addMoney(0.05),
                                                                   w.configure(text="Wrzucone pieniadze " + str(
                                                                       self.wrzucone))])
        p3.place(x=60, y=10)

        p4 = Button(okno_zaplaty, text='10gr', width=3, command=lambda : [self.dodaj(0.1), transakcja.addMoney(0.1),
                                                                    w.configure(text="Wrzucone pieniadze " + str(
                                                                        self.wrzucone))])
        p4.place(x=90, y=10)

        p5 = Button(okno_zaplaty, text='20gr', width=3, command=lambda : [self.dodaj(0.2), transakcja.addMoney(0.2),
                                                                    w.configure(text="Wrzucone pieniadze " + str(
                                                                        self.wrzucone))])
        p5.place(x=120, y=10)

        p6 = Button(okno_zaplaty, text='50gr', width=3, command=lambda : [self.dodaj(0.5), transakcja.addMoney(0.5),
                                                                    w.configure(text="Wrzucone pieniadze " + str(
                                                                        self.wrzucone))])
        p6.place(x=150, y=10)

        p7 = Button(okno_zaplaty, text='1zł', width=3, command=lambda : [self.dodaj(1), transakcja.addMoney(1), w.configure(
            text="Wrzucone pieniadze " + str(self.wrzucone))])
        p7.place(x=180, y=10)

        p8 = Button(okno_zaplaty, text='2zł', width=3, command=lambda : [self.dodaj(2), transakcja.addMoney(2), w.configure(
            text="Wrzucone pieniadze " + str(self.wrzucone))])
        p8.place(x=210, y=10)

        p9 = Button(okno_zaplaty, text='5zł', width=3, command=lambda : [self.dodaj(5), transakcja.addMoney(5), w.configure(
            text="Wrzucone pieniadze " + str(self.wrzucone))])
        p9.place(x=240, y=10)

        # przyciski od banknotow

        p10 = Button(okno_zaplaty, text='10zl', width=5, command=lambda : [self.dodaj(10), transakcja.addMoney(10),
                                                                     w.configure(text="Wrzucone pieniadze " + str(
                                                                         self.wrzucone))])
        p10.place(x=0, y=35)

        p10 = Button(okno_zaplaty, text='20zl', width=5, command=lambda : [self.dodaj(20), transakcja.addMoney(20),
                                                                     w.configure(text="Wrzucone pieniadze " + str(
                                                                         self.wrzucone))])
        p10.place(x=45, y=35)

        p10 = Button(okno_zaplaty, text='50zl', width=5, command=lambda : [self.dodaj(50), transakcja.addMoney(50),
                                                                     w.configure(text="Wrzucone pieniadze " + str(
                                                                         self.wrzucone))])
        p10.place(x=90, y=35)

        p10 = Button(okno_zaplaty, text='100zl', width=5, command=lambda : [self.dodaj(100), transakcja.addMoney(100),
                                                                      w.configure(text="Wrzucone pieniadze " + str(
                                                                          self.wrzucone))])
        p10.place(x=135, y=35)

        zakoncz = Button(okno_zaplaty, text='Zakoncz transakcje', width=20, bg='red', command = lambda: [self.podsumowanie(), transakcja.giveChange(self.machine.suma, self.wrzucone), transakcja.clearCustomerMoneyList(), self.machine.endOfTransaction(), self.zeruj(), w.configure(text="Wrzucone pieniadze " + str(self.wrzucone)), s.configure(text="Suma do zaplaty " + str(self.machine.suma))])
        zakoncz.place(x=190, y=40)


    def dodaj(self, value) :
        """Funkcja dodajaca wrzucone monety"""
        self.wrzucone += Decimal(str(value))

    def zeruj(self):
        """Funkcja zerujaca wrzucone monety"""
        self.wrzucone = 0

    def podsumowanie(self):
        """Funkcja podsumujaca zakupy"""
        if self.machine.suma == 0:
            pass
        else:
            print("Kupiono biletów za: " + str(self.machine.suma) + "zł")
            print("Wrzucono: "+str(self.wrzucone) + "zł")



test = Gui()
test.Interface()