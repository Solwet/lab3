class Figure:
    """
    Родительский класс Figure с атрибутами name, length, width, height
    """
    def __init__(self, name, length, width, height):
        # Приватные атрибуты
        self.__name = name
        self.__length = length
        self.__width = width
        self.__height = height

    # Геттеры для доступа к приватным атрибутам
    @property
    def name(self):
        return self.__name

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @staticmethod
    def about():
        """
        Статический метод about()
        """
        return (
            "Сюжировка разработчиков:\n"
            "Разработчик 1: Мухтаров Рустам отвечает за начальное определение родительского класса и атрибутов.\n"
            "Разработчик 2: Пересыпкин Давид отвечает за определение методов класса. Инициализация. Определение приватных атрибутов.\n"
            "Разработчик 3: Пестерея Андрей отвечает за наследование от родительского класса. Переопределение методов. Реализация вычисляемого значения."
        )

# Проверяем работу разработчика 2
figure = Figure("Прямоугольник", 10, 5, 3)
print(f"Название: {figure.name}")
print(f"Длина: {figure.length}")
print(f"Ширина: {figure.width}")
print(f"Высота: {figure.height}")