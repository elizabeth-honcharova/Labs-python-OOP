"""

    Task 1

    Program performs simple arithmetic operations

"""

from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser() 
    # set restriction: more than 1 arg
    parser.add_argument("expression", nargs = "+") 
    arg = parser.parse_args()
    result = "".join(arg.expression)

    # executes the expression at run time and print it
    print(eval(result)) 
