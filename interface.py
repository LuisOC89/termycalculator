#! /Users/lorozco7/miniconda3/bin/python python3

# interface.py

import sys

from utils.helpers import APP_TITLE, APP_OPTIONS, APP_FINISHED
from utils.errors import INVALID_CHOICE
from utils.process_expression import make_list, calculate
from utils.validation import check_valid_values, check_surroundings_VALID_OPERATORS, check_first_last_values, check_no_empty_parenthesis, check_equal_open_close_parenthesis, check_surroundings_and_order_parenthesis

def banner(text, icon_upper=None, icon_lower=None):
    '''Makes nice signs with text'''
    row_upper = icon_upper * (len(text) + 6) + "\n" if icon_upper else ""
    row_lower = "   \n" + icon_lower * (len(text) + 6) if icon_lower else ""
    print(row_upper+ "   " + text + row_lower)

def menu():
    '''User interface'''
    counter = 0
    while True:
        # Always visibility of application name
        if counter%2 == 0:
            banner(APP_TITLE, "T", "T")
            # print("   Look out!: Don't leave any spaces in your expression :/   ")
        banner(APP_OPTIONS, "‾", "_")
           
        user_choice = input("\nPlease select an option: ")
        
        if user_choice == "1":
            while True:
                math_expressions = input("Calculate this: ")
                print("")
                math_instructions = math_expressions.replace(" ", "")
                validator = check_valid_values(math_instructions) 
                if not validator:
                    break
                validator = check_first_last_values(math_instructions)  
                if not validator:
                    break
                validator = check_surroundings_VALID_OPERATORS(math_instructions)
                if not validator:
                    break
                validator = check_no_empty_parenthesis(math_instructions)
                if not validator:
                    break
                validator = check_equal_open_close_parenthesis(math_instructions)
                if not validator:
                    break
                validator = check_surroundings_and_order_parenthesis(math_instructions)
                if not validator:
                    break
                
                calculus = make_list(math_instructions)
                result=calculate(calculus)

                print("Results: {}".format(result))
                break

        elif user_choice == "2":
            pass
                
        elif user_choice == "3":
            banner(APP_FINISHED, 'x', 'x')
            sys.exit()
        else:
            print(INVALID_CHOICE)
        
        counter += 1
        input("Press Enter to continue...\n")

if __name__=="__main__":
    menu()