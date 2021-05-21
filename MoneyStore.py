from decimal import *


class MoneyStore:
    _list_of_money_format = [0.01, 0.02, 0.05, 0.01, 0.2, 0.5, 1, 2, 5, 10, 20, 50]

    def __init__(self):
        self.list_of_money_in_machine = []
        self.value = 0

    def addMoney(self, value):
        if value in self._list_of_money_format:
            self.value = value
            self.list_of_money_in_machine.append(value)
        else:
            print("Unknown format of money")  # TODO: oblsluga bledu

    def takeMoney(self, value):         #TODO: zastanowic sie czy ta funkcja wgl jest potrzebna
        if value in self.list_of_money_in_machine:
            self.list_of_money_in_machine.remove(value)
        else:
            print("No such value in  machine ")  # TODO: oblsluga bledu

    def sumOfCoins(self):
        print("Suma pieniedzy w biletomacie to ", sum(self.list_of_money_in_machine))
        return sum(self.list_of_money_in_machine)

    def giveChange(self, price, amount): #TODO: napisac obluge bledu. Tak zeby w przypadku braku mozliwosci wydania reszty program  przechodzil do procedury else i oddawal pieniadze
        change = amount - price
        list_of_money_to_return = []
        while change>0:
            #try:
            maxValueToReturn = max(filter(lambda i : i <= change, self.list_of_money_in_machine))
            #except ValueError():
            list_of_money_to_return.append(maxValueToReturn)
            self.takeMoney(maxValueToReturn)
            change -= maxValueToReturn

        print("Reszta to:",sum(list_of_money_to_return))
        print("Wydana w ", list_of_money_to_return)


        #TODO: dopisac usuwanie z listy wydanych pieniedzy.

p = MoneyStore()
p.addMoney(2)
p.addMoney(2)
p.addMoney(2)
p.addMoney(2)
print(p.sumOfCoins())
p.giveChange(4, 8)
print(p.sumOfCoins())