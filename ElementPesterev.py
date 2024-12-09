class ElementPesterev:
    def __init__(self, name, symbol, number):
        # Приватные атрибуты
        self.__name = name
        self.__symbol = symbol
        self.__number = number
        # Свойства-получатели (геттеры) для каждого атрибута
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    # Метод для вывода значений атрибутов
    def dump(self):
        print(f"Element Name: {self.name}")
        print(f"Symbol: {self.symbol}")
        print(f"Atomic Number: {self.number}")
chlor = ElementPesterev("Chlorine", "Cl", 17)
chlor.dump()
