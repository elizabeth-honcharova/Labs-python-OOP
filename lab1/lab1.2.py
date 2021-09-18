"""

    Task 2

    Program performs the standard math functions on the data.

"""

from argparse import ArgumentParser
from operator import iadd, isub, imul, itruediv, imod, ipow

if __name__ == "__main__":
    
    parser = ArgumentParser()
    # the 1-st arg is action and the others are values (float only)
    parser.add_argument("action", choices = ["add", "sub", "mul", "div", "mod", "pow"])
    parser.add_argument("values", type = float, nargs = '+')
    arg = parser.parse_args()

    # create dict of functions with keys that the user`s entered
    # uses functions from operator module
    operators = {
        "add": iadd, "sub": isub, "mul": imul, 
        "div": itruediv, "mod": imod, "pow": ipow
    }

    # produce one of the selected action on all entered values 
    result = arg.values[0]
    for value in arg.values[1:]:
        if arg.action == "div" and not value:
            result = "Division by zero error!"
            break
        else:
            result = operators[arg.action](result, value)

    print(result)