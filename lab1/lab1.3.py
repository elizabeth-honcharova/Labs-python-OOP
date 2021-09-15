"""

    Task 3

    Program determines whether the input string is the correct entry 
    for the 'formula' according EBNF syntax

"""

from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser()
    # set restriction: more than 1 arg
    parser.add_argument("expression", nargs = "+")
    arg = parser.parse_args()
    expression = "".join(arg.expression)

    if(' ' in expression): # check and delete all spaces from string
        expression = expression.replace(' ', '')

    operators = ['+', '-']
    result_value = None
    prev_el = None
    isFormula = True

    # if the el isn`t a digit or a sign 
    # or if it`s a sign but a previous el was sign too
    # this expression is nor a formula
    for el in expression: 
        if not(el.isdigit() or (el in operators and prev_el not in operators)):
            isFormula = False
            break
        prev_el = el

    if(isFormula):
        result_value = eval(expression)
    result = (isFormula, result_value)

    print("result =", result)
