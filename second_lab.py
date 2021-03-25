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
        pass

    def four(self):
        pass

    def five(self):
        pass

    def six(self):
        pass

    def seven(self):
        pass


if __name__ == '__main__':
    l1 = Lists()
    # l1.one()
    l1.two()
