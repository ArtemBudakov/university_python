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


def call(function, args):
    """Strange task. I don't know how i must do it and why someone use it. skipped for now.
    https://stackoverflow.com/questions/40644740/what-is-the-difference-between-the-apply-function-and-a-function-call-using-th"""
    pass


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
    pass




