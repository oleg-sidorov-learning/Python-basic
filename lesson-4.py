from sys import argv
from functools import reduce
from itertools import count, cycle


def task1():

    """

        1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
        В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
        Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

    :return:
    """

    if len(argv) != 4:
        print("Требуется указать 4 параметра для расчета заработной платы, включая имя скрипта: ")
    else:
        _, productivity, bet, bonus = argv
        if correct_input(productivity, bet, bonus):
            print("Расчет заработной платы не возможен, некорректные параметры скрипта!")
        else:
            salary = float(productivity) * float(bet) + float(bonus)
            print(f"заработная плата составляет: {salary}")


def correct_input(param1, param2, param3):

    """
        Функция провеяет корректность ввода данных для расчета заработной платы

    :param param1: float выработка
    :param param2: float ставка
    :param param3: float премия
    :return:
    """

    try:
        float(param1)
        float(param2)
        float(param3)
        return False
    except ValueError:
        return True


def task2():

    """
        2. Представлен список чисел.
        Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

    :return:
    """

    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print([my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index - 1]])


def task3():

    """
        3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
        Необходимо решить задание в одну строку.

    :return:
    """
    print([elem for elem in range(20, 241) if elem % 20 == 0 or elem % 21 == 0])


def task4():
    my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    print([elem for elem in my_list if my_list.count(elem) < 2])


def task5():

    """
        5. Реализовать формирование списка, используя функцию range() и возможности генератора.
        В список должны войти четные числа от 100 до 1000 (включая границы).
        Необходимо получить результат вычисления произведения всех элементов списка.

    :return:
    """
    print(reduce(composition, [elem for elem in range(100, 1001) if elem % 2 == 0]))


def composition(prev_el, el):

    """
        Функция возвращает произведение двух чисел

    :param prev_el: int предыдущее выполнение функции
    :param el: int следующий элемент списка
    :return: int произведение параметров функции
    """
    return prev_el * el


def task6():

    """
        6. Реализовать два небольших скрипта:

        а) итератор, генерирующий целые числа, начиная с указанного,

        б) итератор, повторяющий элементы некоторого списка, определенного заранее.

    :return:
    """

    start_number = int(input("Введите число с которого необходимо произвести генерацию: "))
    stop_number = int(input("Введите число до которого необходимо произвести генерацию: "))
    repeat_list = ["1", "2", 3]
    repeat_count = int(input("Введите количество итераций: "))

    for elem in count(start_number):
        if elem > stop_number:
            break
        else:
            print(elem)

    index = 0
    for elem in cycle(repeat_list):
        if index > repeat_count:
            break
        else:
            print(elem)
            index += 1


def task7():

    """
        Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
        При вызове функции должен создаваться объект-генератор.
        Функция должна вызываться следующим образом: for el in fact(n).
        Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
        начиная с 1! и до n!.

    :return:
    """
    n = int(input("Введите число, факториал, которого необходимо получить: "))
    f = 1
    for el in fact(n):
        f *= el
        print(f)


def fact(n):

    """
        Генератор последовательности чисел от 1 до n
    :param n: целое число
    :return:
    """
    for el in range(1, n + 1):
        yield el


if __name__ == "__main__":

    # Задание 1
    task1()

    # Задание 2
    task2()

    # Задание 3
    task3()

    # Задание 4
    task4()

    # Задание 5
    task5()

    # Задание 6
    task6()

    # Задание 7
    task7()
