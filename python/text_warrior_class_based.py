# See PEP (Python Enhancement Proposals)
# PEP 8 is the most commonly used style guide

# PROMPT FOR LOGIN
def prompt_for_login():
    login_user = input("Please enter your username: ")
    login_pass = input("Please enter your password: ")
    credentials = {'user': login_user, 'pass': login_pass}
    validate_credentials(credentials)

def validate_credentials(credential_param):
    # DEVELOPER LOGIN PROCESS
    if credential_param['user'] == 'dev':
        if credential_param['pass'] == 'code':
            print("> Login successful")
            load_user_permissions('DEV')
        else:
            print("Invalid login credentials. Please try again.")
            prompt_for_login()
    # CEO LOGIN PROCESS
    elif credential_param['user'] == 'ceo':
        if credential_param['pass'] == 'owner':
            print('> Login successful')
            load_user_permissions('CEO')
        else:
            print("Invalid login credentials. Please try again.")
            prompt_for_login()
    else:
        print("User not found.")
        prompt_for_login()

def load_user_permissions(permission_level):
    if permission_level == 'DEV':
        print("> Loading DEV Permissions")
    else:
        print("> Loading CEO Permissions")

# INTRODUCTION
print("Welcome to Text Warrior Version 1!")

prompt_for_login()

# OBTAIN CHARACTER DATA BASED ON USERNAME


# PROMPT FOR USER COMMAND

# COMMAND: UPDATE CHARACTER INFO

# COMMAND: PURCHASE ITEM

# COMMAND: SELL ITEM

# COMMAND: CALCULATE BANK BALANCE

def gather_user_info():
    character_details = {}
    print("Welcome to the Python Playground Realm!")
    char_name = input("Enter a character name: ")
    char_class = input("Enter a character class [Mage, Warrior, Archer, Nomad]: ")
    char_level = input("Enter a character level [Apprentice, Full-Fledged, Master, Overlord]: ")
    character_details['name'] = char_name
    character_details['class'] = char_class
    character_details['level'] = char_level

    return character_details

def create_welcome_message(character_info):
    message = f"Welcome {character_info['name']} - {character_info['level']} {character_info['class']} of the Python Playground Realm!"
    print(message)

#character_info = gather_user_info()
#create_welcome_message(character_info)

