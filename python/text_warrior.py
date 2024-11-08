

# DEFINE WEAPONS PER CLASS
weapons_magic = {
    "Wooden Wand": 
    {
        "Power": 1,
        "Accuracy": 3,
        "Hands_Required": 1,
        "Members_Only": False
    },

    "Wooden Staff":
    {
        "Power": 1,
        "Accuracy": 1,
        "Hands_Required": 2,
        "Members_Only": False
    }
}
weapons_ranger = {
    "Wooden Bow": 
    {
        "Power": 1,
        "Accuracy": 3,
        "Hands_Required": 1,
        "Members_Only": False
    },

    "Slingshot":
    {
        "Power": 1,
        "Accuracy": 1,
        "Hands_Required": 2,
        "Members_Only": False
    }
}
weapons_warrior = {
    "Wooden Sword": 
    {
        "Power": 1,
        "Accuracy": 3,
        "Hands_Required": 1,
        "Members_Only": False
    },

    "Butter Knife":
    {
        "Power": 1,
        "Accuracy": 1,
        "Hands_Required": 2,
        "Members_Only": False
    }
}

god_sword = {
    "Power": 1000,
    "Accuracy": 100
}
god_bow = {
    "Power": 2000,
    "Accuracy": 200
}
god_staff = {
    "Power": 3000,
    "Accuracy": 300
}
god_weapons = {
    "God Sword": god_sword,
    "God Bow" : god_bow,
    "God Staff" : god_staff
}


# DEFINE ARMOUR PER CLASS
armour_magic = {}
armour_range = {}
armor_warrior = {}

# DEFINE PERKS PER CLASS
perks_magic = {}
perks_range = {}
perks_warrior = {}

def start_game():

    character = character_initialization()

    while character["char_name"] == '':
        new_char_name = input("Please enter a valid character name: ")
        character["char_name"] = new_char_name
        
    while character["char_gender"] == '':
        new_char_gender = input("Please enter your characters gender [Enter \'M\' or \'F\']: ")
        character["char_gender"] = new_char_gender

    if character["char_gender"] == 'm' or character["char_gender"] == 'M':
        character["char_prefix"] = 'Sir'
    else:
        character["char_prefix"] = 'Madam'

    while character["char_class"] == '':
        new_char_class = input("Please enter your characters class [Warrior, Ranger, Mage, Godmode]: ")
        character["char_class"] = new_char_class

    confirm_character = input("Confirm your selections & being your adventure? [Y\\N]:")

    if confirm_character == 'Y' or confirm_character == 'y':
        greet_new_user(character)
    else:
        restart_game()

def restart_game():
    start_game()

def character_initialization():
    character = {
        "char_name": '',
        "char_gender": '',
        "char_prefix": '',
        "char_class": '',
        "lvl_attack": 1,
        "exp_attack": 0,
        "lvl_strength": 1,
        "exp_strength": 0,
        "lvl_defense": 1,
        "exp_defense": 0,
        "lvl_range": 1,
        "exp_range": 0,
        "lvl_magic": 1,
        "exp_magic": 0
    }
    return character

def greet_new_user(character_param):
    print(f"\t> Greetings {character_param["char_prefix"]} {character_param["char_name"]}! Welcome to Text Warrior!")
    print("\t> Our first order of business is to choose your starting weapon!")
    
    get_class_weapons(character_param["char_class"])
    

def get_class_weapons(char_class_param):
    
    weapons_options = {}

    if char_class_param == "Mage" or char_class_param == "mage":
        global weapons_magic
        weapons_options = weapons_magic
    elif char_class_param == "Ranger" or char_class_param == "ranger":
        global weapons_ranger
        weapons_options = weapons_ranger
    elif char_class_param == "Warrior" or char_class_param == "warrior":
        global weapons_warrior
        weapons_options = weapons_warrior
    elif char_class_param == "Godmode" or char_class_param == "godmode":
        global god_weapons
        weapons_options = god_weapons
    
    print("\t> Available items for your character class are: ")

    iterator = 0

    for weapon, weapon_attribute in weapons_options.items():
        weapon_power = weapon_attribute["Power"]
        weapon_accuracy = weapon_attribute["Accuracy"]
        print(f"\t\t> Option #{iterator} : {weapon} --> Power: {weapon_power} | Accuracy {weapon_accuracy}")
        iterator += 1
    iterator = 0

    selected_weapon = input("Please enter the option # you would like to equip: ")
    equipped_weapon = weapons_options[selected_weapon]
    print(f"{equipped_weapon}")

def equip_char_active_weapon():
    pass    

start_game()