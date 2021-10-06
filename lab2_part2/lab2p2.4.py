class Binary_Tree:

    def __init__(self, **products):
        self.products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        for item in products:
            if not isinstance(item.value(), (float, int)) or item.value() <= 0:
                raise TypeError("Invalid price")
            elif not isinstance(item.key(), str) :
                raise TypeError("Invalid code")
        self.__products = products


if __name__ == "__main__":

