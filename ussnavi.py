#!/usr/bin/env python
# -*- coding: utf-8 -*

# def display_grid():
#     print("    +---+---+---+---+---+---+---+---+---+---+")
#     print("    | A | B | C | D | E | F | G | H | I | J |")
#     print("+----+---+---+---+---+---+---+---+---+---+---+")
#     for i, row in enumerate(grid, start=1):
#         print(f"| {i:<2} | " + " | ".join(row) + " |")
#         print("+----+---+---+---+---+---+---+---+---+---+---+")
#
# def position_to_indices(position):
#     col = ord(position[0].lower()) - ord('a')
#     row = int(position[1:]) - 1
#     return row, col

grid = [[' . ' for x in range(10)] for x in range(10)]

def affiche (table):
    print("  |  A  |   B  |   C  |   D  |   E  |   F  |   G  |   H  |   I  |   J  |")
    for i in range(10):
        print( i+1 , table[i])

shipsData = \
    {
        "aircraftCarrier": ['b2', 'c2', 'd2', 'e2', 'f2'],
        "cruiser": ['a4', 'a5', 'a6', 'a7'],
        "destroyer": ['c5', 'c6', 'c7'],
        "submarine": ['g5', 'h5', 'i5'],
        "torpedo": ['d9', 'e9'],
    }

def ships(column , row):

    letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    letter = column.upper()
    number = int(row)
    shoot = column + row

    if  grid[number-1][letters[letter]] == ' X ' or grid[number-1][letters[letter]] == ' o ':
        print("deja shooter ici !! ")
        return 0

    else:
        for ship, position in shipsData.items():

            if shoot in position:

                position.remove(shoot)
                grid[number - 1][letters[letter]] = ' X '
                print(f"toucher en {shoot} !!")

                if len(position) < 1:
                    print(f"bravo {ship} couler !!!!")
                return 1

            else:
                grid[number - 1][letters[letter]] = ' o '
                print("looper !!")
                return 0

if __name__ == '__main__':

    shipCount = sum( len(position) for position in shipsData.values())
    affiche(grid)
    print(f"nombre de tire pour abattre toute la flotte : {shipCount}")

    while shipCount > 0:

        column = (input("sur quel colone voulez vous tirez ?  A a J: "))
        row = (input("sur quel ligne voulez vous tirez ?  1 a 9 : "))
        shipCount -= ships(column, row)
        affiche(grid)
        print(f"reste : {shipCount} shoot pour abattre tout les bateaux ")

    print("bravo toute la flotte a etait couler ! ")
