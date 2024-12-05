class ElementMukhtarov:
    """Иницилизируем объект по признакам Имя, символ, номер из периодической таблицы"""
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number  

    """Декоратор property и сеттеры """
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if type(name) == str:
            self.__name = name
        else:
            raise ValueError ("Имя может иметь только тип str")
    
    @property
    def symbol(self):
        return self.__symbol
    @symbol.setter
    def symbol(self,symbol):
        if type(symbol) == str:
            self.__symbol = symbol
        else:
            raise ValueError ("Символ может иметь только тип str")

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,number):
        if type(number) == int:
            self.__number = number
        else:
            raise ValueError ("Номер элемента может быть только целым числом")
    
    
    def dump(self):
        """Метод вывода признаков объекта"""
        print("Название элемента "+ self.name+ "Химический символ элемента "+ self.symbol+ "Порядковый номер элемента в переодической таблице " +str(self.number))

MyElement=ElementMukhtarov("None ","None ",0)
MyElement.name = "Кремний "
MyElement.symbol = "Si " 
MyElement.number = 14

MyElement.dump()