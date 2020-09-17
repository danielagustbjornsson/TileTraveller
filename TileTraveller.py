# def way_choser
    # program takes in what ways are alowed and the room that there in lets the user choose and sents room there in then
# def room_checker
    # if room == x
        # set North = x
        # set South = x
        # set East = x
        # set West = x
    # check what room they are in and showes what moves are alowed

def way_mover (room, North, South, East, West):
    room_2 = room.split(",")
        
    if North:
        room_int = int(room_2[1])
        room_3 = str(room_int +1)
        room_4 = room_2[0] + "," + room_3
    if South:
        room_int = int(room_2[1])
        room_3 = str(room_int - 1)
        room_4 = room_2[0] + "," + room_3
    if East:
        room_int = int(room_2[0])
        room_3 = str(room_int + 1)
        room_4 = room_3 + ","+ room_2[1]
    if West:
        room_int = int(room_2[0])
        room_3 = str(room_int - 1)
        room_4 = room_3 + ","+ room_2[1]
    return room_4

def way_cheker(way, North, South, East, West):
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

room = "1,1"
while room != "3,1":
    North, South, East, West = room_checker(room)
    print("You can travel:", end=" ")
    if North:
        print("(N)orth or", end=" ")
    if East:
        print("(E)ast or", end=" ")
    if South:
        print("(E)ast", end=" ")
    if West:
        print("(W)est", end=" ")
    way = input("Direction: ")

    way_check, North_way, South_way, East_way, West_way = way_cheker(way, North, South, East, West)
    

