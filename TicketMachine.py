from decimal import *

class TicketMachine():
    suma = 0

    def __init__(self):
        """Konstruktor"""
        super().__init__()

    def buyTicket(self, ticket_price):
        """Funkcja odpowiedzialna za kupowanie biletow"""
        self.suma += Decimal(str(ticket_price))

    def returnSum(self):
        """Funkcja zwracajaca calkowity koszt biletow"""
        return self.suma

    def endOfTransaction(self):
        """Funkcja konczaca transakcje """
        self.suma = 0

