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
program_start()