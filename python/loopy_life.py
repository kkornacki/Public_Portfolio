import datetime

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
        "calculate true or false",
        "calculate remainder",
        "calculate sum",
        "calculate difference",
        "calculate average",
        "calculate min",
        "calculate max",
        "calculate product",
        "current date",
        "determine equality"
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

program_start()