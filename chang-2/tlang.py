#! /usr/bin/env python3.4

import fileinput
import re


def operation(operation, op, result):
    if(operation == 1):
        result = result + int(op)
    elif(operation == 2):
        result = result * int(op)
    elif(operation == 3):
        result = result - int(op)
    return result


def tlang():
    """Interpret some weird lenguage

    Get line by line and return the result of the operations.
    """
    for line in fileinput.input():
        operat, result, first = 0, 0, False
        for token in line.split():
            if(re.search('^\^', token) and len(token) == 2):
                first = True
                oper = token[1]
                if(oper == '='):
                    print('Procesando suma')
                    operat = 1
                elif(oper == '#'):
                    print('Procesando multiplicación')
                    operat = 2
                elif(oper == '@'):
                    print('Procesando resta')
                    operat = 3
            elif(re.search('\$$', token)):
                number = token[:len(token) - 1]
                if((len(number) > 0) and
                   (number.isnumeric()
                    or (number.startswith('-')
                        and number[1:].isdigit()))):
                    if(first):
                        first = False
                        result = int(number)
                    else:
                        print(operation(operat, number, result))
            elif(token.isnumeric() or
                 (token.startswith('-') and
                  token[1:].isdigit())):
                    if(first):
                        first = False
                        result = int(token)
                    else:
                        result = operation(operat, token, result)


tlang()


