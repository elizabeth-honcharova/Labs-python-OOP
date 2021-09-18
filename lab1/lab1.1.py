"""

    Task 1

    Program performs simple arithmetic operations

"""

from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser() 
    # set restriction: more than 1 arg
    parser.add_argument("value1", type = float) 
    parser.add_argument("sign", choices = ["+", "-", "*", "/"]) 
    parser.add_argument("value2", type = float) 
    arg = parser.parse_args()
    expression = str(arg.value1) + arg.sign + str(arg.value2)
    
    if arg.sign == "/" and not arg.value2:
        print("Division by zero error!")
    else:
        # executes the expression at run time and print it
        print(eval(expression)) 
        
