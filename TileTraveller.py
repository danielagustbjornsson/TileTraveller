
# def way_choser
    # program það takes in what ways are alowed and the room that there in lets the user choose and sents room there in then
# def room_checker
    # if room == x
        # set North = x
        # set South = x
        # set East = x
        # set West = x
    # check what room they are in and showes what moves are alowed

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
        