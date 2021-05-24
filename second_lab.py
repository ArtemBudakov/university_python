import random


class Lists:

    def one(self):
        """Сгенерировать список из 10 последовательных чисел от 1 до 10.
        Вывести на экран все элементы с нечетными индексами"""
        my_list = [element for element in range(1, 10)]
        for index, value in enumerate(my_list):
            if index % 2:
                print(my_list[index])

    def two(self):
        """Сгенерировать список из 20 чисел из любого диапазона.
        Вывести на экран все четные элементы и их индексы"""
        my_list: list = []

        while len(my_list) < 20:
            my_list.append(random.random())

        for index, value in enumerate(my_list):
            if index % 2 == 0:
                print(f" el = {my_list[index]}, index = {index}")

    def three(self):
        """Сгенерировать список из 10 случайных целых чисел из любого диапазона (для генерации случайных
        элементов использовать модуль random
        https://pythonworld.ru/moduli/modul-random.html)
        Выведете список на экран. Отсортируйте список по возрастанию и по убыванию.
        Выведете на экран оба отсортированных списка."""
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.randint(-99999999, 99999999))

        print(f"primary list: {my_list}\n")
        my_list.sort()
        print(f"sorted asc list: {my_list}\n")
        my_list.sort(reverse=True)
        print(f"sorted desc list: {my_list}")

    def four(self):
        """Сгенерировать список из 10 случайных целых чисел из любого диапазона Выведете список на экран.
        Выведите все элементы этого списка, которые больше предыдущего элемента"""
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
        """Сгенерировать список из 10 случайных целых чисел из любого диапазона.
        Выведете список на экран. Выведите значение наибольшего элемента в списке,
        а затем индекс этого элемента в списке.
        Если наибольших элементов несколько, выведите индекс первого из них."""
        my_list: list = []

        while len(my_list) < 10:
            my_list.append(random.random())

        print("primary list:")
        for el in my_list:
            print(el)
        max_el_index = 0
        max_el = my_list[max_el_index]
        for index, el in enumerate(my_list):
            if el > max_el:
                max_el, max_el_index = el, index

        print(f"element = {max_el}, index = {max_el_index}")

    def six(self):
        """Сгенерировать список из 10 случайных целых чисел из любого диапазона.
        Выведете список на экран. Отсортируйте список по возрастанию,
        переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
        Если элементов нечетное число, то последний элемент остается на своем месте"""
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
        """Сгенерировать список из 10 случайных целых чисел из любого диапазона. Выведете список на экран.
        Поменяйте местами минимальный и максимальный элемент этого списка."""
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
        """Введите строку с клавиатуры. Сначала выведите третий символ этой строки.
        Во второй строке выведите предпоследний символ этой строки.
        В третьей строке выведите первые пять символов этой строки.
        В четвертой строке выведите всю строку, кроме последних двух символов.
        В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
        В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
        В седьмой строке выведите все символы в обратном порядке.
        В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
        В девятой строке выведите длину данной строки"""
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
        """Введите строку с клавиатуры, состоящую из слов, разделенных пробелами.
        Определите, сколько в ней слов."""
        string_entered = str(input("write a message: "))

        print(f"words: {len(string_entered.split())}")

    def three(self):
        """Введите строку с клавиатуры. Разрежьте ее на две равные части (если длина строки — четная,
        а если длина строки нечетная, то длина первой части должна быть на один символ больше).
        Переставьте эти две части местами, результат запишите в новую строку и выведите на экран."""
        string_entered = str(input("write a message: "))
        if len(string_entered) % 2 == 0:
            print(f"half and half: {string_entered[len(string_entered) // 2:]} and "
                  f"{string_entered[:len(string_entered) // 2]}")
        else:
            print(f"half and half: {string_entered[len(string_entered) // 2 + 1:]} and "
                  f"{string_entered[:len(string_entered) // 2 + 1]}")

    def four(self):
        """Введите строку с клавиатуры, состоящую ровно из двух слов, разделенных пробелом.
        Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку."""
        string_entered = str(input("write a message using only two words with space between: "))

        print(f"words: {string_entered[string_entered.find(' ') + 1:]} and {string_entered[:string_entered.find(' ')]}")

    def five(self):
        """Введите строку с клавиатуры. Если в этой строке буква f встречается только один раз, выведите её индекс.
        Если она встречается два и более раз, выведите индекс её первого и последнего появления.
        Если буква f в данной строке не встречается, ничего не выводите."""
        string_entered = str(input("write a message: "))
        if string_entered.count("f") == 1:
            print(f'only one: {string_entered.find("f")}')
        elif string_entered.count("f") == 2:
            print(f'only twice: {string_entered.find("f"), string_entered.rfind("f")}')

    def six(self):
        """Введите строку с клавиатуры, в которой буква h встречается минимум два раза.
        Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними"""
        string_entered = str(input("write a message: "))
        print(f"Output: {string_entered[:string_entered.find('h')] + string_entered[string_entered.rfind('h') + 1:]}")

    def seven(self):
        """Введите строку с клавиатуры. Замените в этой строке все цифры 1 на слово one"""
        string_entered = str(input("write a message: "))
        print(f"'one' instead '1': {string_entered.replace('1', 'one')}")


class Dicts:

    def one(self):
        """Введите строку с клавиатуры. Посчитайте, сколько раз каждое слово в строке встречалось ранее.
        Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки"""
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
        """Введите строку с клавиатуры.
        Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее."""
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
        """Введите строку с клавиатуры. Составьте словарь, состоящий из уникальных слов, содержащихся в этой строке.
        Выведете на экран последовательность из индексов (ключей) этого словаря, в том порядке,
        в котором они встречаются в строке"""
        string_entered = str(input("write a message: "))
        counter_dict: dict = {}

        for el in string_entered.split():
            if el in counter_dict:
                counter_dict[el] = False
            else:
                counter_dict[el] = True

        counter: int = 1
        for word in string_entered.split():
            if counter_dict[word] is False:
                value = 0
            else:
                value = counter
                counter += 1
            print(f"{word} {value}")

    def four(self):
        """Составьте «словарь синонимов» следующим образом: сначала введите количество вводимых пар ключ-значение.
        Каждое слово является синонимом к парному ему слову.
        Затем введите слово, для которого надо вывести синоним"""
        counter_message = int(input("write count of message: "))
        counter_dict: dict = {}

        while counter_message > 0:
            string_entered = str(input("write a message: "))
            string_entered_list = string_entered.split()
            counter_dict[string_entered_list[1]] = string_entered_list[0]
            counter_message -= 1

        print(f"antonym: {counter_dict[str(input('write a word: '))]}")

    def five(self):
        """Введите строку с клавиатуры. Подсчитайте количество появлений каждого символа в строке"""
        string_entered = str(input("write a message: "))
        string_entered = string_entered.replace(" ", "")
        counter_dict: dict = {}

        for el in string_entered:
            try:
                counter_dict[el] += 1
            except KeyError:
                counter_dict[el] = 1

        for word in counter_dict:
            print(f"{word} {counter_dict[word]}")

    def six(self):
        """Введите строку с клавиатуры. Выведите слово, которое в этом тексте встречается чаще всего."""
        string_entered = str(input("write a message: "))
        counter_dict: dict = {}

        for el in string_entered.split():
            try:
                counter_dict[el] += 1
            except KeyError:
                counter_dict[el] = 1

        current = next(iter(counter_dict))
        for word in counter_dict:
            if counter_dict[word] > counter_dict[current]:
                current = word
        print(f"more often: {current}")


if __name__ == '__main__':
    l1 = Lists()
    # l1.one()
    # l1.two()
    # l1.three()
    # l1.four()
    l1.five()
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
    # d1.two()
    # d1.three()
    # d1.four()
    # d1.five()
    # d1.six()
