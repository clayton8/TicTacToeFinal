#!/usr/bin/env python

import Board as board

myboard = board.Board() #Declare main Board object

#Set initial Variables
winX = False
winO = False
valid = 0
TurnCount = 0

#Print initial Display
for value in range(0,50):
     print('\n')

while True:
     print('__________.__       __________             __________                 ')
     print('\__    __/|__|  ___ \__    __/____  ______ \__    __/ ____    _____   ')
     print('   |  |   |  | /  _\   |  |  \__  \ \  ___\   |  |   / __ \  /  __ \  ')
     print('   |  |   |  | | |_    |  |   / ^  \ \ \____  |  |  | |__| |(   ___/  ')
     print('   |__|   |__| \___/   |__|  (___\__\ \_____\ |__|   \____/  \______\ ')
     print('                   ____________________                               ')
     print('\_________________/                    \______________________/\/\/\/ ')
     print('\n')
     print('   1: 1 - Player        2: 2 - Player      3: Instructions            ')

#Take in the choice of 1 player or 2

     choice = raw_input('Enter Choice : ')
     if(choice=='1' or choice=='2'):
          break
     
     elif(choice=='3'):
          myboard.Instruct()
     else:
          for value in range(0,50):
               print('\n')
          print("\nInvalid Entry: Enter 1, 2 or 3\n")


#Show the display and the initial Board
print(myboard.showboard())

#Main while loop
while True:
     
     
     #While loop that continues until Player 1 enters a valid input
     while True:
          cmd = raw_input('Enter Xs Move: ')
	  if cmd == '1' or cmd == '2' or cmd == '3' or cmd == '4' or cmd == '5' or cmd == '6' or cmd == '7' or cmd =='8' or cmd == '9':
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
     winX = myboard.CheckWin('X',TurnCount)
     if (winX==True):
          myboard.xWin()
          break
     #Draw will always happen after x's Turn
     #Check if Draw
     TurnCount = TurnCount + 1
     winDraw = myboard.CheckWin('3',TurnCount)
     print(winDraw)
     if(winDraw == True):
          print("Draw!! ")
          break
     
     if (choice=='2'):
          #While loop that continues until player 2 has entered a valid move
          while True:
		if cmd == '1' or cmd == '2' or cmd == '3' or cmd == '4' or cmd == '5' or cmd == '6' or cmd == '7' or cmd =='8' or cmd == '9':
               		cmd = raw_input('Enter Os move: ')
              		valid = myboard.setPiece(cmd,'O')
               		if(valid == 0):
                    		break
               		else:
                    		print("Spot Already Taken!")
     else:
	  #Will place a CPU move on the board. 
	  myboard.setPiece( myboard.cpuMove(), 'O')
 
     #Update the state of the board          
     myboard.UpdateBoard()
     print('\n')
     #Display updated board
     print(myboard.showboard())
     #Check if O has won
     winO = myboard.CheckWin('O',TurnCount)
     if(winO==True):
          myboard.oWin()
          break
     
     
