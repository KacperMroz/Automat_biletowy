from MoneyStore import MoneyStore
from Tickets import *

class TicketMachine(MoneyStore):
    suma = 0

    def __init__(self):
        super().__init__()

    def buyTicket(self, ticket_price):
        self.suma += ticket_price
        print("Do koszyka dodado bilet o wartosci " + str(ticket_price) + " zl")

    def returnSum(self):
        return self.suma

    def endOfTransaction(self):
        print(self.suma)
        self.suma = 0

