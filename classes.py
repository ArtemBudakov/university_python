import math


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
    def __init__(self, x: float = 0, y: float = 0):  # конструктор класса, который отрабатывает всегда при создании
        self.x = x                                   # экземпляра этого класса
        self.y = y                                   # и помещает полученные аргументы х и у в переменные внутри класса

    def dist(self, other_point):  # метод dist, находит расстояние между точками по формуле ((x1-x2)^2 + (y1-y2)^2)^0.5
        result = ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5  # где 0.5 - получение
        return result                                                                    # квадратного корня


class Circle:
    """
    2.	Напишите класс Circle, представляющий круг. У этого класса должны быть: конструктор принимающий объект класса
    Point, точку центра круга, и число, радиус круга; атрибуты center и radius, возвращающие центр
    и радиус круга соответственно; метод square, который возвращает площадь круга.
    circ = Circle(Point(0, 3), 4)
    circ.radius == 4
    circ.center.x == 0

    Circle(Point(0, 0), 0).square() == 0

    3.	Доработайте класс Circle. Добавьте ему метод do_intersect, который будет принимать другой объект класса Circle
    и возвращать True или False в зависимости от того, пересекаются круги или нет.
    Весь остальной код класса вы можете скопировать из решения предыдущей задачи.

    4.	Добавьте возможность сравнивать объекты класса Circle. Больше будет тот круг, у которого площадь больше.
    """
    def __init__(self, point_object, circle_radius):  # конструктор класса Circle
        self.radius = circle_radius                   # присвоение аргументу класса значения из переменной,
                                                      # которое передано в момент создания экземпляра класса
        self.center_x = point_object.x                # присвоение значения X, которое берётся из аргумента класса point
        self.center_y = point_object.y                # присвоение значения Y, которое берётся из аргумента класса point
        self.point_object = point_object              # аргумент для хранения ссылки на объект point
        self.square = self.square_calculate()         # аргументу square присваивается значение, которое возвращает
                                                      # функция square - после расчёта площади круга

    def __eq__(self, other):             # эквивалентность (равенство). используется при сравнении двух экземпляров этого класса
        if self.square == other.square:  # если площать данного экземпляра равна площади другого экземпляра
            return True                  # то вернуть True (истина)
        else:                            # иначе
            return False                 # вернуть False (ложь)

    def __lt__(self, other):             # less then (меньше чем)
        if self.square < other.square:   # Если площать данного экземпляра меньше площади другого экземпляра
            return True
        else:
            return False

    def __gt__(self, other):             # greater then (больше чем)
        if self.square > other.square:   # если площать данного экземпляра больше площади другого экземпляра
            return True
        else:
            return False

    def square_calculate(self):  # метод (функция) для расчёта площади круга по формуле 2*П*r^2
        self.square = 3.14 * self.radius * self.radius
        return self.square

    def do_intersect(self, other_circle):  # метод (функция). принимает на вход другой экземпляр класса (другой круг)
        # считаем по формуле: d = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
        distance_between_circles = math.sqrt((other_circle.point_object.x - self.point_object.x) ** 2
                                             + (other_circle.point_object.y - self.point_object.y) ** 2)
        # если d (расстояние между кругами) больше чем модуль разности окружностей (r1 - r2)
        # и меньше суммы окружностей (r1 + r2), то возвращает True. если хотя бы одно условие не выполнилос, то False
        return abs(self.radius - other_circle.radius) <= distance_between_circles <= (self.radius + other_circle.radius)


    """5.	Все животные имеют между собой много общего. Они умеют издавать звуки и перемещатся.
    А еще у них есть имена, которые им дают при рождении. Это общее можно описать следующим классом:

    Создайте классы Dog и Snake, унаследовав их от Animal.
    Объект класса Dog должен издавать звук woof. Ходят собаки пешком. Поэтому при вызове метода move должен выводится
    текст "<Name> walks", где <Name> – это имя животного.
    Объект класса Snake должен издавать звук hsss. Змеи ползают. Поэтому при вызове метода move должен
    выводится текст "<Name> crawles", где <Name> – это имя животного.

    Примеры проверки работы написанных классов
    -> snake = Snake('John')
    -> snake.make_sound()
    John says hss
    -> snake.move()
    John crawles
    -> dog = Dog('Mike')
    -> dog.make_sound()
    Mike says woof
    ->dog.move()
    Mike walks
    """


class Animal:
    def __init__(self, name, sound):  # создаём конструктор класса Animal
        self.name = name              # инициализируем аргумент name для класса
        self.sound = sound            # инициализируем аргумент sound для класса

    def make_sound(self):
        print(f"{self.name} says {self.sound}")  # выводим информацию о том какой звук издаёт кто-то с именем {self.name}


class Dog(Animal):                              # Создаём класс Dog, который является наследником от Animal
    def __init__(self, name, sound='woof'):     # Создаём конструктор класса Dog. Если sound не указан
        super().__init__(name, sound)           # при создании, то будет woof по умолчанию
        self.name = name
        self.sound = sound

    def move(self):
        print(f"{self.name} walks")             # выводим информацию о том как передвигаются собаки


class Snake(Animal):                            # Создаём класс Snake, который является наследником от Animal
    def __init__(self, name, sound='hsss'):     # Cоздаём конструктор класса Snake. Если sound не указан
        super().__init__(name, sound)           # при создании, то будет hsss по умолчанию
        self.name = name
        self.sound = sound

    def move(self):
        print(f"{self.name} crawls")            # выводим информацию о том как передвигаются змеи


if __name__ == '__main__':

    # p1 = Point(1.5, 0)  # инициализируем (создаём) экземпляр точки с координатами x = 1.5, y = 0
    # p2 = Point(1.5, 2)  # инициализируем (создаём) экземпляр точки с координатами x = 1.5, y = 2
    # print(p1.dist(p2))  # в экземпляре p1 вызываем функцию dist и передаём этой функции экземпляр другой точки
    #
    # pc1 = Point(1, 2)             # инициализируем (создаём) экземпляр точки с координатами x = 1, y = 2
    # c1 = Circle(pc1, 5)           # инициализируем (создаём) экземпляр круга с точкой из pc1 и радиусом 5
    # print(c1.square_calculate())  # в экземпляре c1 вызываем метод(функци) для расчёта площади
    #                               # т.к. мы делаем это в конструкторе класса, то можно сделать так
    # print(c1.square)              # здесь мы получаем аргумент из экземпляра класса, не(!) вызывая функция для расчёта
    #
    # pc1_small = Point(1, 1)     # small. точка малого круга x = 1, y = 1
    # pc2_middle = Point(2, 2)    # middle. точка среднего круга x = 2, y = 2
    #
    # c1 = Circle(pc1_small, 1)   # создаём круг по точку малого(small) круга и радиусу 1
    # c2 = Circle(pc2_middle, 3)  # создаём круг по точку среднего(middle) круга и радиусу 3
    # print(c1.do_intersect(c2))  # проверяем пересекаются ли круги
    #
    # print(c1 == c2)             # сравниваем два круга на эквивалентность
    # print(c1 < c2)              # первый круг больше второго ? -> Если да, то true
    # print(c1 > c2)              # первый круг меньше второго ? -> Если да, то true
    #
    # pc3 = Point(5, 5)           # big. создание точки для большого круга x=5, y=5
    # c3 = Circle(pc3, 5)         # создание круга с точкой pc3 и радиусом 5
    # circle_list = [c3, c1, c2]  # создаём массив из трёх кругов
    #
    # print("before sort()")  # вывод названия объекта, его расположение в памяти и координаты точки центра этого круга
    # for el in circle_list:  # для всех кругов вывести название и расположение, координату Х, координату У
    #     print(f"el = {el}, x = {el.point_object.x}, y = {el.point_object.y}")
    #
    # circle_list.sort()      # сортировка массива из кругов исходя из их площадей (методы __eq__, __lt__, __gt__)
    #
    # print("after sort()")
    # for el in circle_list:  # то же самое, что и раньше, только после сортировки
    #     print(f"el = {el}, x = {el.point_object.x}, y = {el.point_object.y}")

    dog1 = Dog(name="Sharik")      # создаём экземпляр класса Dog с назваинем dog1, указываем имя = "Sharik"
    dog1.make_sound()              # вызываем метод make_sound для dog1
    dog1.move()                    # вызываем метод move для dog1

    snake1 = Snake(name="Zmeyaa")  # создаём экземпляр класса Snake с назваинем snake1, указываем имя = "Zmeyaa"
    snake1.make_sound()            # вызываем метод make_sound для snake1
    snake1.move()                  # вызываем метод move для snake1
