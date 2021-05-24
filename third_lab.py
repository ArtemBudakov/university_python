from abc import ABC, abstractmethod
import math


def distance(x1=0, y1=0, x2=0, y2=0):
    """1.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
    вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
    Считайте четыре действительных числа и выведите результат работы этой функции."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def miles_to_km(miles: float = 0):
    """2.	Напишите функцию `miles_to_km`, которая будет переводить мили в километры.
    В одной миле примерно 1.609 километров"""
    return miles * 1.609


def mean(args):
    """3.	Напишите функцию mean, которая будет считать среднее арифметическое переданных в нее аргументов"""
    """
    # equals
    average, counter = 0, 0
    for arg in args:
        average += arg
        counter += 1
    return average / counter
    """

    return sum(args) / len(args)


def concat(args):
    """4.	Напишите функцию concat, которая будет принимать произвольное число строк и объединять их в одну"""
    result: str = ""

    for arg in args:
        result += arg

    return result


def add(var1, var2):
    """5.	Напишите функцию call, которая будет принимать произвольную функцию,
    аргументы для неё и делать вызов переданной функции."""
    return var1 + var2


def add2(*args):
    """5.	Напишите функцию call, которая будет принимать произвольную функцию,
    аргументы для неё и делать вызов переданной функции."""
    result: float = 0
    for element in args:
        result += element
    return result


def call(function, var1, var2):
    """6.	Написать модуль, в котором содержатся все эти функции,
    а также отдельные скрипты проверки для каждой функции"""
    result = function(var1, var2)
    return result


class Point:
    """
    1.	Реализуйте класс Point (точка). У этого класса должны быть конструктор, принимающий два числа x и y,
    координаты точки на плоскости; атрибуты x и y через которые можно будет получить координаты точки;
    метод dist, который принимает еще один объект класса Point и находит эвклидово расстояние между двумя точками.
    Примеры вызова:
    p1 = Point(1.5, 1)
    p2 = Point(1.5, 2)
    p1.dist(p2) == 1
    """
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


class Circle:
    """
    2.	Напишите класс Circle, представляющий круг. У этого класса должны быть: конструктор принимающий объект класса
    Point, точку центра круга, и число, радиус круга; атрибуты center и radius, возвращающие центр
    и радиус круга соответственно; метод square, который возвращает площадь круга.
    circ = Circle(Point(0, 3), 4)
    circ.radius == 4
    circ.center.x == 0

    Circle(Point(0, 0), 0).square() == 0

    3.	Доработайте класс Circle. Добавьте ему метод do_intersect, который будет принимать другой объект класса Circle и возвращать True или False в зависимости от того, пересекаются круги или нет.
    Весь остальной код класса вы можете скопировать из решения предыдущей задачи.

    4.	Добавьте возможность сравнивать объекты класса Circle. Больше будет тот круг, у которого площадь больше.
    """
    def __init__(self, point_object, circle_radius):
        self.radius = circle_radius
        self.center = point_object
        self.point_object = point_object
        self.square = self.square()

    def __eq__(self, other):
        if self.square == other.square:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.square < other.square:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.square > other.square:
            return True
        else:
            return False

    def square(self):
        self.square = 3.14 * self.radius * self.radius
        return self.square

    def do_intersect(self, another_circle):
        distance_between_circles = math.sqrt((another_circle.point_object.x - self.point_object.x) ** 2
                                             + (another_circle.point_object.y - self.point_object.y) ** 2)
        return abs(self.radius - another_circle.radius) <= distance_between_circles <= (self.radius + another_circle.radius)


class Animal(ABC):
    """5.	Все животные имеют между собой много общего. Они умеют издавать звуки и перемещатся.
    А еще у них есть имена, которые им дают при рождении. Это общее можно описать следующим классом:

    Создайте классы Dog и Snake, унаследовав их от Animal.
    Объект класса Dog должен издавать звук woof. Ходят собаки пешком. Поэтому при вызове метода move должен выводится
    текст "<Name> walks", где <Name> – это имя животного.
    Объект класса Snake должен издавать звук hsss. Змеи ползают. Поэтому при вызове метода move должен
    выводится текст "<Name> crawles", где <Name> – это имя животного.

    Примеры проверки работы написанных классов
    >>> snake = Snake('John')
    >>> snake.make_sound()
    John says hss
    >>> snake.move()
    John crawles
    >>> dog = Dog('Mike')
    >>> dog.make_sound()
    Mike says woof
    >>> dog.move()
    Mike walks
    """
    def __init__(self, name, sound=None):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def __init__(self, name, sound='woof'):
        super().__init__(name, sound)

    def move(self):
        print(f"{self.name} walks")


class Snake(Animal):
    def __init__(self, name, sound='hsss'):
        super().__init__(name, sound)

    def move(self):
        print(f"{self.name} crawls")


if __name__ == '__main__':

    # first task - distance()
    # values_list = [float(value) for value in (input("write x1, y1 and x2, y2: ")).split()]
    # result = distance(x1=values_list[0], y1=values_list[1], x2=values_list[2], y2=values_list[3])
    # print(str(result))

    # second task - miles_to_km()
    # value = float(input("write miles in float: "))
    # result = miles_to_km(value)
    # print(str(result))

    # third task - mean()
    # values = [float(value) for value in (input("write numbers: ")).split()]
    # result = mean(values)
    # print(str(result))

    # fourth task - concat()
    # values = input("write numbers: ").split()
    # print(concat(values))

    # fifth task - call()
    # print(call(add, "dasdsad", "aaaaaaaaa"))
    # print(call(add, 1, 3))

    # p1 = Point(1.5, 0)
    # p2 = Point(1.5, 2)
    # print(p1.dist(p2))

    # pc1 = Point(1, 2)
    # c1 = Circle(pc1, 5)
    # print(c1.square())

    # pc1 = Point(0, 0)
    # pc2 = Point(0, 0)

    # pc1 = Point(1, 1)  # small
    # pc2 = Point(2, 2)  # middle

    # c1 = Circle(pc1, 1)
    # c2 = Circle(pc2, 3)
    # print(c1.do_intersect(c2))
    #
    # print(c1 == c2)
    # print(c1 < c2)
    # print(c1 > c2)

    # pc3 = Point(5, 5)  # big
    # c3 = Circle(pc3, 5)
    # circle_l = [c3, c1, c2]
    #
    # print("before sort()")
    # for el in circle_l:
    #     print(f"el = {el}, x = {el.point_object.x}, y = {el.point_object.y}")
    #
    # circle_l.sort()
    #
    # print("after sort()")
    # for el in circle_l:
    #     print(f"el = {el}, x = {el.point_object.x}, y = {el.point_object.y}")

    d1 = Dog(name="bars")
    d1.make_sound()
    d1.move()

    s1 = Snake(name="snake")
    s1.make_sound()
    s1.move()
