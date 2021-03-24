import math


class InputOutput:

    def task_one(self) -> None:
        a, b, c = map(float, input("write three numbers: ").split())
        print(f"{'%g' % (a + b + c)}")

    def task_two(self) -> None:
        a, b = map(float, input("write the value of the two legs: ").split())
        print(f"{'%g' % ((a + b) / 2)}")

    def task_three(self) -> None:
        n, k = map(int, input("write N - school students and K - apples: ").split())
        print(f"apples to everyone = {'%g' % (k // n)}\n"
              f"reminder = {'%g' % (k % n)}")

    def task_four(self) -> None:
        name = input("write your name: ")
        print(f"Hello, {name}!")

    def task_five(self) -> None:
        minutes = int(input("write N - minutes: "))
        print(f"Hours = {minutes // 60}, minutes = {minutes % 60}")

    def task_six(self) -> None:
        value = float(input("write number: "))
        print(f"The next number for the number {'%g' % value} is {'%g' % (value + 1)}.")
        print(f"The previous number for the number {'%g' % value} is {'%g' % (value - 1)}.")


class ConditionalStatements:
    def task_one(self) -> None:
        a, b = map(int, input("write two numbers: ").split())
        print(f"Output: {(a if a < b else b)}")  # min(a, b)

    def task_two(self) -> None:
        value = float(input(" write number: "))
        if value < 0:
            sign_x = -1
        elif value == 0:
            sign_x = 0
        else:
            sign_x = 1
        print(f"Output: {sign_x}")

    def task_three(self) -> None:
        first_column, first_raw, second_column, second_raw = map(int, input("write 4 numbers from 1 to 8: ").split())
        if (first_column + first_raw) % 2 == 0 and (second_column + second_raw) % 2 == 0:
            print("YES")
        else:
            print("NO")

    def task_four(self) -> None:
        year = int(input("write your year: "))
        print(f"{('YES' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 'NO')}!")

    def task_eight(self):
        n, m, k = map(int, input("write n, m, k: ").split())
        if (k == n) or (k == m) or (k in range(n, m * n, n)) or (k in range(m, n * m, m)):
            print("YES")
        else:
            print("NO")


class ArithmeticOperations:
    def task_one(self) -> None:
        number = int(input("write positive integer number: "))
        print(f"last digit = {number % 10}")

    def task_two(self) -> None:
        """I don't understand this task."""
        v, t = map(int, input(" write v and t: ").split())
        print(f"Output: {v * t % 109}")

    def task_three(self) -> None:
        number = float(input("write a number: "))
        print(f"{int((number * 10) % 10)}")

    def task_four_master_degree(self):
        a, b = map(int, input("write a and b: ").split())
        print(f"hypotenuse = {math.sqrt(a * a + b * b)}")


class CycleFor:

    def task_one(self) -> None:
        a, b = map(int, input("write two integer numbers: ").split())
        print(f"a = {a}, b = {b}")
        for el in range(a, b + 1, 1):
            print(f"el = {el}")

    def task_two(self) -> None:
        a, b = map(int, input("write two integer numbers: ").split())
        print(f"a = {a}, b = {b}")
        if a < b:
            for el in range(a, b + 1, 1):
                print(f"el = {el}")
        else:  # a > b
            for el in range(a, b - 1, -1):
                print(f"el = {el}")

    def task_three(self) -> None:
        a, b = map(int, input("write two integer numbers where A > B: ").split())
        for el in range(a - (a + 1) % 2, b - b % 2, -2):
            print(f"el = {el}")

    def task_four(self):
        n = int(input("write n: "))
        result = 0
        for el in range(1, n, 1):
            result += el * 10 + 3
        print(f"result = {result}")


class CycleWhile:

    def task_one(self) -> None:
        n = int(input("write n: "))
        i = 1
        while i ** 2 <= n:
            print(f"square = {i ** 2}")
            i += 1

    def task_two(self) -> None:
        n = int(input("write n: "))
        degree = 0
        number = 1
        while number + number <= n:
            number += number
            degree += 1
        print(f"degree = {degree}, number = {number}")

    def task_three(self) -> None:
        counter = 0
        entered_number = int(input("write an integer: "))
        while entered_number != 0:
            counter += entered_number
            entered_number = int(input("write a number: "))
        print(f"Result = {counter}")

    def task_four(self):
        counter = 0
        entered_number = int(input("write an integer: "))
        while entered_number != 0:
            if entered_number > counter:
                counter = entered_number
            entered_number = int(input("write a number: "))
        print(f"Result = {counter}")


if __name__ == '__main__':
    io = InputOutput()
    # io.task_one()
    # io.task_two()
    # io.task_three()
    # io.task_four()
    # io.task_five()
    # io.task_six()

    cs = ConditionalStatements()
    # cs.task_one()
    # cs.task_two()
    # cs.task_three()
    # cs.task_four()
    # cs.task_five()
    # cs.task_six()
    # cs.task_seven()
    # cs.task_eight()

    ao = ArithmeticOperations()
    # ao.task_one()
    # ao.task_two()
    # ao.task_three()
    # ao.task_four_master_degree()

    cf = CycleFor()
    # cf.task_one()
    # cf.task_two()
    # cf.task_three()
    # cf.task_four()

    cw = CycleWhile()
    # cw.task_one()
    # cw.task_two()
    # cw.task_three()
    # cw.task_four()
