
def sum_of_three():
    """Напишите программу, которая считывает три числа и выводит их сумму.Каждое число записано в отдельной строке."""

    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(f"{(a + b + c)}")


def length_of_legs():
    """
    Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
    Каждое число записано в отдельной строке
    """
    a = int(input('a = '))
    b = int(input('b = '))
    print(f"{((a + b) / 2)}")


def greetings():
    """
    Напишите прогрмамму, которая приветсвтует пользователя, вывлдя слово Hello, введенное имя и знаки препинания
    по образцу:
    Harry
    Hello, Harry!
    """
    name = input("write your name: ")
    print(f"Hello, {name}!")


def next_and_previous_numbers():
    """
    Напишите программу, которая считывает целое число и выводит текст, аналогичный приведённому в примере:
    >> 12345
    << The next number for the number 12345 is 12346.
    << The previous number for the number 12345 is 12344.
    """
    value = int(input("write number: "))
    print(f"The next number for the number {value} is {value + 1}.")
    print(f"The previous number for the number {value} is {value - 1}.")


def min_of_two_numbers():
    """
    Даны два целых числа. Выведите значение наименьшего из них.
    """
    a = int(input('a = '))
    b = int(input('b = '))
    if a > b:
        print(b)
    elif b < a:
        print(a)
    else:
        print('numbers equals')


def sign_function():
    """
    В математике функция sign(x) (знак числа) определена так:
    sign(x) = 1, Если x > 0,
    sign(x) = -1, Если x < 0,
    sign(x) = 0, Если x = 0,
    """
    value = float(input(" write number: "))
    if value < 0:
        sign_x = -1
    elif value == 0:
        sign_x = 0
    else:
        sign_x = 1
    print(f"Output: {sign_x}")


def chess_yes_or_no():
    """
    Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в заные - то NO.
    Программа получает на вход четыре чисоа от 1 до 8 каждое, задающие номер столбца и номер строки сначал для первой
    клетки, потом для второй клетки.
    """
    first_column = int(input("write number from 1 to 8: "))
    first_raw = int(input("write number from 1 to 8: "))
    second_column = int(input("write number from 1 to 8: "))
    second_raw = int(input("write number from 1 to 8: "))

    # проверяем клетки на чётность. получаем сумму столбцов и строк двух клеток
    # сравнивем остатки (получается 0 или 1)
    # если остатки совпадают у двух клеток, значит YES
    if (first_column + first_raw) % 2 == (second_column + second_raw) % 2:
        print("YES")
    else:
        print("NO")


def min_of_three():
    """
    Даны три целых числа. Выведите зачение наименьше из них.
    """
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    if a < c and b < c:
        if a < b:
            print(a)
        else:
            print(b)
    else:
        print(c)


def last_digit_from_number():
    """Дано натуральное число. Выведите его последнюю цифру."""
    number = int(input("write positive integer number: "))
    print(f"last digit is {number % 10}")


def MKAD_and_Vasya():
    """Длина Московской кольцевой автомобильной дороги - 109 километров. Байкер
    Вася стартует с нулевого километра МКАД и едет со скоростью vv километров в
    час. На какой отметке он остановится через tt часов?

    Программа получает на вход значение v и t. Если v > 0, то Вася движется в
    положительном направлении по МКАД, если же значение v < 0, то в отрицательном.

    Программа должна вывести целое число от 0 до 108 - номер отметки на которой отсановится Вася.
    """
    v = int(input('write v '))
    t = int(input('write t '))
    # Получаем расстояние которое проехал Вася, а потом ищем точку в которой он остановился.
    # 109 - радиус окружности
    print(f"Output: {v * t % 109}")


def first_digit_after_comma():
    """
    Дано положительное действиетельное число Х. Выведите его первую цифру после десятичной точки.
    """
    number = float(input("write a number: "))
    digit = int(number * 10) % 10
    print(digit)


def hypotenuse_of_triangle():
    """
    Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
    """
    a = int(input("a = "))
    b = int(input("b = "))
    # 0.5 = 1\2. Получаем квадратный корень путём возведения числа в степень 0.5
    print(f"hypotenuse = {(a ** 2 + b ** 2) ** 0.5}")


def all_numbers_from_A_to_B():
    """Даны два целых чиста А и В (при этом А <= B). Выведите все числа от А до В включительно."""
    a = int(input("a = "))
    b = int(input("b = "))
    print(f"a = {a}, b = {b}")
    for el in range(a, b + 1, 1):
        print(f"el = {el}")


def asc_desc_for_two_numbers():
    """
    Даны два целых чиста A и В. Выведите все числа от А до В включительно, в порядке возрастанеия, есил A < В,
    или в порядке убывания в противном случае.
    """
    a = int(input("a = "))
    b = int(input("b = "))
    print(f"a = {a}, b = {b}")
    if a < b:
        for el in range(a, b + 1, 1):  # Начать с a, закончить в (b+1), с шагом 1
            print(f"el = {el}")
    else:  # a > b
        for el in range(a, b - 1, -1):  # Начать с a, закончить в (b-1), с шагом -1
            print(f"el = {el}")


def all_odds_numbers():
    """
    Даны два целых числа A и B, A > B. Выведите все нечётные числа от А до В
    включительно в порядке убывания. В этой задаче обойтись без инструкции If.
    """
    a = int(input('А должно быть больше В, a = '))
    b = int(input('А должно быть больше В, b = '))
    start_from = a - (a + 1) % 2
    end_there = b - b % 2
    step = -2
    for el in range(start_from, end_there, step):
        print(f"el = {el}")


def degrees():
    """По данному натуральному n вычислите сумму 1**3 + 2**3 + 3**3 + ... + n**3 """
    n = int(input("write n: "))
    result = 0
    for el in range(1, n + 1, 1):  # начинаем с 1, заканчиваем (N+1), с шагом 1
        print(el, el ** 3)  # выводим число и его куб
        result += el ** 3  # добавляем значение куба числа к общей сумме всех кубов
    print(f"result = {result}")  # выводим сумму кубов всех чисел


def all_square_for_N():
    """По данному целому числу N распечатайте все квадраты натуральных числе,
    не превосходящие N в порядке возрастания."""
    n = int(input("write n: "))
    i = 1
    while i ** 2 <= n:
        print(f"square = {i ** 2}")
        i += 1


def biggest_degree_of_N():
    """По данному натуральному числу N найдите наибольшую целую степень двойки,
    не превосходящую N. Выведите показатель степени и саму степень.
    Решить без использования операции возведения в степень"""

    n = int(input("write n: "))
    degree = 0
    number = 1
    while number + number <= n:
        number += number
        degree += 1
    print(f"degree = {degree}, number = {number}")


def sum_numbers_who_ends_of_zero():
    """С клавиатуры последовательно вводятя числа, заканчивающиеся нулём.
    Определите сумму всех элементов последовательно, завершающейся числом 0."""
    counter = 0
    entered_number = int(input("write an integer: "))
    while entered_number != 0:
        counter += entered_number
        entered_number = int(input("write a number: "))
    print(f"Result = {counter}")


def max_value_from_sequence():
    """С клавиатуры последовательно вводятя числа, заканчивающиеся нулём.
    Определите значение максимального элемента этой последовательности."""
    counter = 0
    entered_number = int(input("write an integer: "))
    while entered_number != 0:  # пока введённое число не равно 0
        if entered_number > counter:
            counter = entered_number
        entered_number = int(input("write a number: "))
    print(f"Result = {counter}")


if __name__ == '__main__':

    """Ввод вывыод"""
    # sum_of_three()
    # length_of_legs()
    # greetings()
    # next_and_previous_numbers()

    """Условные операторы"""
    # min_of_two_numbers()
    # sign_function()
    # chess_yes_or_no()
    # min_of_three()

    """Арифметические операции"""
    # last_digit_from_number()
    # MKAD_and_Vasya()
    # first_digit_after_comma()
    # hypotenuse_of_triangle()

    """Цикл for"""
    # all_numbers_from_A_to_B()
    # asc_desc_for_two_numbers()
    # all_odds_numbers()
    # degrees()

    """Цикл while"""
    # all_square_for_N()
    # biggest_degree_of_N()
    # sum_numbers_who_ends_of_zero()
    # max_value_from_sequence()

    pass
