import datetime
import os
'''
    This program is intended to practice & illustrate understanding of the following:
        1. Passing parameters and working with arguments
        2. Controlling the flow of a program
        3. Maintaining control of LOOP structures (for & while)
        4. Finding solutions using breadcrumbs as needed
        5. Processing user input and storing it for the duration of program execution
    
    Author: Keith Kornacki
    Initial Date Created: 11/2/2024
    
'''
run_program = True
last_command = ''

def program_start():
    global run_program
    while run_program:
        user_input = input("awaiting next command: ")
        process_input(user_input)


def process_input(input_param):
    input_value = input_param.lower()
    global last_command

    if input_value == "help":
        help_prompt()
        last_command = "help"
    elif 'true' in input_value or 'false' in input_value:
        calculate_true_false()
        last_command = "true or false"
    elif input_value == "remainder" or input_value == 'divide':
        calculate_remainder()
        last_command = "remainder"
    elif input_value == "sum":
        calculate_sum()
        last_command = "sum"
    elif input_value == "difference" or input_value == 'diff':
        calculate_difference()
        last_command = "difference"
    elif input_value == "product" or input_value == 'prod':
        calculate_product()
        last_command = "product"
    elif input_value == "average" or input_value == 'avg':
        calculate_average()
        last_command = "average"
    elif input_value == "min":
        calculate_min()
        last_command = "min"
    elif input_value == "max":
        calculate_max()
        last_command = "max"
    elif input_value == "date":
        get_current_date()
        last_command = "date"
    elif input_value == "equality" or input_value == 'equal':
        determine_equality()
        last_command = "equality"
    elif input_value == "string length" or input_value == 'string len' or input_value == 'str len':
        get_string_length()
        last_command = "string length"
    elif input_value == "exit" or input_value == "end" or input_value == "close":
        print("\t> Terminating program execution - Goodbye!")
        exit()
    elif "run loop " in input_value:
        run_loop_x_times(input_value)
        last_command = input_value
    elif input_value == "cls":
        run_clear_terminal()
        last_command = "cls"
    elif input_value == "repeat":
        process_input(last_command)
    else:
        print("Invalid command received.")
        program_start()


def help_prompt():
    available_commands = (
        "\'help\' | Lists all available commands & a description of their functionality.",
        "\'exit\' / \'end\' / \'close\' | Terminates program execution.",
        "\'repeat\' | Repeats the last command statement used.",
        "\'cls\' | Clears the terminal screen.",
        "\'true\', \'false\', \'true or false\' | Evaluates one value to a Boolean True or False.",
        "\'remainder\', \'divide\' | Calculates the remainder of a division operation with two operands.",
        "\'sum\' | Calculates the sum of an addition operation with two operands",
        "\'difference\', \'diff\' | Calculates the difference of a subtraction operation with two operands.",
        "\'average\', \'avg\' | Calculates the average of all numeric values in a given data set.",
        "\'min\' | Calculates the min (lowest) value from a given numeric data set." ,
        "\'max\' | Calculates the max (highest) value from a given numeric data set.",
        "\'product\', \'prod\' | Calculates the product of a multiplication operation with two operands.",
        "\'date\' | Returns the current system date in MM/DD/YYYY format.",
        "\'equality\', \'equal\' | Determines whether two values are exactly equal.",
        "\'run loop {x-number} of times\' | Runs a loop of logic the specified number of times.",
        "\'string length\', \'string len\', \'str len\' | Determines the length of the provided input string."
    )

    print("\t======== AVAILABLE COMMANDS ========")

    for command in available_commands:
        print(f"\t> {command}")

    return


def calculate_true_false():
    input_param = input("Enter a singular value to be evaluated as True or False: ")
    if input_param:
        print(True)
    else:
        print(False)
    return


def calculate_remainder():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) % float(param_2))

    print(f"\t> The remainder of {param_1} / {param_2} is {result}")
    return

def calculate_sum():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) + float(param_2))

    print(f"\t> The sum of {param_1} + {param_2} is {result}")
    return

def calculate_difference():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) - float(param_2))

    print(f"\t> The difference of {param_1} - {param_2} is {result}")
    return

def calculate_average():
    '''
        Utilized the following info doc: https://www.geeksforgeeks.org/python-convert-float-string-list-to-float-values/
    '''
    input_value_string= input("Enter the values for which you want an average: ")
    input_values = input_value_string.split()
    float_array = [float(number) for number in input_values]
 
    total = sum(float_array)
    average = total / len(float_array)


    print(f"\t> The average of {float_array} is {average: .2f}")
    return

def calculate_min():
    input_value_string= input("Enter the values for which you want to calculate the minimum (lowest) value: ")
    input_values = input_value_string.split()
    float_array = [float(number) for number in input_values]
 
    result = min(float_array)

    print(f"\t> The lowest value of the data set {float_array} is {result}")
    return

def calculate_max():
    input_value_string= input("Enter the values for which you want to calculate the max (highest) value: ")
    input_values = input_value_string.split()
    float_array = [float(number) for number in input_values]
 
    result = max(float_array)

    print(f"\t> The highest value of the data set {float_array} is {result}")
    return

def calculate_product():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) * float(param_2))

    print(f"\t> The product of {param_1} * {param_2} is {result}")
    return


def get_current_date():
    exact_date_time = datetime.datetime.now()
    print("\t> " + exact_date_time.strftime('%x'))
    return

def determine_equality():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = param_1 == param_2

    print(f"\t> {param_1} == {param_2} equality check evaluates to: {result}")
    return

def run_loop_x_times(input_value_param):
    iterator = 0
    num_runs = ''
    
    while iterator < (len(input_value_param)):
        if input_value_param[iterator].isnumeric():
            num_runs += input_value_param[iterator]
        iterator += 1

    print(f"\t> Function will execute {num_runs} times.")

    iterator = 1

    while iterator <= int(num_runs):
        print(f"\t\t> Iteration #{iterator} ")
        iterator += 1 
    return
def get_string_length():
    eval_string = input("Enter the string for evaluation: ")
    string_length = len(eval_string)

    string_nospace = eval_string.replace(' ', '')
    string_length_nospace = len(string_nospace)

    print(f"\t> String Length: {string_length} | Without Whitespace: {string_length_nospace}")

    return;

def run_clear_terminal():
    # Google Search for 'how to clear terminal screen from Python code'
    os.system('cls' if os.name == 'nt' else 'clear')
    return

program_start()