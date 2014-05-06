class Piece:
     "A single Piece"
     def __init__(self,data):
          self.item = data

     def __str__(self):
          return self.item

     def setPiece(self,data):
          self.item = data

     def getPiece(self):
          return self.item


class Board:
     def __init__(self):
          self.state = "   |   |   -----------   |   |   -----------   |   |   "
          self.Piece = {}
          self.usedSlots = []
          for value in range(1,10):
               self.Piece[value] = Piece(' ')
			   
     def __str__(self):
          return self.state

     def setPiece(self,data,player):
          invalid = False
          i = 0;
          #Check if the placement is valid
          for value in self.usedSlots:
               if(self.usedSlots[i] == data):
                    invalid = True
               i=i+1
               
          if invalid == False:
               self.Piece[int(data)].setPiece(player)
               self.usedSlots.append(data)
               return 0
          else:
               return 1
     
     def cpuMove(self):
	#Used to see if the CPU or the user has 2 items in a row.
	#if the user has 2 pieces in a row the CPU will block
	#if the CPU has two pieces in a row the CPU will win
	dangerValue = [0,0,0,0,0,0,0,0]
	#If there are no lines that are 2 or -2 then it will use this to find
	#a line with a free spot to place an item
	lineFilled = [0,0,0,0,0,0,0,0]
	
	#Top Left Piece
	if str(self.Piece[1]) == 'X':
		dangerValue[0]+= 1
		dangerValue[3]+= 1
		dangerValue[6]+= 1
		lineFilled[0]+=1
                lineFilled[3]+=1
                lineFilled[6]+=1
	elif str(self.Piece[1]) == 'O':
                dangerValue[0]-= 1
                dangerValue[3]-= 1
                dangerValue[6]-= 1
                lineFilled[0]+=1
                lineFilled[3]+=1
                lineFilled[6]+=1	
	#Middle Top
	if str(self.Piece[2]) == 'X':
                dangerValue[0]+= 1
                dangerValue[4]+= 1
                lineFilled[0]+=1
                lineFilled[4]+=1
        elif str(self.Piece[2]) == 'O':
                dangerValue[0]-= 1
                dangerValue[4]-= 1
                lineFilled[0]+=1
                lineFilled[4]+=1
	#Top Right
        if str(self.Piece[3]) == 'X':
                dangerValue[0]+= 1
                dangerValue[5]+= 1
                dangerValue[7]+= 1
                lineFilled[0]+=1
                lineFilled[5]+=1
                lineFilled[7]+=1
        elif str(self.Piece[3]) == 'O':
                dangerValue[0]-= 1
                dangerValue[5]-= 1
                dangerValue[7]-= 1
                lineFilled[0]+=1
                lineFilled[5]+=1
                lineFilled[7]+=1
	#Middle Left
        if str(self.Piece[4]) == 'X':
                dangerValue[1]+= 1
                dangerValue[3]+= 1
                lineFilled[1]+=1
                lineFilled[3]+=1
        elif str(self.Piece[4]) == 'O':
                dangerValue[1]-= 1
                dangerValue[3]-= 1
                lineFilled[1]+=1
                lineFilled[3]+=1
	#Middle Middle
        if str(self.Piece[5]) == 'X':
                dangerValue[1]+= 1
                dangerValue[4]+= 1
                dangerValue[6]+= 1
		dangerValue[7]+= 1
                lineFilled[1]+=1
                lineFilled[4]+=1
                lineFilled[6]+=1
                lineFilled[7]+=1
        elif str(self.Piece[5]) == 'O':
                dangerValue[1]-= 1
                dangerValue[3]-= 1
                dangerValue[6]-= 1
		dangerValue[7]-= 1
                lineFilled[1]+=1
                lineFilled[4]+=1
                lineFilled[6]+=1
                lineFilled[7]+=1
	#Middle Right
        if str(self.Piece[6]) == 'X':
                dangerValue[1]+= 1
                dangerValue[5]+= 1
		lineFilled[1]+=1
		lineFilled[5]+=1
        elif str(self.Piece[6]) == 'O':
                dangerValue[1]-= 1
                dangerValue[5]-= 1
                lineFilled[1]+=1
                lineFilled[5]+=1
	#Bottom Left
        if str(self.Piece[7]) == 'X':
                dangerValue[2]+= 1
                dangerValue[3]+= 1
                dangerValue[7]+= 1
                lineFilled[2]+=1
                lineFilled[3]+=1
		lineFilled[7]+=1
        elif str(self.Piece[7]) == 'O':
                dangerValue[2]-= 1
                dangerValue[3]-= 1
                dangerValue[7]-= 1
                lineFilled[2]+=1
                lineFilled[3]+=1
                lineFilled[7]+=1
	#Bottom Middle
        if str(self.Piece[8]) == 'X':
                dangerValue[2]+= 1
                dangerValue[4]+= 1
		lineFilled[2]+=1
		lineFilled[4]+=1
        elif str(self.Piece[8]) == 'O':
                dangerValue[2]-= 1
                dangerValue[4]-= 1
                lineFilled[2]+=1
                lineFilled[4]+=1
	#Bottom Right
        if str(self.Piece[9]) == 'X':
                dangerValue[2]+= 1
                dangerValue[5]+= 1
                dangerValue[6]+= 1
                lineFilled[2]+=1
                lineFilled[5]+=1
                lineFilled[6]+=1
        elif str(self.Piece[9]) == 'O':
                dangerValue[2]-= 1
                dangerValue[5]-= 1
                dangerValue[6]-= 1
                lineFilled[2]+=1
                lineFilled[5]+=1
                lineFilled[6]+=1
	print(dangerValue)
	print (lineFilled)
	pieceSet = -1
	counter = 0
	#Check for a winning spot or a place to block
	for value in dangerValue:
		#If there is a place to win select that line and move on
		if (value == -2):
			pieceSet = counter
			break
		#If there is a place to block select that line but keep looking for places to go.
		elif (value == 2):
			pieceSet = counter
		counter += 1
	#If there was a place to block or win use that row.
	if pieceSet != -1:
		 return str(self.findBlock(pieceSet))
	#Otherwise find an empty space to place an Piece
	else:
		counter = 0
		for value in lineFilled:
			if(value < 3):
				pieceSet = counter
			counter += 1
		return  str(self.findBlock(pieceSet))

     def findBlock(self, line):
	#This function finds the first open space in a row and will return it as a number.
	space = 0
	if str(self.Piece[1]) == ' ':
		if line == 0 or line == 3 or line == 6:
			space = 1

        if str(self.Piece[2]) == ' ':
                if line == 0 or line == 4:
                        space = 2

        if str(self.Piece[3]) == ' ':
                if line == 0 or line == 5 or line == 7:
                        space = 3

        if str(self.Piece[4]) == ' ':
                if line == 1 or line == 3:
                        space = 4

        if str(self.Piece[5]) == ' ':
		if line == 1 or line == 4 or line == 7 or line == 6:
			space = 5
		  
        if str(self.Piece[6]) == ' ':
                if line == 1 or line == 5:
                        space = 6

        if str(self.Piece[7]) == ' ':
                if line == 2 or line == 3 or line == 7:
                        space = 7

        if str(self.Piece[8]) == ' ':
                if line == 2 or line == 4:
                        space = 8

        if str(self.Piece[9]) == ' ':
                if line == 2 or line == 5 or line == 6:
                        space = 9

	return space	

     def UpdateBoard(self):
          self.state = ' ' + self.state.replace(' ',str(self.Piece[1]))[1:2] + ' | ' + self.state.replace(' ',str(self.Piece[2]))[5:6] + ' | ' + self.state.replace(' ',str(self.Piece[3]))[9:10] + ' ----------- ' + self.state.replace(' ',str(self.Piece[4]))[22:23] + ' | ' + self.state.replace(' ',str(self.Piece[5]))[26:27] + ' | ' +  self.state.replace(' ',str(self.Piece[6]))[30:31] + ' ----------- ' +  self.state.replace(' ',str(self.Piece[7]))[44:45] + ' | ' + self.state.replace(' ',str(self.Piece[8]))[48:49] + ' | ' + self.state.replace(' ',str(self.Piece[9]))[52:53]
           
     def CheckWin(self,player,turn):
          if str(self.Piece[1])==player and str(self.Piece[2])==player and str(self.Piece[3])==player: return True
          if str(self.Piece[4])==player and str(self.Piece[5])==player and str(self.Piece[6])==player: return True
          if str(self.Piece[7])==player and str(self.Piece[8])==player and str(self.Piece[9])==player: return True
          if str(self.Piece[1])==player and str(self.Piece[4])==player and str(self.Piece[7])==player: return True
          if str(self.Piece[2])==player and str(self.Piece[5])==player and str(self.Piece[8])==player: return True
          if str(self.Piece[3])==player and str(self.Piece[6])==player and str(self.Piece[9])==player: return True
          if str(self.Piece[1])==player and str(self.Piece[5])==player and str(self.Piece[9])==player: return True
          if str(self.Piece[3])==player and str(self.Piece[5])==player and str(self.Piece[7])==player: return True
          if turn==5: return True
          return False
		  
     def showboard(self):
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
          print(' 1 | 2 | 3')
          print('-----------')
          print(' 4 | 5 | 6')
          print('-----------')
          print(' 7 | 8 | 9')
          print('\n=====================================================================\n')
          BoardDisp = self.state[:11] + '\n' + self.state[11:22] + '\n' + self.state[22:33] + '\n' + self.state[33:44] + '\n' + self.state[44:]
          return BoardDisp

     def xWin(self):
          print(' ____    ____     ____             ____  __                           ')
          print(' \   \  /   /     \   \    ___    /   / |__|  _             ______    ')
          print('  \   \/   /       \   \  /   \  /   /   __  / \_____      /  ____/   ')
          print('   \      /         \   \/     \/   /   |  | |   __  \    /  /___     ')
          print('   /      \          \             /    |  | |  /  \  |  /___    /    ')
          print('  /   /\   \          \     /\    /     |  | |  |  |  |  ____/  /     ')
          print(' /___/  \___\          \___/  \__/      |__| |__|  |__| /______/      ')

     def oWin(self):
          print('  __________      ____             ____  __                           ')
          print(' |          |     \   \    __     /   / |__|  _             ______    ')
          print(' |   ____   |      \   \  /   \  /   /   __  / \_____      /  ____/   ')
          print(' |  |    |  |       \   \/     \/   /   |  | |   __  \    /  /___     ')
          print(' |  |____|  |        \             /    |  | |  /  \  |  /___    /    ')
          print(' |          |         \     /\    /     |  | |  |  |  |  ____/  /     ')
          print(' |__________|          \___/  \__/      |__| |__|  |__| /______/      ')

