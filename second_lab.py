import random


def list_one():
    """Сгенерировать список из 10 последовательных чисел от 1 до 10.
    Вывести на экран все элементы с нечетными индексами"""
    my_list = [element for element in range(1, 10)]  # каждый элемент в диапазоне от 1 до 10
    for index, value in enumerate(my_list):
        if index % 2:
            print(my_list[index])  # вывести элемент массива по его индексу, если инекс не чётный


def list_two():
    """Сгенерировать список из 20 чисел из любого диапазона.
    Вывести на экран все четные элементы и их индексы"""
    my_list: list = []

    while len(my_list) < 20:
        my_list.append(random.random())  # добавить в my_list случайное значение

    for index, value in enumerate(my_list):
        if index % 2 == 0:
            print(f" el = {my_list[index]}, index = {index}")  # вывод элемента и его индекса, если индекс нечётный


def list_three():
    """Сгенерировать список из 10 случайных целых чисел из любого диапазона (для генерации случайных
    элементов использовать модуль random
    https://pythonworld.ru/moduli/modul-random.html)
    Выведете список на экран. Отсортируйте список по возрастанию и по убыванию.
    Выведете на экран оба отсортированных списка."""
    my_list: list = []

    while len(my_list) < 10:
        my_list.append(random.randint(-99999999, 99999999))  # добавить в my_list элемент значение в
        # промежутке от -99999999 до 99999999 пока количество элементов не будет равно 10

    print(f"primary list: {my_list}\n")     # вывод исходного массима
    my_list.sort()                          # сортировка массива
    print(f"sorted asc list: {my_list}\n")  # вывод отсортированного массива по алфавиту и увеличению элементов
    my_list.sort(reverse=True)              # реверсивная сортировка массива
    print(f"sorted desc list: {my_list}")   # вывод реверсивно отсортированного массива


def list_four():
    """Сгенерировать список из 10 случайных целых чисел из любого диапазона Выведете список на экран.
    Выведите все элементы этого списка, которые больше предыдущего элемента"""
    my_list: list = []

    while len(my_list) < 10:
        my_list.append(random.random())  # добавить в my_list элемент значение в
        # пока количество элементов не будет равно 10

    print(f"primary list: {my_list}\n")  # вывод исходного массива

    compare = my_list[0]    # переменная для хранения последнего наибольшего элемента, которой присваивается
                            # значение первого элемента массива
    for el in my_list:
        if el > compare:    # если текущий элемент больше, чем последний наибольший сохранённый
            print(el)       # вывод элемента
            compare = el    # замена последнего наибольшего элемента текущим элементом


def list_five():
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
    max_el_index = 0                            # переменная для хранения индекса максимального элемента
    max_el = my_list[max_el_index]              # переменная для хранения значения максимального элемента
    for index, el in enumerate(my_list):
        if el > max_el:                         # если текущий элемент больше, чем хранимое значение
            max_el, max_el_index = el, index    # то присвоить значение текущего элемента и его индекс переменным

    print(f"element = {max_el}, index = {max_el_index}")


def list_six():
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
        if index % 2:  # если есть остаток, значит это второй элемент, значит его
                       # значение можно поменять с предыдущим элементом
            my_list[index - 1], my_list[index] = my_list[index], my_list[index - 1]  # по аналогии a, b = b, a

    print(f"changed list: {my_list}\n")


def list_seven():
    """Сгенерировать список из 10 случайных целых чисел из любого диапазона. Выведете список на экран.
    Поменяйте местами минимальный и максимальный элемент этого списка."""
    my_list: list = []

    while len(my_list) < 10:
        my_list.append(random.random())

    print(f"primary list: {my_list}\n")

    my_list.sort()
    print(f"asc list: {my_list}\n")
    index_min_value, index_max_value = 0, 0  # переменные для хранения индекса индекса с минимальным и
                                             # максимальным значением
    min_value, max_value = my_list[index_min_value], my_list[index_max_value]  # переменные для хранения значений
    for index, el in enumerate(my_list):
        if el > max_value:              # если текущий элемент больше, чем хранимый, то
            max_value = el              # положить текущее значение в переменную
            index_max_value = index     # положить индекс этого элемента в переменную
        elif el < min_value:            # если текущий элемент меньше, чем хранимый, то
            min_value = el              # положить текущий элемент в переменную
            index_min_value = index     # положить индекс этого элемента в переменную
    my_list[index_min_value], my_list[index_max_value] = my_list[index_max_value], my_list[index_min_value]
    # меняем минимальный и максимальный элемент в массиве по аналогии с a, b = b, a
    print(f"switched max and min values: {my_list}")


def string_one():
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


def string_two():
    """Введите строку с клавиатуры, состоящую из слов, разделенных пробелами.
    Определите, сколько в ней слов."""
    string_entered = str(input("write a message: "))
    words_counter = len(string_entered.split())
    print(f"words: {words_counter}")


def string_three():
    """Введите строку с клавиатуры. Разрежьте ее на две равные части (если длина строки — четная,
    а если длина строки нечетная, то длина первой части должна быть на один символ больше).
    Переставьте эти две части местами, результат запишите в новую строку и выведите на экран."""
    string_entered = str(input("write a message: "))
    if len(string_entered) % 2 == 0:  # если длина строки чётная
        first_part = string_entered[:len(string_entered) // 2]  # первая часть строки
        second_part = string_entered[len(string_entered) // 2:] # вторая часть строки
        print(f"half and half: {second_part} and "
              f"{first_part}")
    else:  # если длина строки нечётная
        first_part = string_entered[:len(string_entered) // 2 + 1]  # первая часть строки
        second_part = string_entered[len(string_entered) // 2 + 1:] # вторая часть строки на символ больше
        print(f"half and half: {second_part} and "
              f"{first_part}")


def string_four():
    """Введите строку с клавиатуры, состоящую ровно из двух слов, разделенных пробелом.
    Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку."""
    string_entered = str(input("write a message using only two words with space between: "))
    # шаблон для разделения строк - [начало, конец, шаг]
    word_second = string_entered[string_entered.find(' ') + 1:]  # взять строку, которая начнётся с пробела
    word_first = string_entered[:string_entered.find(' ')]       # взять строку, которая закончится пробелом
    print(f"words: {word_second} and {word_first}")


def string_five():
    """Введите строку с клавиатуры. Если в этой строке буква f встречается только один раз, выведите её индекс.
    Если она встречается два и более раз, выведите индекс её первого и последнего появления.
    Если буква f в данной строке не встречается, ничего не выводите."""
    string_entered = str(input("write a message: "))
    if string_entered.count("f") == 1:
        print(f'only one: {string_entered.find("f")}')
    elif string_entered.count("f") == 2:
        print(f'only twice: {string_entered.find("f"), string_entered.rfind("f")}')


def string_six():
    """Введите строку с клавиатуры, в которой буква h встречается минимум два раза.
    Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними"""
    string_entered = str(input("write a message: "))
    string_result = string_entered[:string_entered.find('h')] + string_entered[string_entered.rfind('h') + 1:]
    # берём часть строки с начала и ДО первого символа 'h', затем берём часть строки ПОСЛЕ последнего символа 'h'
    print(f"Output: {string_result}")


def string_seven():
    """Введите строку с клавиатуры. Замените в этой строке все цифры 1 на слово one"""
    string_entered = str(input("write a message: "))
    string_result = string_entered.replace('1', 'one')
    #  заменить в введённом сообщении все '1' на 'one'
    print(f"'one' instead '1': {string_result}")


def dict_one():
    """Введите строку с клавиатуры. Посчитайте, сколько раз каждое слово в строке встречалось ранее.
    Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки"""
    string_entered = str(input("write a message: "))
    counter: dict = {}  # словарь для подсчёта слов
    dict_my = string_entered.split()

    for el in dict_my:                      # для каждого элемента в моём словаре
        try:                                # попробуй сделать
            counter[el] += 1                # найти в словаре для подсчёта ключ, которому равен ключ 'el',
                                            # и увеличить 'value' для него на 1
        except KeyError:                    # Иначе, такого элемента в моём словаре нет, то
            counter[el] = 1                 # создать его с ключём, равным 'el' и 'value' = 1

    for word in dict_my:                    # для каждого слова (ключа) в моём словаре
        print(f"{word} {counter[word]}")    # вывести слово(key) и (value) число, обозначающее сколько раз
                                            # встречалось данное слово


def dict_two():
    """Введите строку с клавиатуры.
    Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее."""
    string_entered = str(input("write a message: "))
    counter: dict = {}  # словарь для подсчёта слов

    for word in string_entered.split():         # для каждого слова в введённой строке
        try:                                    # попытайся
            counter[word] += 1                  # найти элемент, ключ(key) которого равен 'word'
        except KeyError:                        # если такого элемента нет, то
            counter[word] = 0                   # создать ключ(key) с значением 'word' и добавить к нему 'value' = 0
        finally:                                # наконец-то (выполняется всегда, не зависимо от того,
                                                # что отработало - try или except
            print(f"{word} - {counter[word]}")  # вывести word(слово) и счётчик - сколько раз это слово встречалось


def dict_three():
    """Введите строку с клавиатуры. Составьте словарь, состоящий из уникальных слов, содержащихся в этой строке.
    Выведете на экран последовательность из индексов (ключей) этого словаря, в том порядке,
    в котором они встречаются в строке"""
    string_entered = str(input("write a message: "))
    counter_dict: dict = {}  # словарь для подсчёта слов

    for word in string_entered.split():  # для каждого слова в введённой строке
        if word in counter_dict:         # если слово уже существует в словаре для подсчёта
            counter_dict[word] = False   # то значение для этого слова False - значит оно не уникально
        else:                            # иначе
            counter_dict[word] = True    # создать слово с True - значит оно уникально

    counter: int = 1                     # счётчик слова в введённой строке
    for word in string_entered.split():  # для каждого слова в введённой строке
        if counter_dict[word] is False:  # если слово в словаре не уникально, то
            value = 0                    # значение 0
        else:                            # иначе, если слово в словаре уникально, то
            value = counter              # номер уникального слова в строке = счётчику слова в введённой строке
            counter += 1                 # добавить счётчику 1
        print(f"{word} {value}")         # вывести слово и его порядковое место в введённом предложении


def dict_four():
    """Составьте «словарь синонимов» следующим образом: сначала введите количество вводимых пар ключ-значение.
    Каждое слово является синонимом к парному ему слову.
    Затем введите слово, для которого надо вывести синоним"""
    counter_message = int(input("write count of message: "))  # вводим количество вводимых пар
    counter_dict: dict = {}                                   # словарь для синонимов

    while counter_message > 0:                                          # пока счётчик вводимых слов не равен 0
        string_entered = str(input("write a message: "))                # получаем введённое сообщение с двумя словами
        string_entered_list = string_entered.split()                    # создаём массив из двух введённых слов
        counter_dict[string_entered_list[1]] = string_entered_list[0]   # кладём в словарь синонимы из массива
        counter_message -= 1                                            # счётчик вводимых пар -1

    word = str(input('write a word: '))  # получаем слово синоним
    antonym = counter_dict[word]         # получаем слово антоним
    print(f"antonym: {antonym}")         # выводим антоним


def dict_five():
    """Введите строку с клавиатуры. Подсчитайте количество появлений каждого символа в строке"""
    string_entered = str(input("write a message: "))
    string_entered = string_entered.replace(" ", "")
    counter_dict: dict = {}

    for symbol in string_entered:               # для каждого символа в строке
        try:                                    # попытаться
            counter_dict[symbol] += 1           # найти символ в словаре и увеличить value на 1
        except KeyError:                        # если символа нет в словаре, то
            counter_dict[symbol] = 1            # добавить его и установить value равным 1

    for word in counter_dict:                   # для каждого слова в словаре
        print(f"{word} {counter_dict[word]}")   # вывести слово и value - количество появлений в строке


def dict_six():
    """Введите строку с клавиатуры. Выведите слово, которое в этом тексте встречается чаще всего."""
    string_entered = str(input("write a message: "))
    counter_dict: dict = {}

    for el in string_entered.split():                   # для каждого элемента в введённой строке
        try:                                            # попытаться
            counter_dict[el] += 1                       # найти элемент в словаре и увеличить value на 1
        except KeyError:                                # иначе, если элемент не найден
            counter_dict[el] = 1                        # добавить элемент в словарь и установить value равным 1

    current = next(iter(counter_dict))                  # получаем слово первого элемента в моём словаре
    for word in counter_dict:                           # для каждого слова в моём словаре
        if counter_dict[word] > counter_dict[current]:  # если value слова больше, чем value текущего слова, то
            current = word                              # текущее слово = новое слово
    print(f"more often: {current}")                     # вывести текущее слово, которое встречается чаще отсальных


if __name__ == '__main__':

    """Списки"""
    list_one()
    list_two()
    list_three()
    list_four()
    list_five()
    list_seven()

    """Строки"""
    string_one()
    string_two()
    string_three()
    string_four()
    string_five()
    string_six()
    string_seven()

    """словари"""
    dict_one()
    dict_two()
    dict_three()
    dict_four()
    dict_five()
    dict_six()
