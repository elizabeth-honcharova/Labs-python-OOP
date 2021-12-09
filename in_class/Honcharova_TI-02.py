# 1. Визначити клас ЦИФРОВИЙ ЛІЧИЛЬНИК.
# Лічильник - це змінна з обмеженим діапазоном,
# який скидається у початковий стан, коли її цілочисельне значення досягає визначеного максимуму.
# 2. Визначити методи встановлення і виведення значень полів даних.
# Забезпечити можливість встановлення максимального і мінімального значень, зчитування поточного значення.
# 3. Перевантажити операцію += для збільшення значення лічильника, -= для зменшення значення лічильника.

# 4. Визначити похідний клас СЕКУНДОМІР з додатковими полями даних, які позначають включення та виключення секундоміра.
# Визначити операторні методи зчитування та виведення значення заміряного часу.

# 5. Розробити клас РЕЗУЛЬТАТИ спринтерського забігу, який містить послідовність об'єктів класу СЕКУНДОМІР.
# Визначити найменший та найбільший час забігу,
# середнє значення часу забігу, результати часу для трьох переможців змагання.
# 6. Для роботи із послідовністю об'єктів побудувати та використати клас-ітератор.
import time


class Larder:
    def __init__(self, min_value, max_value):
        if not isinstance(max_value, (float, int)) or not isinstance(min_value, (float, int)):
            raise TypeError
        if max_value <= min_value:
            raise ValueError
        self.__max_value = max_value
        self.__min_value = min_value
        self.__larder = min_value

    @property
    def larder(self):
        return self.__larder

    @property
    def max_value(self):
        return self.__max_value

    @max_value.setter
    def max_value(self, max_value):
        if not isinstance(max_value, (float, int)):
            raise TypeError
        if max_value <= self.min_value:
            raise ValueError
        self.__max_value = max_value

    @property
    def min_value(self):
        return self.__min_value

    @min_value.setter
    def min_value(self, min_value):
        if not isinstance(min_value, (float, int)):
            raise TypeError
        if min_value >= self.max_value:
            raise ValueError
        self.__min_value = min_value
        self.__larder = min_value

    def __iadd__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError
        self.__larder += value
        if self.__larder >= self.max_value:
            self.__larder = self.min_value
        return self

    def __isub__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError
        self.__larder -= value
        if self.__larder <= self.min_value:
            self.__larder = self.max_value
        return self

    def __str__(self) -> str:
        return f"min: {self.min_value}, max: {self.max_value}, larder: {self.larder}"


class Stopwatch(Larder):

    def __init__(self, min_value, max_value):
        Larder.__init__(self, min_value, max_value)
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        while self.is_on:
            self.__larder += 1
            time.sleep(1)

    def turn_off(self):
        self.is_on = False
        return self.larder

    @property
    def result(self):
        return self.__larder

    def __str__(self) -> str:
        return f"{self.larder} passed"


class ResIterator:
    def __iter__(self):
        return self

    def __init__(self, results):
        self.results = results
        self.index = 0

    def __next__(self):
        if self.index >= len(self.results):
            raise StopIteration()
        self.index += 1
        return self.results[self.index-1]


class Results:
    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError
        if not all(isinstance(arg, Stopwatch) for arg in args):
            raise TypeError
        self.__time_of_participants = args

    def max_time(self):
        max_time = self.__time_of_participants[0].result
        for cur_time in self.__time_of_participants:
            if cur_time.result > max_time:
                max_time = cur_time.result
        return max_time

    def min_time(self):
        min_time = self.__time_of_participants[0].result
        for cur_time in self.__time_of_participants:
            if cur_time.result < min_time:
                min_time = cur_time.result
        return min_time

    def avg_time(self):
        avg_time = 0
        for cur_time in self.__time_of_participants:
            avg_time += cur_time.result
        return avg_time / len(self.__time_of_participants)

    def __winners(self):
        winners = list()
        for cur_time in self.__time_of_participants:
            winners.append(cur_time.result)
        winners.sort(key=lambda i: i[1], reverse=True)
        return winners

    def top_three(self):
        print(self.__winners()[:3])

    def __iter__(self):
        return ResIterator(self.__time_of_participants)



