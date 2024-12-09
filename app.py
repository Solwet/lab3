class Figure:
    """Родительский класс Figure с атрибутами name, length, width, height"""

    def __init__(self, name, length, width, height):
        """Инициализация атрибутов объекта"""
        self.name = name
        self._length = length  # Приватный атрибут
        self._width = width    # Приватный атрибут
        self._height = height  # Приватный атрибут

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной.")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной.")
        self._height = value

    @property
    def area(self):
        """Метод для вычисления площади (если применяется к фигуре, основанной на прямоугольнике)"""
        return self._length * self._width

    def volume(self):
        """Метод для вычисления объема (будет переопределен в дочернем классе)"""
        raise NotImplementedError("Метод volume() должен быть переопределен в дочернем классе.")

    @staticmethod
    def about():
        """Статический метод about()"""
        return ("Команда разработки:\n"
                "Разработчик 1: Мухтаров Руслан отвечает за начальное определение родительского класса и атрибутов. "
                "Определение статического метода about() для вывода информации по команде разработки.\n"
                "Разработчик 2: Пересыпкин Давид отвечает за определение методов класса. Инициализация. "
                "Определение приватных (закрытых) атрибутов объектов.\n"
                "Разработчик 3: Пестерев Андрей отвечает за наследование от родительского класса. "
                "Переопределение методов. Реализация вычисляемого значения.")

# Дочерний класс RectangularPrism, который наследует Figure
class RectangularPrism(Figure):
    """Класс для прямоугольного параллелепипеда, наследующий Figure"""

    def __init__(self, length, width, height):
        """Инициализация с передачей атрибутов в родительский класс"""
        super().__init__("Прямоугольный параллелепипед", length, width, height)

    def volume(self):
        """Переопределенный метод для вычисления объема"""
        return self._length * self._width * self._height

# Функция для безопасного ввода положительных чисел
def input_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Число должно быть положительным. Попробуйте снова.")
            else:
                return value
        except ValueError:
            print("Ошибка: введено некорректное значение. Введите положительное число.")

# Ввод данных с клавиатуры с проверкой
length = input_positive_number("Введите длину прямоугольного параллелепипеда: ")
width = input_positive_number("Введите ширину прямоугольного параллелепипеда: ")
height = input_positive_number("Введите высоту прямоугольного параллелепипеда: ")

# Создаем объект прямоугольного параллелепипеда с введенными значениями
prism = RectangularPrism(length, width, height)

# Вывод результатов
print(prism.name)               # Вывод имени фигуры
print("Площадь:", prism.area)   # Вывод площади
print("Объем:", prism.volume()) # Вывод объема

# Изменение параметров с использованием сеттеров через ввод с клавиатуры
prism.length = input_positive_number("Введите новую длину: ")
prism.width = input_positive_number("Введите новую ширину: ")
prism.height = input_positive_number("Введите новую высоту: ")

print("Обновленная площадь:", prism.area)   # Вывод обновленной площади
print("Обновленный объем:", prism.volume()) # Вывод обновленного объема
