# Author: Brandon Jacks
# Section: CIS 225 01
# Date: 11/18/22
# File: Player.py
#
# A simple program to define a player class.

from Player import Player

def main():
    player1 = Player()
    player1.name = 'Daniel Ortiz'
    player1.jersey_num = 2
    player1.pos = 'G'
    
    player2 = Player()
    player2.name = 'Damian Forrest'
    player2.jersey_num = 33
    player2.pos = 'F'
    
    player3 = Player()
    player3.name = 'Dallas Howell'
    player3.jersey_num = 34
    player3.pos = 'F'
    
    player_list = [player1, player2, player3]
    print('Player Names: ')
    for player in player_list:
        print(player.name)
    
    print('\nPlayer Numbers: ')
    for player in player_list:
        print(player.jersey_num)
    
    print('\nPlayer Position: ')
    for player in player_list:
        print(player.pos)

main()