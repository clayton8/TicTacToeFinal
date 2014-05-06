#!/usr/bin/env python

import Board as board

myboard = board.Board() #Declare main Board object

#Set initial Variables
winX = False
winO = False
valid = 0

#Print initial Display
for value in range(0,50):
     print('\n')

print('__________.__       __________             __________                 ')
print('\__    __/|__|  ___ \__    __/____  ______ \__    __/ ____    _____   ')
print('   |  |   |  | /  _\   |  |  \__  \ \  ___\   |  |   / __ \  /  __ \  ')
print('   |  |   |  | | |_    |  |   / ^  \ \ \____  |  |  | |__| |(   ___/  ')
print('   |__|   |__| \___/   |__|  (___\__\ \_____\ |__|   \____/  \______\ ')
print('                   ____________________                               ')
print('\_________________/                    \______________________/\/\/\/ ')
print('\n')
print('   1: 1 - Player                          2: 2 - Player		     ')

#Take in the choice of 1 player or 2
while True:
     choice = raw_input('Enter Choice : ')
     if(choice=='1' or choice=='2'):
          break
     else:
          print("\nInvalid Entry: Enter 1 or 2\n")
#Show the display and the initial Board
print(myboard.showboard())

#Main while loop
while True:
     #While loop that continues until Player 1 enters a valid input
     while True:
          cmd = raw_input('Enter Xs Move: ')
          valid = myboard.setPiece(cmd,'X')
          if(valid == 0):
               break
          else:
               print("Spot Already Taken or Outside Range!")
     
     #Update the state of the board          
     myboard.UpdateBoard()
     print('\n')
     #Display updated board  
     print(myboard.showboard())
     #Check if X has won
     winX = myboard.CheckWin('X')
     if (winX==True):
          myboard.xWin()
          break
     
     if (choice=='2'):
          #While loop that continues until player 2 has entered a valid move
          while True:
               cmd = raw_input('Enter Os move: ')
               valid = myboard.setPiece(cmd,'O')
               if(valid == 0):
                    break
               else:
                    print("Spot Already Taken!")
     else:
          #ENTER YOUR AI's move function here
          #use myboard.setPiece(   , 'O') and store the returned value. You can use the check function above if you want or not. Your choice
          a=1
 
     #Update the state of the board          
     myboard.UpdateBoard()
     print('\n')
     #Display updated board
     print(myboard.showboard())
     #Check if O has won
     winO = myboard.CheckWin('O')
     if(winO==True):
          myboard.oWin()
          break
