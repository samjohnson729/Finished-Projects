import random
import string

password = str(random.randrange(100000,1000000))

location = [1,1]
keyhole = "small, hidden keyhole in a bookshelf"
safe = "large, iron safe in the corner or the office. It looks like it hasn't been touched in years"
man = "mysterious, looming man ransacking the house. You try to duck back behind the door, but he sees you. He charges at you, gun in hand"
floorboard = "creeky, loose floorboard that seems to be a little loose"

kitchen = "Kitchen. There is a round table in the middle with four chairs. The oven is turned on! A delicious smell comes from the oven; somebody has been here recently. You listen and you can here sounds coming from the next room."
bathroom = "Bathroom. It is very luxurious with a bath/shower, toilet, and two sinks. Everything is very clean and orderly."
master = "master bedroom. There is a king sized bed against the wall with a night stand on either side. A dresser is in the corner as well."
office = "office. There is a desk, some filing cabinets, and a small bookshelf."
living = "living room. There are two couches, a TV, and a table in this room."
library = "library. There are tall shelves full of books, and a fancy oak desk at one end of the room."
guest = "guest bedroom. It is a small, neat room with a bed and small dresser."
dining = "dining room. A fancy table spans the middle of this room and a crystal chandelier hangs above the table. There is a small hole in one corner of the room."
closet = "closet. Coats are hung and boots line the wall."

key = "key hidden under the rug"
code = "code inside the bookshelf scribbled on an old sheet of paper. The writing is faint, but you can make out the numbers '2319'"
will = "will inside the safe. There is some fine print at the bottom of the page that is too small for you to read"
magnifying_glass = "magnifying_glass next to the bed. Your crazy old unce must have used it to read"
riddle = "riddle at the bottom of the will. It says: \n   WARNING: in order to find the next clue, you may need to get your hands dirty. \n      ps. Don't be afraid to wash them"
lighter = "lighter that the man was carrying"
sword = "sword that looks shiny and recently sharpened. It is balanced precariously on top of a vase"
paper = "paper that seems to be blank. Why would he hide a blank sheet of paper?"
CLUE = ("clue that was written in invisible ink! It says: %s" % password)
screwdriver = "screwdriver sitting on the ground. This will probably not be useful"
treasure = "10 million dollars worth of gold! Congradulations, you will inherit the entire estate"

rooms = [[[bathroom,paper],[office,safe],[master,magnifying_glass]],[[kitchen,sword],[living,key],[library, keyhole]],[[guest,man],[dining,screwdriver],[closet,floorboard]]]
inventory = []
items = [["key","code","magnifying_glass","sword","lighter","screwdriver"],["keyhole","safe","will","man","paper","floorboard"],["code","will","riddle","lighter","CLUE","treasure"]]
itemsStrings = [[key,code,magnifying_glass,sword,lighter,screwdriver],[keyhole,safe,will,man,paper,floorboard],[code,will,riddle,lighter,CLUE,treasure]]

print("Your acclectic great uncle has just passed away. For years he had bragged about his wealth, but everyone knew he had no money. Everyone knew he collected ")
print("antiques and was intruiged by treasure maps. The solicitor said his estate is left to you if you can find his hidden prize")
print("You are in the living room, the central room of this nine-room house. \n")

print("Here is the list of commands you can use: \n    Walk (direction)        ex: Walk North \n    Take (item)             ex: Take key")
print("    Search                  use this to find items \n    Use (item) on (object)  ex: Use axe on tree")
print("    Check Inventory         use this to check your inventory")
print()

while True:
    command = str(raw_input()).lower()
    if command == '':
        continue
    if command.split()[0] == 'walk':
        if command.split()[1] == 'north' and location[1] == 2:
            print("You ran into a wall!")
            continue
        if command.split()[1] == 'east' and location[0] == 2:
            print("You ran into a wall!")
            continue
        if command.split()[1] == 'south' and location[1] == 0:
            print("You ran into a wall!")
            continue
        if command.split()[1] == 'west' and location[0] == 0:
            print("You ran into a wall!")
            continue
        if command.split()[1] == 'north' and location[1] != 2:
            if location == [2,1]:
                print("Enter the passcode to enter this door: ")
                if str(raw_input()) == password:
                    print("Success.")
                    location = [2,2]
                    print("You are currently in the %s" % rooms[location[0]][location[1]][0])
            else:
                location = [location[0],location[1] + 1]
                print("You are currently in the %s" % rooms[location[0]][location[1]][0])
            continue
        if command.split()[1] == 'east' and location[0] != 2:
            if location == [1,2]:
                print("This door is bolted shut. You cannot open it.")
            else:
                location = [location[0] + 1,location[1]]
                print("You are currently in the %s" % rooms[location[0]][location[1]][0])
            continue
        if command.split()[1] == 'south' and location[1] != 0:
            location = [location[0],location[1] - 1]
            print("You are currently in the %s" % rooms[location[0]][location[1]][0])
            continue
        if command.split()[1] == 'west' and location[0] != 0:
            location = [location[0] - 1,location[1]]
            print("You are currently in the %s" % rooms[location[0]][location[1]][0])
            continue
        print("The direction you entered is not valid. Please only use North, East, South, and West.")
        continue

    if command == 'check inventory':
        if inventory == []:
            print("You don't have anything in your inventory yet.")
            continue
        for i in range(len(inventory)):
            print("%d. %s" % (i + 1, inventory[i]))
        continue

    if command.split()[0] == 'use':
        if(len(command.split()) == 2):
            print("You did not use the 'use' command correctly")
            continue
        if command.split()[1] in inventory and command.split()[3] in inventory:
            for i in range(len(items[0])):
                if command.split()[1] == items[0][i] and command.split()[3] == items[1][i]:
                    print("It worked! You discovered a %s. You took it!" % itemsStrings[2][i])
                    inventory.append(items[2][i])
                    break
            else:
                print("The %s has no effect on the %s" % (command.split()[1], command.split()[3]))
            continue
        if command.split()[1] in inventory and command.split()[3] == rooms[location[0]][location[1]][1].split()[2]:
            if command.split()[1] == "sword" and command.split()[3] == "man" and location == [2,0]:
                print("You killed him! Yikes that was too close. You found a lighter on him, and took it.")
                inventory.append(items[2][3])
                continue
            for i in range(len(items[0])):
                if command.split()[1] == items[0][i] and command.split()[3] == items[1][i]:
                    print("It worked! You found a %s. You took it!" % itemsStrings[2][i])
                    inventory.append(items[2][i])
                    break
            else:
                print("The %s has no effect on the %s" % (command.split()[1], command.split()[3]))
            continue
        if command.split()[1] not in inventory:
            print("You do not have the %s." % command.split()[1])
        if command.split()[3] != rooms[location[0]][location[1]][1].split()[2]:
            print("There is no %s in the %s" % (command.split()[3], rooms[location[0]][location[1]][0]))
        continue

    if command.split()[0] == 'take':
        if command.split()[1] == rooms[location[0]][location[1]][1].split()[0] and (rooms[location[0]][location[1]][1].split()[0] in items[0] or rooms[location[0]][location[1]][1].split()[0] == "paper"):
            inventory.append(rooms[location[0]][location[1]][1].split()[0])
            print("You picked up the %s!" % rooms[location[0]][location[1]][1].split()[0])
            rooms[location[0]][location[1]][1] = 0
        elif rooms[location[0]][location[1]][1].split()[2] in items[1] and command.split()[1] == rooms[location[0]][location[1]][1].split()[2]:
            print("You can not pick up a %s" % rooms[location[0]][location[1]][1].split()[2])
        else:
            print("No such thing can be found in this room...")
        continue

    if command.split()[0] == 'search':
        if rooms[location[0]][location[1]][1]:
            if location == [2,0] and "sword" in inventory:
                print("You found a %s!" % rooms[location[0]][location[1]][1])
                continue
            elif location == [2,0]:
                print("You found a %s!" % rooms[location[0]][location[1]][1])
                print("You were killed. Better luck next time...")
                break
            elif location == [0,0] and "riddle" in inventory:
                print("You found a piece of paper hidden! Expecting a secret message, you hastily unfold it; unfortunately, it appears to be blank...")
                continue
            elif location == [0,0]:
                print("There doesn't seem to be anything out of the ordinary here")
            else:
                print("You found a %s!" % rooms[location[0]][location[1]][1])
        else:
            print("There is nothing to be found...")
        continue

    else:
        print("The command (verb) you entered was not recognized. Please only use commands from the given list.")
