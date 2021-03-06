# def way_choser
    # moves the user to a sertened room according to the user input
# def room_checker
    # checks what is alloed in the room that the user is in
    # and sents out what the user is allowed to do in the room to be usen elsewhere
    # if room == x
        # set North = x
        # set South = x
        # set East = x
        # set West = x
# def way_checker
    # checkes if the users input is allowed in that room
# def room_reader
    # showes what the user what moves are allowed
import random

def way_mover (room, North, South, East, West):
    room_split = room.split(",")
        
    if North: # moves the users room location up
        room_int = int(room_split[1])
        room_3 = str(room_int +1)
        room_lok = room_split[0] + "," + room_3

    if South: # moves the users room location down
        room_int = int(room_split[1])
        room_3 = str(room_int - 1)
        room_lok = room_split[0] + "," + room_3

    if East: # moves the users room location right
        room_int = int(room_split[0])
        room_3 = str(room_int + 1)
        room_lok = room_3 + ","+ room_split[1]

    if West: # moves the users room location left
        room_int = int(room_split[0])
        room_3 = str(room_int - 1)
        room_lok = room_3 + ","+ room_split[1]

    return room_lok

def way_checker(way, North, South, East, West):
    way_2 = way.lower()
    North_way = False
    South_way = False
    East_way = False
    West_way = False
    way_check = False

    if North and way_2 == "n":
        way_check = True
        North_way = True

    if South and way_2 == "s":
        way_check = True
        South_way = True

    if East and way_2 == "e":
        way_check = True
        East_way = True

    if West and way_2 == "w":
        way_check = True
        West_way = True

    if way_check == False:
        print("Not a valid direction!")

    return way_check, North_way, South_way, East_way, West_way

def room_checker (room):
    North = False
    South = False
    East = False
    West = False

    if room == "1,1":
        North = True
        # Starting room

    elif room == "1,2":
        North = True
        South = True
        East = True

    elif room == "1,3":
        South = True
        East = True

    elif room == "2,1":
        North = True

    elif room == "2,2":
        South = True
        West = True

    elif room == "2,3":
        West = True
        East = True

    elif room == "3,1":
        North = True
        # wining room

    elif room == "3,2":
        North = True
        South = True

    elif room == "3,3":
        West = True
        South = True

    return North, South, East, West

def room_reader(room):
    if room == "1,1":
        print("(N)orth.")
        # starting room

    elif room == "1,2":
        print("(N)orth or (E)ast or (S)outh.")

    elif room == "1,3":
        print("(E)ast or (S)outh.")

    elif room == "2,1":
        print("(N)orth.")

    elif room == "2,2":
        print("(S)outh or (W)est.")

    elif room == "2,3":
        print("(E)ast or (W)est.")

    elif room == "3,1":
        print("Victory!")
        # wining room

    elif room == "3,2":
        print("(N)orth or (S)outh.")

    elif room == "3,3":
        print("(S)outh or (W)est.")

def pull_lever(room):
    if room == "1,2" or room == "2,2" or room == "2,3" or room == "3,2":
        lever = random_pull_lever()
        if lever == "y" or lever == "Y":
            return True
    return False

def random_pull_lever():
    choices = ["y", "n"]
    lever = random.choice(choices)
    print("Pull a lever (y/n):", lever)
    return lever


def random_choice_ways():
    ways = ["n", "e", "s", "w"]
    way = random.choice(ways)
    print("Direction:", way)
    return way
    


def main():
    room = "1,1" # Starting room 
    coin_counter = 0
    seed = int(input("Input seed: "))
    random.seed(seed)
    moves = 0

    while room != "3,1": # loop this until the user is in the winning room
        North, South, East, West = room_checker(room)
        

        print("You can travel:", end=" ")
        
        room_reader(room)

        way = random_choice_ways()

        way_check, North_way, South_way, East_way, West_way = way_checker(way, North, South, East, West)

        if way_check: # cheking if the move was valid
            room = way_mover(room, North_way, South_way, East_way, West_way)
            moves += 1
            if pull_lever(room):
                coin_counter += 1
                print("You received 1 coin, your total is now", coin_counter, end="")
                print(".")
        else:
            moves +=1

    if room == "3,1": # cheking the victory room
        print("Victory! Total coins", coin_counter, end="")
        print(". Moves", moves, end=".")
        print("")

con = "y"
while con != "n":
    main()
    con = input("Play again (y/n): ")


    

