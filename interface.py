import sys

ACCEPTED_RESPONSES=["y", "Y", "n", "N"]
VALID_OPERATORS="+-:/*"
VALID_DIGITS="0123456789"
PRIORITY_OPERATORS="/*:"

def banner(text, icon_upper=None, icon_lower=None):
    '''Increases visibility of text'''
    row_upper = icon_upper * (len(text) + 6) + "\n" if icon_upper else ""
    row_lower = "   \n" + icon_lower * (len(text) + 6) if icon_lower else ""
    print(row_upper+ "   " + text + row_lower)

def check_valid_values(instructions):
    for char_index in range(len(instructions)):
        if instructions[char_index] not in VALID_OPERATORS+VALID_DIGITS:
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

def check_first_last_values_numbers(instructions):
    if instructions[0] not in VALID_DIGITS or instructions[-1] not in VALID_DIGITS:
        print("\n~~~~~~~ERROR: First and last values have to be numbers :/ ~~~~~~~~\n")
        return False
    return True

def check_no_divisions_by_0(instructions):
    for char_index in range(len(instructions)):
        if instructions[char_index] == "/" or instructions[char_index] == ":" :
            if instructions[char_index + 1] == "0" :   
                print("\n~~~~~~~ERROR: Divisions by 0 are INFINITEEEEEE :/ ~~~~~~~~\n")
                return False
    return True


def make_list(instructions):
    list_numbers = []
    list_operators = []
    list_calculus = []
    index = 0
    for char_index in range(len(instructions)):
        if instructions[char_index] in VALID_OPERATORS :
            list_numbers.append(int(instructions[index:char_index]))
            list_operators.append(instructions[char_index])    # OK
            list_calculus.append(int(instructions[index:char_index]))
            list_calculus.append(instructions[char_index])    # OK
            index = char_index + 1
        # LAST NUMBER
        if char_index == len(instructions) - 1 :
            list_numbers.append(int(instructions[index:len(instructions)]))
            list_calculus.append(int(instructions[index:len(instructions)]))
        # index += 1
    print("List_numbers: "+str(list_numbers))
    print("List_operators: "+str(list_operators))     # OK
    print("List_calculus: "+str(list_calculus))
    return list_numbers, list_operators, list_calculus

def make_operation(number1, number2, operator):
    if operator == ":" or operator == "/" :
        reduced_member = number1/number2
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
                    list_calculus[operator_index-1] = temp
                    del list_calculus[operator_index:operator_index+1+1] # Plus extra, sublist structure: [initial:final)
                    print("List: "+str(list_calculus))
                    break
                else:
                    pass
        else:
            for operator_index in range(1,len(list_calculus),2):
                temp = make_operation(list_calculus[operator_index-1],list_calculus[operator_index+1],list_calculus[operator_index])
                list_calculus[operator_index-1] = temp
                del list_calculus[operator_index:operator_index+1+1] # Plus extra, sublist structure: [initial:final)
                print("List: "+str(list_calculus))
                break
        if len(list_calculus) == 1:
            return list_calculus[0]
        else:
            pass

def menu():
    '''User interface'''
    counter = 0
    while True:
        # Always visibility of application name and limitations (PSQL)
        if counter%2 == 0:
            banner("Calculathis: Calculator of simple expressions", "T", "T")
            # print("   Look out!: Don't leave any spaces in your expression :/   ")
        banner("OPTIONS: (1) Insert mathematical operation | (2) Quit", "‾", "_")
           
        user_choice = input("\nPlease select an a option: ")
        
        if user_choice == "1":
            while True:
                math_expressions = input("  Insert mathematical expression: ")
                math_instructions = math_expressions.replace(" ", "")
                validator = check_valid_values(math_instructions) 
                if not validator:
                    break
                validator = check_first_last_values_numbers(math_instructions)  
                if not validator:
                    break
                validator = check_surroundings_VALID_OPERATORS(math_instructions)
                if not validator:
                    break
                validator = check_no_divisions_by_0(math_instructions)
                if not validator:
                    break
                # validator = check_no_divisions_by_0(math_instructions)
                # if not validator:
                #     break
                numbers, operators, calculus = make_list(math_instructions)
                print("Numbers: {n}, Operators: {o}, List: {c}".format(n=numbers, o=operators, c=calculus))
                # make_list_operators(math_instructions)
                
                result = reduce_members(calculus) 

                print("Final result: {}".format(result))

                # while len(numbers) > 1:
                #     print("Numbers: {n}, Operators: {o}".format(n=numbers, o=operators))
                #     for operator_index in range(len(operators)):
                #         if operators[operator_index+1] in PRIORITY_OPERATORS:
                #             reduced_value = reduce_members(numbers[operator_index+1], numbers.pop(operator_index+2), operators.pop(operator_index+1))
                #             numbers[operator_index+1] = reduced_value


                


        elif user_choice == "2":
            banner("DunBoMS finished by user", 'x', 'x')
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