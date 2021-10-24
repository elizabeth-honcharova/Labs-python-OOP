class Rectangle:

    def __init__(self, width = 1.0, length = 1.0):
        self.width = width
        self.length = length

    def calc_perimeter(self):
        return self.__length * 2 + self.__width * 2

    def calc_area(self):
        return self.__length * self.__width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError("Invalid type of number")
        if length <= 0.0 or length > 20.0:
            raise ValueError("Invalid value of number")
        self.__length = length

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Invalid type of number")
        if width <= 0.0 or width > 20.0:
            raise ValueError("Invalid value of number")
        self.__width = width


if __name__ == '__main__':

     a = Rectangle()
     print(a.calc_perimeter(), a.calc_area())
     a.length = 1.0
     print(a.length)