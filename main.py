#! /Users/lorozco7/miniconda3/bin/python python3
# interface.py

import sys
import argparse

from utils.helpers import APP_TITLE, APP_OPTIONS, APP_FINISHED
from utils.errors import INVALID_CHOICE, NO_EXPRESSION
from utils.validation import check_valid_values, check_surroundings_VALID_OPERATORS, check_first_last_values, check_no_empty_parenthesis, check_equal_open_close_parenthesis, check_surroundings_and_order_parenthesis
from process_expression import make_list, calculate
from utils.help_guide_user import SCOPE, EXAMPLES, SEE_STEPS_OPTION

def banner(text, icon_upper=None, icon_lower=None):
    '''Makes nice signs with text'''
    row_upper = icon_upper * (len(text) + 6) + "\n" if icon_upper else ""
    row_lower = "   \n" + icon_lower * (len(text) + 6) if icon_lower else ""
    print(row_upper+ "   " + text + row_lower)

def menu(see_steps):
    '''User interface'''
    counter = 0
    while True:
        # Always visibility of application name
        if counter%2 == 0:
            banner(APP_TITLE, "T", "T")
        banner(APP_OPTIONS, "‾", "_")
           
        user_choice = input("\nPlease select an option: ")
        
        if user_choice == "1":
            while True:
                math_expression = input("Calculate this: ")
                if str(math_expression) == '':
                    print(NO_EXPRESSION)
                    break
                print("")
                math_instructions = math_expression.replace(" ", "")

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
                
                calculus = make_list(math_instructions, see_steps)
                result=calculate(calculus, see_steps)
                if result == "Infinite":
                    break

                print("Results: {}".format(result))
                break

        elif user_choice == "2":
            print('\n{}\n{}\n{}\n'.format(SCOPE, EXAMPLES, SEE_STEPS_OPTION))
                
        elif user_choice == "3":
            print("")
            banner(APP_FINISHED, 'x', 'x')
            sys.exit()
        else:
            print(INVALID_CHOICE)
        
        counter += 1
        input("Press Enter to continue...\n")

if __name__=="__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--see-steps", help="Being able how the program goes through each step", action="store_true")
    args = parser.parse_args()

    see_steps_on = args.see_steps

    menu(see_steps_on)