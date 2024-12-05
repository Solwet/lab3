class ElementMukhtarov:
    """Иницилизируем объект по признакам Имя, символ, номер из периодической таблицы"""
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


MyElement=ElementMukhtarov("Кремний ","Si ",14)

print(MyElement.name, MyElement.symbol, MyElement.number)