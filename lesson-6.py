from time import sleep


def task1():

    """
    Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
    :return:
    """

    traffic_light = TrafficLight(15)
    traffic_light.running()


class TrafficLight:

    # Атрибуты
    __color = ({'color': 'Красный', 'duration': 7},
               {'color': 'Желтый', 'duration': 2},
               {'color': 'Зеленый', 'duration': 5})

    def __init__(self, duration):
        """
            Функция инициализаци класса.
        :param duration: int время действия светофора
        """
        self.duration = duration

    def running(self):

        """
            Функция отвечает за работу светофора.

        :return:
        """
        current_color = 0
        while self.duration > 0:
            print(f'Светофор переключается \n {self.__color[current_color]["color"]}')
            sleep(self.__color[current_color]["duration"])
            self.duration -= self.__color[current_color]["duration"]
            current_color = 0 if current_color == 2 else current_color + 1


def task2():

    """

    Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

    :return:
    """

    road_to_village = Road(20, 5000)
    print(f'Для покрытия дороги требуется {road_to_village.road_surface()}т асфальта')


class Road:

    def __init__(self, _length, _width):
        """
        Функция инициализации класса.
        :param _length: float длина дороги
        :param _width: float ширина дороги
        """
        self.length = _length
        self.width = _width
        self.weight = 25
        self.thickness = 5

    def road_surface(self):

        """
            Функция подсчитываем массу требуемого асфальта, для покрытия полотна дороги
        :return: float масса асфальта (тонн)
        """
        return self.length * self.width * self.weight * self.thickness / 1000


def task3():

    """
        Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
        income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
        содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
        Создать класс Position (должность) на базе класса Worker.
        В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
        и дохода с учетом премии (get_total_income).
        Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
        проверить значения атрибутов, вызвать методы экземпляров).
    :return:
    """

    manager = Position('Иван', 'Иванов', 'менеджер по продажам', 100000, 25000)
    print(f'ФИО сотрудника: {manager.get_full_name()}')
    print(f'Зарплата сотрудника: {manager.get_total_income()}')


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        """
        Функция инициализации класса.
        :param name: string Имя сотрудника
        :param surname: string Фамилия сотрудника
        :param position: string Должность сотрудника
        :param wage: float Оклад
        :param bonus: float Бонус
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        """
            Функция возвращает полное имя сотрудника.
        :return: string
        """

        return f"{self.name}  {self.surname}"

    def get_total_income(self):

        """
            Функция возвращает заработную плату сотрудника.
        :return: string
        """

        return self._income.get("wage") + self._income.get("bonus")


def task4():
    """
    Реализуйте базовый класс Car.
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
    повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    :return:
    """
    porsche = SportCar(100, 'Red', 'Porsche', False)
    bmw = TownCar(120, 'White', 'BMW', False)
    lada = WorkCar(70, 'Rose', 'Lada', True)
    ford = PoliceCar(110, 'Blue', 'Ford', True)
    print(lada.turn("left"))
    print(f'When {bmw.turn("right")}, then {porsche.stop()}')
    print(f'{lada.go()} with speed exactly {lada.show_speed()}')
    print(f'{lada.name} is {lada.color}')
    print(f'Is {porsche.name} a police car? {porsche.is_police}')
    print(f'Is {lada.name}  a police car? {lada.is_police}')
    print(porsche.show_speed())
    print(bmw.show_speed())
    print(ford.show_speed())


class Car:

    def __init__(self, speed, color, name, is_police):
        """
        Фукнция инициалзиации класса.
        :param speed: float Скорость машины
        :param color: string Цвет машины
        :param name: string Наименование машины
        :param is_police: bool Признак полиция или нет
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """
        Функция движения машины.
        :return:
        """
        return f"{self.name} is started"

    def stop(self):
        """
        Функция остановки машины.
        :return:
        """
        return f"{self.name} is stopped"

    def turn(self, direction):
        """
        Фукнция поворота машины.
        :param direction: string Направление поворота машины
        :return:
        """
        return f"{self.name} is turned {direction}"

    def show_speed(self):
        """
        Функция показывает скорость машины.
        :return:
        """
        return f"Current speed {self.name} is {self.speed}"


class TownCar(Car):

    def show_speed(self):
        """
        Функция показывает скорость машины или выводит предупреждение о превышении скорости.
        :return:
        """
        return warning_speed(60) if self.speed > 60 else f"Current speed {self.name} is {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        """
        Функция инициализации класса.
        :param speed: float Скорость машины
        :param color: string Цвет машины
        :param name: string Наименование машины
        :param is_police: bool Признак полиция или нет
        """
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        """
        Функция показывает скорость машины или выводит предупреждение о превышении скорости.
        :return:
        """
        return warning_speed(40) if self.speed > 40 else f"Current speed {self.name} is {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        """
        Функция инициализации класса.
        :param speed: float Скорость машины
        :param color: string Цвет машины
        :param name: string Наименование машины
        :param is_police: bool Признак полиция или нет
        """
        super().__init__(speed, color, name, is_police)


def warning_speed(speed):
    """
    Функция выводит пердупреждение о превышении скорости
    :param speed:
    :return:
    """
    return f"Превышена скорость движения автомобиля, допустимая скорость движения {speed}"


def task5():

    """
    Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
    :return:
    """
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())


class Stationery:

    def __init__(self, tittle):
        """
        Функция инициализации класса.
        :param tittle: string Наименование
        """
        self.tittle = tittle

    def draw(self):
        """
        Функция отрисовки
        :return:
        """
        return f"Запск отрисовки"


class Pen(Stationery):

    def draw(self):
        """
        Функция отрисовки
        :return:
        """
        return f"Запуск отрисовки {self.tittle}"


class Pencil(Stationery):

    def draw(self):
        """
        Функция отрисовки
        :return:
        """
        return f"Запуск отрисовки {self.tittle}"


class Handle(Stationery):

    def draw(self):
        """
        Функция отрисовки
        :return:
        """
        return f"Запуск отрисовки {self.tittle}"


if __name__ == "__main__":

    print("Выполняется задание №1")
    task1()

    print("Выполняется задание №2")
    task2()

    print("Выполняется задание №3")
    task3()

    print("Выполняется задание №4")
    task4()

    print("Выполняется задание №5")
    task5()