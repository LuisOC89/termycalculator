# from interface import menu
from utils.helpers import VALID_OPERATORS, VALID_DIGITS, PARENTHESIS_SIMBOLS, TROLL_FACE
from utils.errors import *

def check_valid_values(instructions):
    '''Checks that the expresion contains just valid values'''
    for char_index in range(len(instructions)):
        if instructions[char_index] not in VALID_OPERATORS+VALID_DIGITS+PARENTHESIS_SIMBOLS:
            print(INVALID_SYMBOL_OR_VALUE)   
            return False
    return True
           
def check_surroundings_VALID_OPERATORS(instructions):
    '''Checks for operators (+-:/*) not to be one next to the other'''
    for char_index in range(len(instructions)):
        if instructions[char_index] in VALID_OPERATORS:
            if instructions[char_index - 1] in VALID_OPERATORS or instructions[char_index + 1] in VALID_OPERATORS:   
                print(OPERATORS_TOGETHER)
                return False
    return True

def check_first_last_values(instructions):
    '''CHecks the first and last values to be either digit or parenthesis sign'''
    if instructions[0] not in VALID_DIGITS+PARENTHESIS_SIMBOLS or instructions[-1] not in VALID_DIGITS+PARENTHESIS_SIMBOLS:
        print(FIRST_LAST_VALUES_PAR)
        return False
    return True

def check_no_empty_parenthesis(instructions):
    '''Looks for empty parenthesis: ()'''
    if "()" in instructions:
        print(EMPTY_PARENTHESIS)
        return False
    return True

def check_equal_open_close_parenthesis(instructions):
    '''Checks for equal amount of open '(' and close ')' parenthesis'''
    qty_open_parenthesis = instructions.count('(')
    qty_closing_parenthesis = instructions.count(')')
    if qty_open_parenthesis != qty_closing_parenthesis:
        print(EXTRA_OR_MISSING_PAR)
        return False
    return True

def check_surroundings_and_order_parenthesis(instructions):
    ''' Checks for next scenarios:
    - Order of parenthesis: ')' before '(' .
    - Non-sense values next to parenthesis:
        - '(' :
            - Before: '0(', '1(', '2(', '3(', '4(', '5(', '6(', '7(', '8(', '9('
            - After: '(+', '(-', '(:', '(*', '(/'
        - ')' :
            - Before: '+)', '-)', ':)', '*)', '/)'
            - After: ')0', ')1', ')2', ')3', ')4', ')5', ')6', ')7', ')8', ')9'
      '''
    count_for_order = 0
    for char_index in range(len(instructions)):
        if instructions[char_index] == ")" :
            count_for_order -= 1
        elif instructions[char_index] == "(" :
            count_for_order += 1
        if count_for_order < 0:
            print(WRONG_ORDER_PARENTHESIS)
            return False

        if instructions[char_index] == "(":
            if instructions[char_index+1] in VALID_OPERATORS:
                print(INVALID_VALUE_RIGHT_OPEN_PAR)
                return False
            if char_index != 0:
                if instructions[char_index-1] in VALID_DIGITS:
                    print(INVALID_VALUE_LEFT_OPEN_PAR)
                    return False

        elif instructions[char_index] == ")":
            if instructions[char_index-1] in VALID_OPERATORS:
                print(INVALID_VALUE_LEFT_CLOSING_PAR)
                return False
            elif char_index != len(instructions) - 1:
                if instructions[char_index+1] in VALID_DIGITS:
                    print(INVALID_VALUE_RIGHT_CLOSING_PAR)
                    return False
    return True

def checking_division_by_0(dividend, divisor):
    if divisor != 0 :
        return dividend/divisor  
    else: 
        print(TROLL_FACE)
        print(DIVISION_BY_ZERO)
        return "Infinite"