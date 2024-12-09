def __repr__(self):
    return f"Element: {self.name} (Symbol: {self.symbol}, Atomic Number: {self.number})"

def dump(self):
    # Метод для вывода значений атрибутов объекта
    print(f"Element Name: {self.name}")
    print(f"Symbol: {self.symbol}")
    print(f"Atomic Number: {self.number}")

chlor = ElementPesterev(name="Chlor", symbol="Cl", number=17)

print(chlor)
chlor.dump()
