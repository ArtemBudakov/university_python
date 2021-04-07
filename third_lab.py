import math


def distance(x1: float = 0, y1: float = 0, x2: float = 0, y2: float = 0):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def miles_to_km(miles: float = 0):
    return miles * 1.609


def mean(args):
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
    result: str = ""

    for arg in args:
        result += arg

    return result


def add(var1, var2):
    return var1 + var2


def call(function, var1, var2):
    result = function(var1, var2)
    return result


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


class Circle:
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
    # c1 = Circle(pc1, 1)
    # c2 = Circle(pc2, 3)
    # print(c1.do_intersect(c2))
    #
    # print(c1 == c2)
    # print(c1 < c2)
    # print(c1 > c2)

    pass
