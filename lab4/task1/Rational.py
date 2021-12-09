import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.__denominator = 1
        self.numerator = numerator
        self.denominator = denominator
        Rational.reduce(self)

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError
        self.__numerator = numerator
        Rational.reduce(self)

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError
        if not denominator:
            raise ValueError
        self.__denominator = denominator
        Rational.reduce(self)

    @staticmethod
    def reduce(fraction):
        if not isinstance(fraction, Rational):
            return TypeError
        average = math.gcd(fraction.numerator, fraction.denominator)
        fraction.__numerator //= average
        fraction.__denominator //= average
        return fraction

    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return Rational.reduce(Rational(self.numerator + other * self.denominator, self.denominator))
        return Rational.reduce(Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                                        self.denominator * other.denominator))

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return Rational.reduce(Rational(self.numerator - other * self.denominator, self.denominator))
        return Rational.reduce(Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                                        self.denominator * other.denominator))

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return Rational.reduce(Rational(self.numerator * other, self.denominator))
        return Rational.reduce(Rational(self.numerator * other.numerator,
                                        self.denominator * other.denominator))

    def __truediv__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return Rational.reduce(Rational(self.numerator, self.denominator * other))
        return Rational.reduce(Rational(self.numerator * other.denominator,
                                        self.denominator * other.numerator))

    def __iadd__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            self.numerator += other * self.denominator
        else:
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
        return Rational.reduce(self)

    def __isub__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            self.numerator -= other * self.denominator
        else:
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator *= other.denominator
        return Rational.reduce(self)

    def __imul__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            self.numerator *= other
        else:
            self.numerator *= other.numerator
            self.denominator *= other.denominator
        return Rational.reduce(self)

    def __itruediv__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            self.denominator *= other
        else:
            self.numerator *= other.denominator
            self.denominator *= other.numerator
        return Rational.reduce(self)

    def __lt__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return self.numerator < other * self.denominator
        return self.numerator * other.denominator < other.numerator * self.denominator


    def __le__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return self.numerator <= other * self.denominator
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __eq__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return self.numerator == other * self.denominator
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return self.numerator != other * self.denominator
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return self.numerator > other * self.denominator
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            return self.numerator >= other * self.denominator
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def to_float(self) -> float:
        return self.__numerator / self.__denominator

    def __str__(self) -> str:
        return str(self.__numerator) + '/' + str(self.__denominator)