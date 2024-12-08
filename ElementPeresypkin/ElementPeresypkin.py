class ElementPeresypkin:
    def __init__(self, name, symbol, number):
        # Инициализация атрибутов
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        # Вывод информации об элементе
        print(f"Название: {self.name}, Символ: {self.symbol}, Порядковый номер: {self.number}")