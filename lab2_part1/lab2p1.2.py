import math

class Rational:

    def __init__(self, numerator = 1, denumerator = 1):

        if not isinstance(numerator , int):
            raise TypeError("numerator is not integer")
        elif not isinstance(denumerator , int):
            raise TypeError("denumenator is not integer")
        elif not denumerator:
            raise ZeroDivisionError("denumerator = 0")

        average = math.gcd(numerator, denumerator)

        self.__numerator = numerator // average
        self.__denumerator = denumerator // average

    def __str__(self) -> str:
        return str(self.__numerator) + '/' + str(self.__denumerator)

    def get_infloat(self) -> float:
        return self.__numerator / self.__denumerator

if __name__ == '__main__':
    val = Rational(33, 11)
    print(val)
    print(val.get_infloat())