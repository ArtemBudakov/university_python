import math


def distance(x1: float = 0, y1: float = 0, x2: float = 0, y2: float = 0):
    print(f"distance between x1, y1 and x2, y2: {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}")


if __name__ == '__main__':

    values_list = [float(value) for value in (input("write x1, y1 and x2, y2: ")).split()]
    distance(x1=values_list[0], y1=values_list[1], x2=values_list[2], y2=values_list[3])







