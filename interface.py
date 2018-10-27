import sys

ACCEPTED_RESPONSES=["y", "Y", "n", "N"]
VALID_OPERATORS="+-:/*"
VALID_DIGITS="0123456789"
PRIORITY_OPERATORS="/*:"
PARENTHESIS_SIMBOLS = "()"

def banner(text, icon_upper=None, icon_lower=None):
    '''Increases visibility of text'''
    row_upper = icon_upper * (len(text) + 6) + "\n" if icon_upper else ""
    row_lower = "   \n" + icon_lower * (len(text) + 6) if icon_lower else ""
    print(row_upper+ "   " + text + row_lower)

def check_valid_values(instructions):
    for char_index in range(len(instructions)):
        if instructions[char_index] not in VALID_OPERATORS+VALID_DIGITS+PARENTHESIS_SIMBOLS:
            print("\n~~~~~~~ERROR: Invalid simbol or number :/ ~~~~~~~~\n")   
            return False
    return True
           
def check_surroundings_VALID_OPERATORS(instructions):
    for char_index in range(len(instructions)):
        if instructions[char_index] in VALID_OPERATORS:
            if instructions[char_index - 1] in VALID_OPERATORS or instructions[char_index + 1] in VALID_OPERATORS:   
                print("\n~~~~~~~ERROR: Two operators can not go together :/ ~~~~~~~~\n")
                return False
    return True

def check_first_last_values(instructions):
    if instructions[0] not in VALID_DIGITS+PARENTHESIS_SIMBOLS or instructions[-1] not in VALID_DIGITS+PARENTHESIS_SIMBOLS:
        print("\n~~~~~~~ERROR: First and last values have to be numbers :/ ~~~~~~~~\n")
        return False
    return True

def check_no_empty_parenthesis(instructions):
    if "()" in instructions:
        print("\n~~~~~~~ERROR: Empty parenthesis detected :/ ~~~~~~~~\n")
        return False
    return True

def check_equal_open_close_parenthesis(instructions):
    qty_open_parenthesis = instructions.count('(')
    qty_closing_parenthesis = instructions.count(')')
    if qty_open_parenthesis != qty_closing_parenthesis:
        print("\n~~~~~~~ERROR: Extra parenthesis character detected :/ ~~~~~~~~\n")
        return False
    return True

def check_surroundings_and_order_parenthesis(instructions):
    count_for_order = 0
    for char_index in range(len(instructions)):
        if instructions[char_index] == ")" :
            count_for_order -= 1
        elif instructions[char_index] == "(" :
            count_for_order += 1
        if count_for_order < 0:
            print("\n~~~~~~~ERROR: Closing parenthesis before open parenthesis found :/ ~~~~~~~~\n")
            return False

        if instructions[char_index] == "(":
            if char_index == 0:
                if instructions[char_index+1] in VALID_OPERATORS:
                    print("\n~~~~~~~ERROR: Invalid value to the right of '(' :/ ~~~~~~~~\n")
                    return False
            elif char_index != 0:
                if instructions[char_index+1] in VALID_OPERATORS or instructions[char_index-1] in VALID_DIGITS:
                    print("\n~~~~~~~ERROR: Invalid value next to '(' :/ ~~~~~~~~\n")
                    return False

        elif instructions[char_index] == ")":
            if char_index == len(instructions) - 1:
                if instructions[char_index-1] in VALID_OPERATORS:
                    print("\n~~~~~~~ERROR: Invalid value to the left of ')' :/ ~~~~~~~~\n")
                    return False
            elif char_index != len(instructions) - 1:
                if instructions[char_index-1] in VALID_OPERATORS or instructions[char_index+1] in VALID_DIGITS:
                    print("\n~~~~~~~ERROR: Invalid value next to ')' :/ ~~~~~~~~\n")
                    return False
    return True
            


def make_list(instructions):
    list_calculus = []
    index = 0
    for char_index in range(len(instructions)):
        print("char_index: {}, value: {}".format(char_index, instructions[char_index]))
        if instructions[char_index] in VALID_OPERATORS+PARENTHESIS_SIMBOLS:
            if instructions[index:char_index] != '':
                list_calculus.append(int(instructions[index:char_index]))
            list_calculus.append(instructions[char_index])    # OK
            index = char_index + 1
        # LAST NUMBER
        if char_index == len(instructions) - 1 :
            if instructions[index:len(instructions)] != '':
                list_calculus.append(int(instructions[index:len(instructions)]))
    print("List_calculus: "+str(list_calculus))
    return list_calculus

def make_operation(number1, number2, operator):
    if operator == ":" or operator == "/" :
        if number2 != 0 :
            reduced_member = number1/number2  
        else: 
            print("\n~~~~~~~ERROR: Divisions by 0 are INFINITEEEEEE :/ ~~~~~~~~\n")
            reduced_member = "ERROR"
    elif operator == "*" :
        reduced_member = number1*number2
    elif operator == "+" :
        reduced_member = number1+number2
    else:                                   # operator == "-" 
        reduced_member = number1-number2
    return reduced_member

# EXAMPLE : [23, '+', 34, '-', 98, ':', 29, '/', 34, '/', 98]
def reduce_members(list_calculus):
    while True:
        if "*" in list_calculus or ":" in list_calculus or "/" in list_calculus:
            for operator_index in range(1,len(list_calculus),2):
                print("Operator index - 1: {}, value: {}".format(operator_index-1, list_calculus[operator_index-1]))
                print("Operator index: {}, value: {}".format(operator_index, list_calculus[operator_index]))
                print("Operator index + 1: {}, value: {}".format(operator_index+1, list_calculus[operator_index+1]))
                if list_calculus[operator_index] in PRIORITY_OPERATORS :
                    temp = make_operation(list_calculus[operator_index-1],list_calculus[operator_index+1],list_calculus[operator_index])
                    if temp == "ERROR":
                        break
                    list_calculus[operator_index-1] = temp
                    del list_calculus[operator_index:operator_index+1+1] # Plus extra, sublist structure: [initial:final)
                    print("List_reduce: "+str(list_calculus))
                    break
                else:
                    pass
        else:
            for operator_index in range(1,len(list_calculus),2):
                temp = make_operation(list_calculus[operator_index-1],list_calculus[operator_index+1],list_calculus[operator_index])
                list_calculus[operator_index-1] = temp
                del list_calculus[operator_index:operator_index+1+1] # Plus extra, sublist structure: [initial:final)
                print("List_reduce: "+str(list_calculus))
                break
        if len(list_calculus) == 1:
            return list_calculus[0]
        else:
            pass
        
def calculate(main_list):
    while True:
        start_parenthesis = 0
        end_parenthesis = 0
        for index in range(len(main_list)):
            if '(' in main_list:
                if main_list[index] == "(":
                    start_parenthesis = index
                if main_list[index] == ")":
                    end_parenthesis = index
                if end_parenthesis:
                    print("Parenthesis: {}".format(main_list[start_parenthesis+1:end_parenthesis]))
                    temp = reduce_members(main_list[start_parenthesis+1:end_parenthesis])
                    main_list[start_parenthesis] = temp
                    del main_list[start_parenthesis+1:end_parenthesis+1] # Plus extra, sublist structure: [initial:final)
                    print("List_calculate h: "+str(main_list))
                    break
            else:
                main_list = reduce_members(main_list)
                print("List_calculate j: "+str(main_list))
                print("Type List_calculate j: "+str(type(main_list)))
                if str(type(main_list)) == "<class 'int'>":
                    return main_list
                elif str(type(main_list)) == "<class 'float'>":
                    return round(main_list, 2)
                else:
                    pass

def menu():
    '''User interface'''
    counter = 0
    while True:
        # Always visibility of application name and limitations (PSQL)
        if counter%2 == 0:
            banner("termycalculator: Calculator of simple expressions", "T", "T")
            # print("   Look out!: Don't leave any spaces in your expression :/   ")
        banner("OPTIONS: (1) Insert expression | (2) Help | (3) Quit", "‾", "_")
           
        user_choice = input("\nPlease select an a option: ")
        
        if user_choice == "1":
            while True:
                math_expressions = input(" Calculate this: ")
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
                # numbers, operators, calculus = make_list(math_instructions)
                # print("Numbers: {n}, Operators: {o}, List: {c}".format(n=numbers, o=operators, c=calculus))
                calculus = make_list(math_instructions)
                print("List: {}".format(calculus))
                # make_list_operators(math_instructions)
                
                result=calculate(calculus)

                # result = reduce_members(calculus) 

                print("Final result: {}".format(result))

                # while len(numbers) > 1:
                #     print("Numbers: {n}, Operators: {o}".format(n=numbers, o=operators))
                #     for operator_index in range(len(operators)):
                #         if operators[operator_index+1] in PRIORITY_OPERATORS:
                #             reduced_value = reduce_members(numbers[operator_index+1], numbers.pop(operator_index+2), operators.pop(operator_index+1))
                #             numbers[operator_index+1] = reduced_value

        elif user_choice == "2":
            pass
                
        elif user_choice == "3":
            banner("termycalculator finished by user", 'x', 'x')
            sys.exit()
        else:
            print("\n~~~~~~~ERROR: Invalid choice :/, try again~~~~~~~\n")
        
        counter += 1
        input("Press Enter to continue...")


#To run this file by itself
if __name__=="__main__":
    print("\n")
    menu()

# if keep_previous_log_files in ACCEPTED_RESPONSES:
                            #     keep_log_files(keep_previous_log_files)
                            #     break
                            # else:
                            #     print("\n~~~~~~~ERROR: Invalid choice :/, try again~~~~~~~\n")