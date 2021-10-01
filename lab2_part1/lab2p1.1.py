class Rectangle:

    def __init__(self):
        self.__width = 1.0
        self.__length = 1.0

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
        if type(length) is float and (0.0 < length <= 20.0):
            self.__length = length
        else:
            print("Invalid number")

    @width.setter
    def width(self, width):
        if type(width) is float and (0.0 < width <= 20.0):
            self.__width = width
        else:
            print("Invalid number")

if __name__ == '__main__':

     a = Rectangle()
     print(a.calc_perimeter(), a.calc_area())
     a.length = -1
     a.length = 1.0
     print(a.length)