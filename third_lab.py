
def distance(x1=0, y1=0, x2=0, y2=0):
    """1.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
    вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
    Считайте четыре действительных числа и выведите результат работы этой функции."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def miles_to_km(miles: float = 0):
    """2.	Напишите функцию `miles_to_km`, которая будет переводить мили в километры.
    В одной миле примерно 1.609 километров"""
    return miles * 1.609


def mean(arguments):
    """3.	Напишите функцию mean, которая будет считать среднее арифметическое переданных в нее аргументов"""
    sum, counter = 0, 0
    for arg in arguments:    # для каждого арумента из всех арументов
        sum += arg           # добавить значение аргумента к общей сумме всех аргументов
        counter += 1         # увеличить на 1 счётчик количества аргументов
    average = sum / counter  # разделить сумму на количество аргументов для получения среднего арифметического
    return average


def concat(arguments):
    """4.	Напишите функцию concat, которая будет принимать произвольное число строк и объединять их в одну"""
    result: str = ""

    for arg in arguments:  # для каждой строки из арументов
        result += arg      # положить значение строки в одну общую строку

    return result


def add(var1, var2):
    """5.1	Напишите функцию call, которая будет принимать произвольную функцию,
    аргументы для неё и делать вызов переданной функции."""
    return var1 + var2


def call(function, var1, var2):
    """5.2	Напишите функцию call, которая будет принимать произвольную функцию,
        аргументы для неё и делать вызов переданной функции."""
    result = function(var1, var2)
    return result


if __name__ == '__main__':
    """
    6.	Написать модуль, в котором содержатся все эти функции,
    а также отдельные скрипты проверки для каждой функции
    """
    # first task - distance()
    result = distance(x1=2, y1=2, x2=4, y2=6)
    print(str(result))

    # second task - miles_to_km()
    value = 321.23
    result = miles_to_km(value)
    print(str(result))

    # third task - mean()
    values = [321.12, 111.22, 333.66, 444.9, 543.6]
    result = mean(values)
    print(str(result))

    # fourth task - concat()
    values = ['aaaa', 'bbbbb', 'cccc', 'hsgjfdosgj']
    print(concat(values))

    # fifth task - call()
    print(call(add, "dasdsad", "aaaaaaaaa"))
    print(call(add, 1, 3))
