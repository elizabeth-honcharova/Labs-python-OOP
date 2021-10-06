import re
class TextStatistics:

    def __init__(self, filepath="text.txt"):
        with open(filepath) as text:
            self.data = text.read()

    def num_of_characters(self):
        return len(self.data) - self.data.count(" ") - self.data.count("\n")

    def num_of_words(self):
        return len(self.data.split())

    def num_of_sentences(self):
        return len(re.split(r'[.!?]+', self.data))-1


if __name__ == '__main__':

    file = TextStatistics('C:/Users/g0nli/Labs-python-OOP-/lab2.txt')
    print(file.data)
    print("\nNumber of\n", "characters (without spaces): ", file.num_of_characters(),
          "\n words: ", file.num_of_words(),
          "\n sentences: ", file.num_of_sentences())