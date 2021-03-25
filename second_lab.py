import random


class Lists:

    def one(self):
        my_list = [element for element in range(1, 10)]
        for index, value in enumerate(my_list):
            if index % 2:
                print(my_list[index])

    def two(self):
        my_list: list = []

        while len(my_list) < 20:
            my_list.append(random.random())

        for index, value in enumerate(my_list):
            if index % 2 == 0:
                print(f" el = {my_list[index]}, index = {index}")

    def three(self):
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.randint(-99999999, 99999999))

        print(f"primary list: {my_list}\n")
        my_list.sort()
        print(f"sorted asc list: {my_list}\n")
        my_list.sort(reverse=True)
        print(f"sorted desc list: {my_list}")

    def four(self):
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.random())

        print(f"primary list: {my_list}\n")

        compare = my_list[0]
        for el in my_list:
            if el > compare:
                print(el)
                compare = el

    def five(self):
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.random())

        print(f"primary list: {my_list}\n")

        index = 0
        max_el = my_list[index]
        for index, el in enumerate(my_list):
            if el > max_el:
                max_el, index = el, index

        print(f"element = {max_el}, index = {index}")

    def six(self):
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.random())

        print(f"primary list: {my_list}\n")

        my_list.sort()
        print(f"asc list: {my_list}\n")

        for index, el in enumerate(my_list):
            if index % 2:
                my_list[index - 1], my_list[index] = my_list[index], my_list[index - 1]

        print(f"changed list: {my_list}\n")

    def seven(self):
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.random())

        print(f"primary list: {my_list}\n")

        my_list.sort()
        print(f"asc list: {my_list}\n")
        index_min_value, index_max_value = 0, 0
        min_value, max_value = my_list[index_min_value], my_list[index_max_value]
        for index, el in enumerate(my_list):
            if el > max_value:
                max_value = el
                index_max_value = index
            elif el < min_value:
                min_value = el
                index_min_value = index
        my_list[index_min_value], my_list[index_max_value] = my_list[index_max_value], my_list[index_min_value]
        print(f"switched max and min values: {my_list}")


if __name__ == '__main__':
    l1 = Lists()
    # l1.one()
    # l1.two()
    # l1.three()
    # l1.four()
    # l1.five()
    # l1.six()
    # l1.seven()
