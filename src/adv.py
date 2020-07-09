import code

from room import Room
from player import Player
from item import Item

class style():
    BLUE = '\033[34m'
    RED = '\033[31m'
    YELLOW = '\033[33m'

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']




#Items for room
room['outside'].add_item(Item("Flask", "Stores liquid"))
room['foyer'].add_item(Item("Egg", "Don't drop it!"))
room['overlook'].add_item(Item("Binoculars", "Helps you see things"))
room['narrow'].add_item(Item("Water", "Goes well with the flask"))
room['treasure'].add_item(Item("Key", "This could come in handy later"))

#
# Main
#

directions = ['n', 's', 'e', 'w']
item_actions = ['get', 'take', 'drop']
p = Player("James", room ['outside'])

print(style.BLUE + "Welcome to the Adventure Game!")
print(f'Welcome {p.name}!\nPlease choose a direction by moving North(n), South(s), East(e), or West(w)\nTo exit the game, enter q\n')
print(style.YELLOW + f'You are in the {p.current_room.name} - {p.current_room.description}\n')
p.current_room.print_items()

while True:
    
    selection = input('Where do you want to go next? ').lower().split(' ')

    if len(selection) > 2 or len(selection) < 1:
        print("Please enter a one or two word input for the game. To get a list of valid commands, type 'help' or 'h")
    elif len(selection) == 2:
        if selection[0] in item_actions:
            if selection[0] == 'get' or selection[0] == 'take':
                item = p.current_room.search_items(selection[1])
                p.current_room.drop_item(item)
                p.add_item(item)
                item.on_take(item)
            elif selection[0] == 'drop':
                item = p.search_items(selection[1])
                p.current_room.add_item(item)
                p.drop_item(item)
                item.on_drop(item)
        else: 
            print("Please enter a valid action for the item. To get a list of valid commands, type 'help' or 'h")
    else:
        if selection[0] == 'q' or selection[0] == 'quit':
            print(f'Thanks for playing {p.name}!') 
            break

        if selection[0] == 'h' or selection[0] == 'help':
            print("Valid game commands:\n'n' - Move North\n's' - Move South\n'e' - Move East\n'w' - Move West\n'i' or 'inventory' - Get a list of your current items\n'get' or 'take' - Pick up an item\n'drop' - Drop an item\n'q' or 'quit' - Exit Game\n")
            continue

        if selection[0] == 'i' or selection[0] == 'inventory':
            p.print_items()
            continue

        if selection[0] in directions:
            try:
                p.move_room(selection[0])
                print(f'You are in the {p.current_room.name} - {p.current_room.description}\n')
                p.current_room.print_items()
            except AttributeError:
                print('No room there, try another direction')
        else:
            print(style.RED + "Movement not possibe! Enter another direction (n, s, e, w) to move around the map")

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
