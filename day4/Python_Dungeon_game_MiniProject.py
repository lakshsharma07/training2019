# Dungeon Game

"""
Challenge 1
    It would be a 2 dimensional maze game 
    We would put the player in a random room in the grid 
    We would also put a monster in a random room in the grid
    We would out a door in a random room in the grid 
    The player would then move around the grid to find the door
    Don’t let he player go out of the edges of the grid 
    If they hit the monster room they are eaten by the monster 
    or if they reach the gate they win 
    Grid of Room = Collection of Coordinates 
    Player is a tuple, it contains two values  

"""

import random

room_grid=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
monster_pos=(random.randint(0,3),random.randint(0,3))
exit_pos=(random.randint(0,3),random.randint(0,3))
while(exit_pos == monster_pos):
    exit_pos=(random.randint(0,3),random.randint(0,3))
player_pos=(random.randint(0,3),random.randint(0,3))
while((player_pos == monster_pos) or (player_pos == exit_pos)):
    exit_pos=(random.randint(0,3),random.randint(0,3))
while True:
    user_input=input()
    if(player_pos == exit_pos):
        print('player wins')
    if(player_pos == monster_pos):
        print('eaten by the monster')

    


"""
Challenge 2
Welcome message is getting printed every-time
Can we display the grid for the visual  

"""