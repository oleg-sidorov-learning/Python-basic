from abc import ABC, abstractmethod


def task1():
    """
     Реализовать класс Matrix (матрица).
     Обеспечить перегрузку конструктора класса (метод __init__()),
     который должен принимать данные (список списков) для формирования матрицы.
    :return:
    """

    matrix1 = Matrix([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ])

    matrix2 = Matrix([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ])

    matrix3 = Matrix([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ])

    print(matrix1 + matrix2 + matrix3)


class Matrix:
    """
    Класс матрица.
    """
    def __init__(self, numbers: list):
        self.matrix = numbers

    def __str__(self):
        return '\n'.join([' '.join(map(str, str_matrix)) for str_matrix in self.matrix])

    def __add__(self, other):
        return Matrix([[x + y for x, y in zip(A, B)] for A, B in zip(self.matrix, other.matrix)])


def task2():
    """
    Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм.
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
    Это могут быть обычные числа: V и H, соответственно.

    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

    Реализовать общий подсчет расхода ткани.
    Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
    проверить на практике работу декоратора @property.
    :return:
    """
    coat1 = Coat("Пальто 1", 10)
    print(coat1.fabric_calculation)
    Clothes.total_expense += coat1.fabric_calculation

    costume1 = Costume("Костюм 1", 20)
    print(costume1.fabric_calculation)
    Clothes.total_expense += costume1.fabric_calculation

    print(Clothes.total_expense)


class Clothes(ABC):
    """
    Базовый класс Одежда.
    """
    total_expense = 0

    def __init__(self, tittle):
        self.tittle = tittle

    @abstractmethod
    def fabric_calculation(self):
        pass


class Coat(Clothes):
    """
    Класс пиджак.
    """
    def __init__(self, tittle, size):
        super().__init__(tittle)
        self.size = size

    @property
    def fabric_calculation(self):
        """
        Функция расчета расхода ткани.
        :return:
        """
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    """
    Класс костюм.
    """
    def __init__(self, tittle, height):
        super().__init__(tittle)
        self.height = height

    @property
    def fabric_calculation(self):
        """
        Функция расчета расхода ткани.
        :return:
        """
        return 2 * self.height + 0.3


def task3():
    """
    Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов:
    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
    умножение и обычное (не целочисленное) деление клеток, соответственно.
    В методе деления должно осуществляться округление значения до целого числа.

    Сложение. Объединение двух клеток.
    При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

    Вычитание. Участвуют две клетки.
    Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
    иначе выводить соответствующее сообщение.

    Умножение. Создается общая клетка из двух.
    Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

    Деление. Создается общая клетка из двух.
    Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    Данный метод позволяет организовать ячейки по рядам.

    Метод должен возвращать строку вида *****\n*****\n*****...,
    где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
    то в последний ряд записываются все оставшиеся.

    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n**.

    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n*****.
    :return:
    """
    cell1 = Cell(15)
    cell2 = Cell(23)
    print(cell1 + cell2)
    print(cell1 - cell2)
    print(cell1.make_order(5))
    print(cell2.make_order(5))


class Cell:
    """
    Класс ячейка.
    """
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        msg_error = f"Нельзя из первой клетки вычесть вторую"
        return Cell(self.quantity - other.quantity) if self.quantity > other.quantity else msg_error

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, step):
        return ''.join(['*\\n' if index % step == 0 and index != self.quantity else '*' for index in range(1, self.quantity + 1)])


if __name__ == "__main__":

    task1()

    task2()

    task3()
