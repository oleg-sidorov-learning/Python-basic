import json


def task1():

    """

    Создать программно файл в текстовом формате, записать в него построчно данные,
    вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
    :return:
    """

    with open('task1.txt', 'a') as f_obj:
        while True:
            some_text = input("Введите текст: ")
            if not some_text:
                break
            else:
                f_obj.write(f"{some_text}\n")


def task2():

    """

        Создать текстовый файл (не программно), сохранить в нем несколько строк,
        выполнить подсчет количества строк, количества слов в каждой строке.
    :return:
    """

    with open('task2.txt', 'r') as f_obj:
        my_list_strings = f_obj.readlines()
        print(f'Количество строк в файле {len(my_list_strings)}')
        for my_string in my_list_strings:
            print(f'Количество слов в строке: {my_string} составляет {len(my_string.split())}')


def task3():

    """

    Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников
    :return:
    """

    with open('task3.txt', 'r') as f_obj:
        my_list_strings = f_obj.readlines()
        salaries = []
        for my_string in my_list_strings:
            name, salary = my_string.split()
            salaries.append(float(salary))
            if salary.isdigit() and float(salary) < 20000:
                print(f'Сотрудник {name} имеет оклад {salary} меньше 20000')

        print(f'Средний оклад равен: {mean(salaries)}')


def mean(numbers):

    """

    :param numbers: list
    :return: float Возвращает среднее
    """

    return sum(numbers) / len(numbers)


def task4():

    """
    Создать (не программно) текстовый файл со следующим содержимым:

    One — 1

    Two — 2

    Three — 3

    Four — 4

    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
    :return:
    """

    translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    my_list_for_new_file = []
    with open('task4.txt', 'r') as f_obj:
        my_list_strings = f_obj.readlines()
        for my_string in my_list_strings:
            try:
                en, number = my_string.split(' — ')
                my_list_for_new_file.append(f'{translate[en]} - {number}')
            except ValueError:
                print('Строка не содержит необходимого разделителя и будет добавлена в новый файл в том же виде')
                my_list_for_new_file.append(my_string)

    with open('task4_new.txt', 'w') as f_obj:
        f_obj.writelines(my_list_for_new_file)


def task5():

    """
        Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
        Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    :return:
    """

    with open('task5.txt', 'w') as file_obj:
        file_obj.write(input('Введите набор чисел разделенные пробелом: '))

    with open('task5.txt', 'r') as file_obj:
        list_numbers = file_obj.read().split()
        try:
            print(sum(map(int, list_numbers)))
        except ValueError:
            print(f"Ошибка данных в файле: {list_numbers}")


def task6():

    """
        Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
        и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
        Важно, чтобы для каждого предмета не обязательно были все типы занятий.
        Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
        Вывести словарь на экран.

    :return:
    """

    subject = {}
    with open('task6.txt', 'r') as file_obj:
        for line in file_obj:
            subs = line.split(':')
            subject[subs[0]] = get_hours(subs[1])
    print(subject)


def get_hours(part_string):
    new_string = ''
    for char in part_string:
        new_string += char if char.isdigit() else ' '

    count_hours = sum(map(int, new_string.split()))

    return count_hours


def task7():

    """
        Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
        название, форма собственности, выручка, издержки.

        Пример строки файла: firm_1 ООО 10000 5000.

        Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
        Если фирма получила убытки, в расчет средней прибыли ее не включать.

        Далее реализовать список.
        Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
        Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

        Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

        Итоговый список сохранить в виде json-объекта в соответствующий файл.
    :return:
    """

    my_list = []
    firms = {}
    avg_profit = {'average_profit': 0}
    with open('task7.txt', 'r') as file_obj:
        for line in file_obj:
            name, form, proceeds, costs = line.split()
            firms[name] = float(proceeds) - float(costs)
        profit = [elem for elem in firms.values() if elem > 0]
        my_list.append(firms)
        avg_profit['average_profit'] = sum(profit) / len(profit) if len(profit) != 0 else 0
        my_list.append(avg_profit)

    with open('task7.json', 'w') as f_obj:
        json.dump(my_list, f_obj)


if __name__ == "__main__":

    print("Выполняется задание 1")
    task1()

    print("Выполняется задание 2")
    task2()

    print("Выполняется задание 3")
    task3()

    print("Выполняется задание 4")
    task4()

    print("Выполняется задание 5")
    task5()

    print("Выполняется задание 6")
    task6()

    print("Выполняется задание 7")
    task7()

