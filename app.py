class Figure:
    """Родительский класс Figure с атрибутами name, length, width, height"""
    def init(self, name, length, width, height):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
    
    @staticmethod
    def about():
        """Статический метод about()"""
        return ("Команда разработки:\n"
                "Разработчик 1: Мухтаров Руслан отвечает за начальное определение родительского класса и атрибутов. Определение статического метода about() для вывода информации по команде разработки\n"
                "Разработчик 2: Пересыпкин Давид отвечает за определение методов класса. Инициализация. Определение приватных (закрытых) атрибутов объектов.\n"
                "Разработчик 3: Пестерев Андрей отвечает за Наследование от родительского класса. Переопределение методов Реализация вычисляемого значения.")
print(Figure.about())