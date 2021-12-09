# Create a class NOTEBOOK, which contains the name, surname, number phone and birthday of person.
# Define methods of access to these fields and overload operations:
# "+" - for adding a new element;
# "-" - for deleting an element;
# "*" - for searching for an element in the Notebook on one of the data fields.
from lab4.task2.Note import Note
from lab4.task2.Notebook import Notebook

if __name__ == "__main__":

    note1 = Note("Liza", "Honcharova", "+380683875850", "20.12.2002")
    note2 = Note("Daria", "Kravchenko", "+38000000000", "01.12.2002")
    print(note1)
    print(note2, end='\n\n')
    notebook = Notebook()
    notebook + note1
    notebook + note2
    print(notebook)
    print(notebook * "+380683875850")
    notebook - "+380683875850"
    print(notebook)
