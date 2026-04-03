# Day 6: Escaping the Maze
# Note: This code was built for the web-based environment at reeborg.ca
# It defines custom functions and uses a while loop to navigate the robot.


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

