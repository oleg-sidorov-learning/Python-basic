def task1():
    """
    Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
    год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
    месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
    :return:
    """
    today = Date('05-12-2020')
    print(today)
    day, month, year = Date.get_date_int('05-12-2020')
    print(f"{day} {month} {year}")
    print(Date.validate(5, 12, 2020))
    print(Date.validate(40, 5, 2450))


class Date:
    """
    Класс Дата
    """
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date_int(cls, date):
        """
        Преобразование к числу частей даты
        :param date:
        :return:
        """
        return map(int, [int(elem) for elem in date.split('-')])

    @staticmethod
    def validate(day, month, year):
        """
        Проверка на корректность
        :param day:
        :param month:
        :param year:
        :return:
        """
        day_months = {1: 31,
                      2: 29 if year % 4 == 0 else 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 30,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}
        return 1 <= month <= 12 and 1 <= day <= day_months[month]


def task2():
    """
    Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
    Проверьте его работу на данных, вводимых пользователем.
    При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
    и не завершиться с ошибкой.
    :return:
    """
    divider = int(input("Введите делимое: "))
    denominator = int(input("Введите делитель: "))
    try:
        if denominator == 0:
            raise MyException("Деление на ноль запрещено")
        return divider / denominator
    except MyException as msg:
        print(msg)


class MyException(Exception):
    """
    Класс исключение
    """
    def __init__(self, txt):
        self.txt = txt


def task3():
    """
    Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
    Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
    Класс-исключение должен контролировать типы данных элементов списка.

    Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
    пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
    При этом скрипт завершается, сформированный список выводится на экран.
    :return:
    """
    my_list = []
    stop_word = 'stop'
    while True:
        user_number = input(f"Введите число или стоп-слово {stop_word}: ")
        if user_number == stop_word:
            break
        else:
            try:
                user_number = user_number_float(user_number)
                if type(user_number) is not float:
                    raise OnlyNumbers("Вы ввели не число!!!")
            except OnlyNumbers as msg:
                print(msg)
            else:
                my_list.append(user_number)

    print(my_list)


def user_number_float(user_number_string):
    """
    Функция приводит число к float
    :param user_number_string: string
    :return: string, float
    """
    try:
        user_number_string = float(user_number_string)
    except ValueError:
        pass

    return user_number_string


class OnlyNumbers(Exception):
    """
    Класс исключение
    """
    def __init__(self, txt):
        self.txt = txt


def task456():
    """
    Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

    Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
    и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
    а также других данных, можно использовать любую подходящую структуру, например словарь.

    Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    :return:
    """
    printer1 = Printer("Принтер 1", 10000.0, 5, 45)
    printer2 = Printer("Принтер 2", 20000.0, 3, 45)
    scanner1 = Printer("Сканнер 1", 5000.0, 7, 45)
    xerox1 = Printer("Ксерокс 1", 15000.0, 10, 45)
    printer3 = Printer("Принтер 3", 2000.0, 2, 45)

    if Warehouse.validation(printer1):
        Warehouse.acceptance(printer1)

    if Warehouse.validation(printer2):
        Warehouse.acceptance(printer2)

    if Warehouse.validation(printer3):
        Warehouse.moving(printer3)

    print(Warehouse.equipment)


class Warehouse:
    """
    Класс Склад.
    """
    equipment = {}

    @classmethod
    def acceptance(cls, self):
        cls.equipment[self.name] = cls.equipment.get(self.name, 0) + self.quantity

    @classmethod
    def moving(cls, self):
        cls.equipment[self.name] = cls.equipment.get(self.name, 0) - self.quantity

    @staticmethod
    def validation(self):
        if type(self.quantity) is int and type(self.price) is float:
            return True
        else:
            print("Данные некорректны!")
            return False


class OfficeEquipment:
    """
    Класс оргтехника.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):
    """
    Класс принтер.
    """
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size


class Scanner(OfficeEquipment):
    """
    Класс сканнер.
    """
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size


class Xerox(OfficeEquipment):
    """
    Класс ксерокс.
    """
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size


def task7():
    """
    Реализовать проект «Операции с комплексными числами».
    Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
    Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
    и умножение созданных экземпляров. Проверьте корректность полученного результата.
    :return:
    """
    print("Встроенная работа с комплексными числами")
    a = complex(1, 2)
    print(a)
    b = complex(2, 3)
    print(b)
    print(a + b)
    print(a * b)
    print("Перегрузка методов")
    x = Complex(1, 2)
    y = Complex(2, 3)
    print(x)
    print(y)
    print(x + y)
    print(x * y)


class Complex:
    """
    Класс комплексное число.
    """
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"({self.real}+{self.imaginary}j)"


if __name__ == '__main__':

    task1()

    task2()

    task3()

    task456()

    task7()

