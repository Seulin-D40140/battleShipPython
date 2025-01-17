#!/usr/bin/env python
# -*- coding: utf-8 -*
from model.ShipModel import ship
from  model.GridModel import gridM

grid : list[list[str]] = [[' . ' for x in range(10)] for x in range(10)]

def affiche ( table : list[list[str]] ) :
    print("  |  A  |   B  |   C  |   D  |   E  |   F  |   G  |   H  |   I  |   J  |")
    for i in range(10):
        print( i+1 , table[i])

shipsDatas = \
    {
        "aircraftCarrier": ship('aircrafter' , ['b2', 'c2', 'd2', 'e2', 'f2'], 0),
        "cruiser": ship('cruiser' , ['a4', 'a5', 'a6', 'a7'] , 0),
        "destroyer": ship('destroyer' , ['c5', 'c6', 'c7'] , 0),
        "submarine": ship('submarine' , ['g5', 'h5', 'i5'] , 0),
        "torpedo": ship('torpedo' , ['d9', 'e9'] , 0)
    }

def shipGame( column : str , row : str ):

    letters : dict[str , int] = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    letter : str = column.upper()
    number : int = int(row)
    shoot : str = column + row

    if  grid[number-1][letters[letter]] == ' X ' or grid[number-1][letters[letter]] == ' o ':

        return 0

    else:
        for shipName , shipDInfos in shipsDatas.items():
            if shoot in shipDInfos.position:
                grid[number - 1][letters[letter]] = ' X '
                shipDInfos.isActive += 1
                if shipDInfos.isActive == shipDInfos.shipLength():
                    print(f"bravo {shipName} couler !!!!")
                return 1

            else:
                grid[number - 1][letters[letter]] = ' o '

if __name__ == '__main__':
    affiche(grid)
    shipCount : int = sum(shipInfo.shipLength() for shipInfo in shipsDatas.values())
    while shipCount > 0:

        column = (input("sur quel colone voulez vous tirez ?  A a J: "))
        row = (input("sur quel ligne voulez vous tirez ?  1 a 9 : "))
        shipResult : int  = shipGame(column , row)
        if shipResult == 1:
            print("toucher ! ")
        elif shipResult == 0:
            print("deja shooter ici !! ")
        else:
            print("looper !!")
        shipCount = sum(shipInfo.shipLength() for shipInfo in shipsDatas.values())
        affiche(grid)

        print(f"reste : {shipCount} shoot pour abattre tout les bateaux ")
        print(shipsDatas)

    print("bravo toute la flotte a etait couler ! ")
