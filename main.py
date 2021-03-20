from room import Room
from character import Enemy
from character import Character

kitchen = Room('Kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room('Dining Hall')
dining_hall.set_description('A large room with ornate golden decorations on each wall.')

ballroom = Room('Ballroom')
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

ballroom.link_room(dining_hall, "east")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up dude?")
dave.set_weakness("banana")

dining_hall.set_character(dave)

catrina = Character("Catrina", "A friendly skeleton")
catrina.set_conversation("Hello there!")

ballroom.set_character(catrina)

current_room = kitchen

dead = False

while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant == None:
            print("There is no one here to fight with")
        else:
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("You won the fight!")
                current_room.set_character(None)
            else:
                print("Game over, you lose")
                dead = True
