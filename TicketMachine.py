from MoneyStore import MoneyStore
from Tickets import *
from decimal import *

class TicketMachine(MoneyStore):
    suma = 0

    def __init__(self):
        super().__init__()

    def buyTicket(self, ticket_price):
        self.suma += Decimal(str(ticket_price))

    def returnSum(self):
        return self.suma

    def endOfTransaction(self):

        self.suma = 0

p = TicketMachine()
p.buyTicket(2)
p.buyTicket(1)
print(p.returnSum())
