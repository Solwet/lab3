class ElementMukhtarov:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'Element Name: {self.name}, Symbol: {self.symbol}, Atomic Number: {self.number}'

this_element = ElementMukhtarov("Silicon", "Si", 14)

print(this_element)