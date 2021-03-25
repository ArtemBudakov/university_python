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


class Strings:

    def one(self):
        string_entered = str(input("write a message: "))
        print(f"third symbol: {string_entered[2]}\n"
              f"before last symbol: {string_entered[-2]}\n"
              f"first five symbols: {string_entered[0: 5]}\n"
              f"without two last symbols: {string_entered[:-2:]}\n"
              f"an even indexes: {string_entered[::2]}\n"
              f"an odd indexes: {string_entered[1::2]}\n"
              f"reversed: {string_entered[::-1]}\n"
              f"reversed and through one: {string_entered[::-2]}\n"
              f"current length: {len(string_entered)}")

    def two(self):
        string_entered = str(input("write a message: "))

        print(f"words: {len(string_entered.split())}")

    def three(self):
        string_entered = str(input("write a message: "))
        if len(string_entered) % 2 == 0:
            print(f"half and half: {string_entered[len(string_entered) // 2:]} and "
                  f"{string_entered[:len(string_entered) // 2]}")
        else:
            print(f"half and half: {string_entered[len(string_entered) // 2 + 1:]} and "
                  f"{string_entered[:len(string_entered) // 2 + 1]}")

    def four(self):
        string_entered = str(input("write a message using only two words with space between: "))

        print(f"words: {string_entered[string_entered.find(' ') + 1:]} and {string_entered[:string_entered.find(' ')]}")

    def five(self):
        string_entered = str(input("write a message: "))
        if string_entered.count("f") == 1:
            print(f'only one: {string_entered.find("f")}')
        elif string_entered.count("f") == 2:
            print(f'only twice: {string_entered.find("f"), string_entered.rfind("f")}')

    def six(self):
        string_entered = str(input("write a message: "))
        print(f"Output: {string_entered[:string_entered.find('h')] + string_entered[string_entered.rfind('h') + 1:]}")

    def seven(self):
        string_entered = str(input("write a message: "))
        print(f"'one' instead '1': {string_entered.replace('1', 'one')}")


class Dicts:

    def one(self):
        string_entered = str(input("write a message: "))
        counter: dict = {}

        for el in string_entered.split():
            try:
                counter[el] += 1
            except KeyError:
                counter[el] = 1

        for word in string_entered.split():
            print(f"{word} {counter[word]}")

    def two(self):
        pass
        string_entered = str(input("write a message: "))
        counter: dict = {}

        for el in string_entered.split():
            try:
                counter[el] += 1
            except KeyError:
                counter[el] = 0
            finally:
                print(f"{el} - {counter[el]}")

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
    # l1.two()
    # l1.three()
    # l1.four()
    # l1.five()
    # l1.six()
    # l1.seven()

    s1 = Strings()
    # s1.one()
    # s1.two()
    # s1.three()
    # s1.four()
    # s1.five()
    # s1.six()
    # s1.seven()

    d1 = Dicts()
    # d1.one()
    d1.two()
    d1.three()
    d1.four()
    d1.five()
    d1.six()
    d1.seven()
