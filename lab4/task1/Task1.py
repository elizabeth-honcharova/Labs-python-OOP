# Modify the class Rational of Lab No2 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.
from lab4.task1.Rational import Rational

if __name__ == '__main__':

    value1 = Rational(33, 11)
    value2 = Rational(2, 5)
    value3 = Rational(3, 1)
    print(value1, value2, value3)
    print(value1 > value2)
    print(value1 == value3)
    print(value1 + value2)
    value1 += 1
    print(value1)
