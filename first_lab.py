import math

class InputOutput:

    def task_one(self) -> None:
        a, b, c = map(float, input("write three numbers: ").split())
        print(f"{'%g'%(a + b + c)}")

    def task_two(self) -> None:
        a, b = map(float, input("write the value of the two legs: ").split())
        print(f"{'%g'%((a + b) / 2)}")

    def task_three(self) -> None:
        n, k = map(int, input("write N - school students and K - apples: ").split())
        print(f"apples to everyone = {'%g'%(k // n)}\n"
              f"reminder = {'%g'%(k % n)}")

    def task_four(self) -> None:
        name = input("write your name: ")
        print(f"Hello, {name}!")

    def task_five(self) -> None:
        minutes = int(input("write N - minutes: "))
        print(f"Hours = {minutes // 60}, minutes = {minutes % 60}")

    def task_six(self) -> None:
        value = float(input("write number: "))
        print(f"The next number for the number {'%g'%value} is {'%g'%(value + 1)}.")
        print(f"The previous number for the number {'%g'%value} is {'%g'%(value - 1)}.")


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
    pass


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
