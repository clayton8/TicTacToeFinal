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

          
     
		  
     def UpdateBoard(self):
          self.state = ' ' + self.state.replace(' ',str(self.Piece[1]))[1:2] + ' | ' + self.state.replace(' ',str(self.Piece[2]))[5:6] + ' | ' + self.state.replace(' ',str(self.Piece[3]))[9:10] + ' ----------- ' + self.state.replace(' ',str(self.Piece[4]))[22:23] + ' | ' + self.state.replace(' ',str(self.Piece[5]))[26:27] + ' | ' +  self.state.replace(' ',str(self.Piece[6]))[30:31] + ' ----------- ' +  self.state.replace(' ',str(self.Piece[7]))[44:45] + ' | ' + self.state.replace(' ',str(self.Piece[8]))[48:49] + ' | ' + self.state.replace(' ',str(self.Piece[9]))[52:53]
           
     def CheckWin(self,player):
          if str(self.Piece[1])==player and str(self.Piece[2])==player and str(self.Piece[3])==player: return True
          if str(self.Piece[4])==player and str(self.Piece[5])==player and str(self.Piece[6])==player: return True
          if str(self.Piece[7])==player and str(self.Piece[8])==player and str(self.Piece[9])==player: return True
          if str(self.Piece[1])==player and str(self.Piece[4])==player and str(self.Piece[7])==player: return True
          if str(self.Piece[2])==player and str(self.Piece[5])==player and str(self.Piece[8])==player: return True
          if str(self.Piece[3])==player and str(self.Piece[6])==player and str(self.Piece[9])==player: return True
          if str(self.Piece[1])==player and str(self.Piece[5])==player and str(self.Piece[9])==player: return True
          if str(self.Piece[3])==player and str(self.Piece[5])==player and str(self.Piece[7])==player: return True
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

