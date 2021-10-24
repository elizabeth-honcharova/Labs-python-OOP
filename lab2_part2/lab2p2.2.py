import re
import os


class TextStatistics:

    def __init__(self, filepath="text.txt"):
        if not os.path.exists(filepath):
            raise FileNotFoundError("Can`t open the file!")
        self.filepath = filepath

    def num_of_characters(self):
        result = 0
        with open(self.filepath) as text:
            for line in text:
                for char in line:
                    if not char.isspace():
                        result += 1
        return result

    def num_of_words(self):
        result = 0
        with open(self.filepath) as text:
            for line in text:
                result += len(line.split())
        return result

    def num_of_sentences(self):
        with open(self.filepath) as text:
            return len(re.split(r'[.!?]+', text.read()))-1


if __name__ == '__main__':

    file = TextStatistics('C:/Users/g0nli/Labs-python-OOP-/lab2.txt')
    print("\nNumber of\n", "characters (without spaces): ", file.num_of_characters(),
          "\n words: ", file.num_of_words(),
          "\n sentences: ", file.num_of_sentences())