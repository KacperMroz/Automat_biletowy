from MoneyStore import MoneyStore
from Tickets import *

class TicketMachine(MoneyStore):
    _sum = 0

    def __init__(self):
        pass

    def buyTicket(self, ticket_price):
        self._sum += ticket_price

    def endOfTransaction(self):
        self._sum = 0