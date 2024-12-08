class ElementPeresypkin:
    def __init__(self, name, symbol, number):
        # Приватные атрибуты
        self.__name = name  # Название элемента
        self.__symbol = symbol  # Символ элемента
        self.__number = number  # Порядковый номер элемента

    def dump(self):
        # Метод для вывода значений атрибутов
        print(f"Название: {self.__name}, Символ: {self.__symbol}, Порядковый номер: {self.__number}")

    # Геттер для name
    @property
    def name(self):
        return self.__name

    # Геттер для symbol
    @property
    def symbol(self):
        return self.__symbol

    # Геттер для number
    @property
    def number(self):
        return self.__number


# Создаем объект для элемента "Сера"
element = ElementPeresypkin("Сера", "S", 16)

# Выводим данные об элементе
element.dump()