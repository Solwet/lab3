class ElementMukhtarov:
    """Иницилизируем объект по признакам Имя, символ, номер из периодической таблицы"""
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        """Метод вывода признаков объекта"""
        print("Название элемента "+ self.name+ "Химический символ элемента "+ self.symbol+ "Порядковый номер элемента в переодической таблице " +str(self.number))

MyElement=ElementMukhtarov("Кремний ","Si ",14)


MyElement.dump()