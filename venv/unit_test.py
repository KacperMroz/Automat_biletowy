import unittest
from TicketMachine import *
from MoneyStore import *

class MyTestCase(unittest.TestCase) :
    """klasa odpowiadajaca za unittest"""
    def testShouldReturnNoChange(self):
        """Zakup biletu za odliczona kwote"""
        machine = TicketMachine()
        store = MoneyStore()
        machine.buyTicket(2)
        store.addMoney(2)
        self.assertEqual('Kupiles bilet za odliczona kwote', store.giveChange(machine.suma, store.sumOfCoinsAddedByCustomer()))

    def testShoudlReturnChange(self):
        """Zakup biletu za większą kwote, oczekiwana reszta"""
        machine = TicketMachine()
        store = MoneyStore()
        store.addMoney(1)
        store.addMoney(2)
        store.addMoney(2)
        machine.buyTicket(4)
        self.assertEqual('Twoja reszta : 1.0', store.giveChange(machine.suma, store.sumOfCoinsAddedByCustomer()))

    def testShouldNotReturnChange(self):
        """Brak możliwosci wydania reszty"""
        machine = TicketMachine()
        store = MoneyStore()
        store.addMoney(2)
        store.addMoney(2)
        machine.buyTicket(3.5)
        self.assertEqual('TYLKO ODLICZONA KWOTA!! Oddaje: 2.0, 2.0', store.giveChange(machine.suma, store.sumOfCoinsAddedByCustomer()))

    def testStoGroszyToJedenZloty(self):
        """Sprawdzenie czy 100gr jest rowne 1zl"""
        store = MoneyStore()
        for _ in range(0,100):
            store.addMoney(0.01)
        self.assertEqual(1, store.sumOfCoins())

    def testBuyTwoDiffrentTickets(self):
        """Zakup dwóch różnych biletów"""
        machine = TicketMachine()
        store = MoneyStore()
        machine.buyTicket(2)
        machine.buyTicket(4)
        self.assertEqual(6, machine.returnSum())

    def testAddMoneyAfterTicket(self):
        """Wybór kolejnego biletu po wrzuceniu pieniedzy"""
        machine = TicketMachine()
        store = MoneyStore()
        machine.buyTicket(2)
        store.addMoney(2)
        machine.buyTicket(4)
        store.addMoney(2)
        store.addMoney(2)
        self.assertEqual('Kupiles bilet za odliczona kwote', store.giveChange(machine.suma, store.sumOfCoinsAddedByCustomer()))


if __name__ == '__main__' :
    unittest.main()