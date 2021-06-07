from decimal import *


class MoneyStore:
    _list_of_money_format = [0.01, 0.02, 0.05, 0.10, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]

    def __init__(self):
        self.list_of_money_in_machine = []
        self.value = 0
        self.money_added_by_customer = []

    def addMoney(self, value):
        if value in self._list_of_money_format:
            self.value = value
            self.list_of_money_in_machine.append(Decimal(str(value)))
            self.money_added_by_customer.append(Decimal(str(value)))
        else:
            print("Unknown format of money")  # TODO: oblsluga bledu

    def takeMoney(self, value):         #TODO: zastanowic sie czy ta funkcja wgl jest potrzebna
        if value in self.list_of_money_in_machine:
            self.list_of_money_in_machine.remove(value)
        else:
            print("No such value in  machine ")  # TODO: oblsluga bledu

    def sumOfCoins(self):
        print("Suma pieniedzy w biletomacie to ", sum(self.list_of_money_in_machine))
        print("Pieniadze w automacie: "+ str(", ".join([str(float(i)) for i in self.list_of_money_in_machine])))
        return sum(self.list_of_money_in_machine)

    def giveChange(self, price, amount):
        change = amount - price
        changeList = []
        czy_reszta_wydana = False
        if amount == 0:
            return print("ZA DARMO NIC NIE DOSTANIESZ!!! WRZUC PIENIADZE")
        if price == 0:
            self.takeMoneyFromList(self.list_of_money_in_machine, self.money_added_by_customer)
            self.money_added_by_customer.clear()
            return print("Nic nie kupiles!")
        if change == 0 :
            self.money_added_by_customer.clear()
            return print("Kupiles bilet za odliczona kwote")
        else:
            for i in range(len(self.list_of_money_in_machine)):
                if change == 0 :
                    print("Twoja reszta : " + str(", ".join([str(float(i)) for i in changeList])))
                    czy_reszta_wydana = True
                    break
                else :
                    if self.list_of_money_in_machine[i] <= change :
                        changeList.append(self.list_of_money_in_machine[i])
                        change -= self.list_of_money_in_machine[i]
            if change != 0 :
                print("Nie moge wydac reszty!! TYLKO ODLICZONA KWOTA!!")
                print("Oddaje: "+ str(", ".join([str(float(i)) for i in self.money_added_by_customer])))

        if(czy_reszta_wydana == False):
            self.takeMoneyFromList(self.list_of_money_in_machine, self.money_added_by_customer)
        else:
            self.takeMoneyFromList(self.list_of_money_in_machine, changeList)

        self.money_added_by_customer.clear()


    def takeMoneyFromList(self, money_list, change_list):
        for element in change_list :
            if element in money_list:
                money_list.remove(element)

