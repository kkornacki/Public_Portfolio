
command_list = []

def populate_command_list():
    global command_list
    command_list.append('\t--> cmd: provides a list of available commands.')
    command_list.append('\t--> exit: ends program execution.')


# PROMPT FOR LOGIN
def prompt_for_login():
    login_user = input("Please enter your username: ")
    login_pass = input("Please enter your password: ")
    credentials = {'user': login_user, 'pass': login_pass}
    validate_credentials(credentials)

# VALIDATE USER LOGIN CREDENTIALS
def validate_credentials(credential_param):
    # DEVELOPER LOGIN PROCESS
    if credential_param['user'] == 'dev':
        if credential_param['pass'] == 'code':
            print("\t> Login successful")
            load_user_permissions('DEV')
        else:
            print("Invalid login credentials. Please try again.")
            prompt_for_login()
    
    # CEO LOGIN PROCESS
    elif credential_param['user'] == 'ceo':
        if credential_param['pass'] == 'owner':
            print('\t> Login successful')
            load_user_permissions('CEO')
        else:
            print("Invalid login credentials. Please try again.")
            prompt_for_login()
    else:
        print("Username not found. Please try again.")
        prompt_for_login()

# LOAD PERMISSIONS BASED ON THE USER PROFILE
def load_user_permissions(permission_level):
    permissions = {} # Tuple data type - immutable

    if permission_level == 'DEV':
        print("\t> Loading DEV Permissions")
        permissions = {'access_level': 6, 'require_manager_approvals': True, 'primary_geolocation': 'Corporate Headquarters - Southeast Michigan - Detroit Annex Building'}
    else:
        print("\t> Loading CEO Permissions")
        permissions = {'access_level': 10, 'require_manager_approvals': False, 'primary_geolocation': 'World Headquarters - Southeast Michigan - Detroit'}

    print(f'\t> Permissions Set: {permissions}')
    awaiting_command()

def awaiting_command():
    user_prompt = input("Enter a Command [Type \'cmd\' for a list of commands]:")
    process_user_command(user_prompt)

def process_user_command(user_prompt_param):
    if user_prompt_param == 'cmd':
      global command_list
      for item in command_list:
          print(f'{item}')

    elif user_prompt_param == 'exit':
        exit(0)

    awaiting_command()


# PRE-POPULATE THE COMMAND LIST
populate_command_list()

# INTRODUCTION
print("==== DATA STRUCTURE PRACTICE PROGRAM ====!")

prompt_for_login()