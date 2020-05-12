class TicketMachine:
    def __init__(self):
        self.storage = {
            '0.01': 100, '0.02': 100, '0.05': 100, '0.10': 100, '0.20': 100,
            '0.50': 100, '1.00': 100, '2.00': 100, '5.00': 100, '10.00': 10,
            '20.00': 10, '50.00': 10, '100.00': 10, '200.00': 5, '500.00': 5
        }

    # Oblicz ile reszty wydać, dostajesz zamówienie na którym są wszystkie bilety i cena całkowita
    def calculateCashToReturn(self, order):
        return True
