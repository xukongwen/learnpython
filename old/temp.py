# -- coding: utf-8 --

import os

inv = {'arrow': 12, 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# STEP 1 #########################################################
def display_inventory(**kwargs):
    print("Inventory:")
    for item, count in kwargs.items():
        print("%s %s" % (count, item))
    print("Total number of items: {}\n".format(sum(inv.values())))


# STEP 2 #########################################################
# check for same items in list and dictionary and merge their values
# or update the dict with new keys-values
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.update({item: 1})

# STEP 3 #########################################################
# sort dictionary by input argument, format and print to the screen
def print_table(order = None):
    sorted_list = sorted(inv.items(), key=lambda x:x[1])
    m = max(len(word) for word in inv) + 3                              # +3 for aesthetic purposes only
    print("Inventory:")
    print("{0:>5} {1:>{m}}".format("Count", "Item name", m = m))
    print("-----------------------")
    if order == "count,desc":
        for i in reversed(range(len(sorted_list))):
            print("{0:>5} {1:>{m}}".format(sorted_list[i][1], sorted_list[i][0], m = m))
    elif order == "count,asc":
        for i in range(len(sorted_list)):
            print("{0:>5} {1:>{m}}".format(sorted_list[i][1], sorted_list[i][0], m = m))
    elif order == None:
        display_inventory(**inv)
    print("-----------------------")
    print("Total number of items: {}\n".format(sum(inv.values())))


# STEP 4 #########################################################
def import_inventory(filename = "import_inventory.csv"):
    file_list = []
    with open(filename, "r") as file:
        for line in file:
            row = line.split(",")                                       # split lines at the comma.
            first = row[0]                                              # assign first and second values
            second = row[1]                                             # to temporary variables.
            minus_line = len(second)-1                                  # get rid of the newline character
            second = second[0:minus_line]                               # here.
            file_list.extend([[first,second]])                          # add values to the file_list array.

    for lista in range(1,len(file_list)):                               # ignore the first line,
        if file_list[lista][0] in inv:                                  # update or assign new inventory
            inv[file_list[lista][0]] += int(file_list[lista][1])        # according to value
        else:
            inv[file_list[lista][0]] = int(file_list[lista][1])


# STEP 5 #########################################################
def export_inventory(filename = "export_inventory.csv"):
    if os.path.exists(filename) == False:
        with open(filename, 'w') as file:
            for key, value in inv.items():
                file.write('{0},{1}\n'.format(key, value))
    else:
        with open(filename, 'w') as file:
            for key, value in inv.items():
                file.write('{0},{1}\n'.format(key, value))

# MAIN PROGRAM ###################################################
def game_inventory():
    display_inventory(**inv)
    add_to_inventory(inv,dragon_loot)
    print_table("count,desc")
    import_inventory("import_inventory.csv")
    display_inventory(**inv)
    export_inventory()

game_inventory()
