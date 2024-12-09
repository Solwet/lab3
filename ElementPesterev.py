class ElementPesterev:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __repr__(self):
        return f"Element: {self.name} (Symbol: {self.symbol}, Atomic Number: {self.number})"

chlor = ElementPesterev(name="Chlor", symbol="Cl", number=17)

print(chlor)
