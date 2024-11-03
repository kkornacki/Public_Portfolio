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
        output = help_prompt()
        print("\t======== AVAILABLE COMMANDS ========")

        for command in output:
            print(f"\t --|> {command}")
    elif input_value == "calculate true or false":
        calculate_true_false()
        last_command = "calculate true or false"
    elif input_value == "calculate remainder":
        calculate_remainder()
        last_command = "calculate remainder"
    elif input_value == "calculate sum":
        calculate_sum()
        last_command = "calculate sum"
    elif input_value == "calculate difference":
        calculate_difference()
        last_command = "calculate difference"
    elif input_value == "calculate product":
        calculate_product()
        last_command = "calculate product"
    elif input_value == "calculate average":
        calculate_average()
        last_command = "calculate average"
    elif input_value == "calculate min":
        calculate_min()
        last_command = "calculate min"
    elif input_value == "calculate max":
        calculate_max()
        last_command = "calculate max"
    elif input_value == "current date":
        get_current_date()
        last_command = "current date"
    elif input_value == "determine equality":
        determine_equality()
        last_command = "determine equality"
    elif input_value == "exit" or input_value == "end" or input_value == "close":
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
        "help",
        "exit / end / close",
        "repeat",
        "cls | clears terminal screen",
        "calculate true or false",
        "calculate remainder",
        "calculate sum",
        "calculate difference",
        "calculate average",
        "calculate min",
        "calculate max",
        "calculate product",
        "current date",
        "determine equality",
        "run loop {x-number} of times"
    )
    return available_commands


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

    print(f"The remainder of {param_1} / {param_2} is {result}")
    return

def calculate_sum():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) + float(param_2))

    print(f"The sum of {param_1} + {param_2} is {result}")
    return

def calculate_difference():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) - float(param_2))

    print(f"The difference of {param_1} - {param_2} is {result}")
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


    print(f"The average of {float_array} is {average: .2f}")
    return

def calculate_min():
    input_value_string= input("Enter the values for which you want to calculate the minimum (lowest) value: ")
    input_values = input_value_string.split()
    float_array = [float(number) for number in input_values]
 
    result = min(float_array)

    print(f"The lowest value of the data set {float_array} is {result}")
    return

def calculate_max():
    input_value_string= input("Enter the values for which you want to calculate the max (highest) value: ")
    input_values = input_value_string.split()
    float_array = [float(number) for number in input_values]
 
    result = max(float_array)

    print(f"The highest value of the data set {float_array} is {result}")
    return

def calculate_product():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = (float(param_1) * float(param_2))

    print(f"The product of {param_1} * {param_2} is {result}")
    return


def get_current_date():
    exact_date_time = datetime.datetime.now()
    print(exact_date_time.strftime("%x"))
    return

def determine_equality():
    param_1 = input("Enter the first parameter: ")
    param_2 = input("Enter the second parameter: ")
    result = param_1 == param_2

    print(f"{param_1} == {param_2} equality check evaluates to: {result}")
    return

def run_loop_x_times(input_value_param):
    iterator = 0
    num_runs = ''
    
    while iterator < (len(input_value_param)):
        if input_value_param[iterator].isnumeric():
            num_runs += input_value_param[iterator]
        iterator += 1

    print(f"Function will execute {num_runs} times.")

    iterator = 1

    while iterator <= int(num_runs):
        print(f"\t\tIteration #{iterator} ")
        iterator += 1 
    return

def run_clear_terminal():
    # Google Search for 'how to clear terminal screen from Python code'
    os.system('cls' if os.name == 'nt' else 'clear')
    return
program_start()