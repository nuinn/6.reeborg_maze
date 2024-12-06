def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_north():
    while not is_facing_north():
        turn_left()
        
def face_right():
    face_north()
    turn_right()
    
def try_north():
    face_north()
    while front_is_clear():
        move()
    return right_is_clear()    
        
def try_east():
    face_right()
    while front_is_clear():
        move()
        if at_goal():
            break
            
def try_south():
    face_north()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    face_right()
    return front_is_clear()
            
def try_left_and_out():
    face_north()
    turn_left()
    if not front_is_clear():
        return False
    move()
    way_out = right_is_clear()
    if not way_out:
        try_east()
    return way_out
            
while not at_goal():
    way_out = try_north()
    if way_out:
        try_east()    
    left_and_out = try_left_and_out()
    if left_and_out:
        continue  
    right_turn = try_south()
    if right_turn:
        try_east()
    else:
        turn_left()
        turn_left()
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
