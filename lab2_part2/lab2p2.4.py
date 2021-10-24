class ProductPriceInfo:

    all_codes = []

    def __init__(self, code, price, left=None, right=None):
        self.code = code
        self.price = price
        self.left = left
        self.right = right

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError("Invalid type of code")
        if code in self.all_codes:
            raise ValueError("Invalid code")
        if code <= 0:
            raise ValueError("Invalid code")
        self.__code = code
        self.all_codes.append(code)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError("Invalid price")
        if price <= 0.0:
            raise ValueError("Invalid price")
        self.__price = price

    def __str__(self):
        return f'Node ["{self.product}"]'


class ProductsPricesTree:

    def __init__(self):
        self.__root = None

    def add_node(self, node):
        if not isinstance(node, ProductPriceInfo):
            return TypeError("Invalid type of node")

        new_node = node

        if not self.__root:
            self.__root = new_node
            return None

        if not ProductsPricesTree.__is_unique(self.__root, node.code):
            return None

        current_node = self.__root

        while True:
            if node.code < current_node.code:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    current_node.right = new_node
                    break

    @staticmethod
    def __is_unique(root, code):
        if not root:
            return True
        if root.code == code:
            return False
        if code < root.code:
            return ProductsPricesTree.__is_unique(root.left, code)
        else:
            return ProductsPricesTree.__is_unique(root.right, code)

    def delete_node(self, code):
        if not isinstance(code, int):
            raise TypeError("Invalid type of code")
        self.__root = ProductsPricesTree.__delete_node(self.__root, code)

    @staticmethod
    def __delete_node(root, code):
        if not root:
            return root
        if code < root.code:
            root.left = ProductsPricesTree.__delete_node(root.left, code)
        elif code > root.code:
            root.right = ProductsPricesTree.__delete_node(root.right, code)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = ProductsPricesTree.__min_node(root.right)
            root.value = temp.value
            root.right = ProductsPricesTree.__delete_item(root.right, code)
        return root

    @staticmethod
    def __min_node(node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def find(self, code):
        if not isinstance(code, int):
            raise TypeError('Invalid code type')
        return self.__find(self.__root, code)

    @staticmethod
    def __find(root, code):
        if root:
            if code < root.code:
                return ProductsPricesTree.__find(root.left, code)
            elif code > root.code:
                return ProductsPricesTree.__find(root.right, code)
            else:
                return root.price
        return None

    def get_cost(self, code, quantity):
        if not isinstance(quantity, int):
            return TypeError("Invalid type of quantity")
        if quantity <= 0:
            return ValueError("Invalid value of quantity")
        result = self.find(code)
        if result:
            return result * quantity
        else:
            return "Invalid code"

    def print(self):
        ProductsPricesTree.__print(self.__root)

    @staticmethod
    def __print(node):
        if not node:
            return None
        ProductsPricesTree.__print(node.left)
        print(f"Product:\n\t{node.code}, price: {node.price}")
        ProductsPricesTree.__print(node.right)


if __name__ == "__main__":
    prod1 = ProductPriceInfo(12, 1200)
    prod2 = ProductPriceInfo(78, 400)
    prod3 = ProductPriceInfo(1, 785)

    tree = ProductsPricesTree()

    tree.add_node(prod1)
    tree.add_node(prod2)
    tree.add_node(prod3)

    print("\tTree 1.0")
    tree.print()

    tree.delete_node(1)

    print("\n\tTree 2.0")
    tree.print()

    try:
        data = [int(x) for x in input('\nEnter product code and quantity of products (separated by space): ').split()]
        if len(data) != 2:
            raise Exception('Invalid input')
        print(tree.get_cost(data[0], data[1]))
    except Exception as e:
        print(e)