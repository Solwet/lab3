class ElementPeresypkin:
    def __init__(self, name, symbol, number):
        # Приватные атрибуты
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def dump(self):
        # Вывод информации об элементе
        print(f"Название: {self.__name}, Символ: {self.__symbol}, Порядковый номер: {self.__number}")

    # Геттеры
    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


# Создаем объект для элемента "Сера"
element = ElementPeresypkin("Сера", "S", 16)

# Выводим данные об элементе
element.dump()
