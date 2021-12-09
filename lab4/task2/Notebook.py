from lab4.task2.Note import Note


class Notebook:

    def __init__(self):
        self.notes = {}

    def __add__(self, other):
        if not isinstance(other, Note):
            raise TypeError
        self.notes.update({other.phone: other})

    def __sub__(self, other):
        if not isinstance(other, str):
            raise TypeError
        if other in self.notes.keys():
            self.notes.pop(other)

    def __mul__(self, other):
        if not isinstance(other, str):
            raise TypeError
        if other in self.notes.keys():
            return self.notes[other]
        return "Not found"

    def __str__(self):
        return f"notes: {list(map(str, self.notes.values()))}"
