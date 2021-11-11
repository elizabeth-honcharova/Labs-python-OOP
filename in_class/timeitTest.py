import os
from random import randint
from timeit import timeit


def fill_file():
    with open("file.txt", "a") as file:
        while os.path.getsize("file.txt") < 50000000:
            file.write(str(randint(0, 100)) + "\n")


def sum_of_digits1():
    s = 0
    with open("file.txt", "r") as file:
        data = file.readlines()
        for line in data:
            if line.strip().isdigit():
                s += int(line.strip())


def sum_of_digits2():
    s = 0
    with open("file.txt", "r") as file:
        for line in file:
            if line.strip().isdigit():
                s += int(line.strip())


def sum_of_digits3():
    s = 0
    with open("file.txt", "r") as file:
        s = sum(int(line.strip()) for line in file if line.strip().isdigit())


def main():
    fill_file()
    print("1: ", timeit(lambda: sum_of_digits1(), number=10))
    print("2: ", timeit(lambda: sum_of_digits2(), number=10))
    print("3: ", timeit(lambda: sum_of_digits3(), number=10))


if __name__ == "__main__":
    main()
