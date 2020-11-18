def task1():
    user_number1 = int(input("Введите числитель: "))
    user_number2 = int(input("Введите знаменатель: "))
    print(division_of_numbers(user_number1, user_number2))


def division_of_numbers(number1, number2):
    """
        Функция принимает два параметра и возвращает результат деления этих параметров.

        :param number1: type int
        :param number2: type int
        :return:
    """

    try:
        return number1 / number2
    except ZeroDivisionError:
        print("Деление на ноль")


def task2():
    user_name = input("Введите имя: ")
    user_female = input("Введите фамилию: ")
    user_year = input("Введите год рождения: ")
    user_city = input("Введите город проживания: ")
    user_email = input("Введите электронную почту: ")
    user_phone = input("Введите мобильный телефон: ")

    set_user_data_description(city=user_city, phone=user_phone, name=user_name,female=user_female,year=user_year, email=user_email)


def set_user_data_description(name, female, year, city, email, phone):
    print(f"{name} {female} {year} {city} {email} {phone}")


def task3():
    number1 = int(input("Введите число №1: "))
    number2 = int(input("Введите число №2: "))
    number3 = int(input("Введите число №3: "))
    print(my_func(number1, number2, number3))


def my_func(num1, num2, num3):
    return num1 + num2 + num3 - min(num1, num2, num3)


def task4():
    degree = 0
    basis = 0

    while basis <= 0 <= degree:
        basis = float(input("Введите основание (действительное положительное число): "))
        degree = int(input("Введите степень (целое отрицательное число): "))

    print(number_pow(basis, degree))
    print(number_pow_lib(basis, degree))


def number_pow_lib(x, y):
    return x ** y


def number_pow(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x

    return 1 / res


def task5():
    sum_numbers = 0
    while True:
        numbers = input("Введите строку чисел. Используйте стоп-символ 'q' для выхода из цикла ").split()
        for number in numbers:
            if number.upper() == "Q":
                break
            else:
                sum_numbers += int(number)

        print(sum_numbers)

        if number.upper() == "Q":
            break


def task6():
    phrase = input("Введите слово или фразу: ").lower().split()
    print(' '.join(int_func(text) for text in phrase))


def int_func(text):
    return ''.join(text[i].upper() if i == 0 else text[i] for i in range(len(text)))


if __name__ == '__main__':

    # Задание 1
    print("Выполняется задание №1")
    task1()

    # Задание 2
    print("Выполняется задание №2")
    task2()

    # Задание 3
    print("Выполняется задание №3")
    task3()

    # Задание 4
    print("Выполняется задание №4")
    task4()

    # Задание 5
    print("Выполняется задание №5")
    task5()

    # Задание 6
    print("Выполняется задание №6")
    task6()
