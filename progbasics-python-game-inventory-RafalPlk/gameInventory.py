# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inv = {'rope': 1, 'torch': 6, 'gold coin': 45, 'dagger': 1, 'arrow': 12} 
# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Displays the inventory.
def display_inventory(inventory):

    print('Inventory:')
    for k, v in inventory.items():
        print(v, k)
    print('Total number of items:', sum(inventory.values()))
    return inventory

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    
    for item in added_items:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory[item] = 1
    return inventory

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order = None):
    
    item_length = max(len(item) for item in inventory)
    count_length = max(len(str(value)) for value in inventory.values())
    line_length = item_length + count_length

    print(("Inventory:\n") + ("count".rjust(count_length + 4, " ")) + (" " * (line_length - 7)) + "item name\n" + ("-" * (line_length + 8)))
    if order == None:
        for item, count in inventory.items():
            print(str(count).rjust(count_length + 4, " ") + item.rjust(item_length + 4))
    elif order == "count,desc":
        for item, count in sorted(inventory.items(), key = lambda item: item[1]):
            print(str(count).rjust(count_length + 4, " ") + item.rjust(item_length + 4))
    elif order == "count,asc":
        for item, count in sorted(inventory.items(), key = lambda item: item[1], reverse = True):
            print(str(count).rjust(count_length + 4, " ") + item.rjust(item_length + 4))
    print("-" * (line_length + 8) + "\nTotal number of items: " + str(sum(inventory.values())))

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import.csv"):
    
    with open(filename, 'r') as temp:
        temp = list(temp)
        temp = temp[0]
        temp = temp.split(",")

    return print_table(add_to_inventory(inventory, temp))

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export.csv"):

    with open(filename, "w+") as exportation:
        export_list = []
        for k, v in inventory.items():
            if v > 1:
                for i in range(v):
                    export_list.append(k)
            else:
                export_list.append(k)

        export_str = ",".join(export_list)
        exportation.write(export_str)
