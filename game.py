from players import Player

class Game:

	def __init__(self,num):
		if num==1:
			self.player = Player('X')
		else:
			self.player = Player('O')
		self.board = [['*']*8 for n in range(8)]
		
        def checkDiag(self, iStep, iStart, jStep, jStart, iStartStep, jStartStep, pToken):
	        for k in range(7,0,-1):
        	        j=jStart
			count=0
        	        for i in range(iStart,k,iStep):
                	        if self.board[i][j]==pToken:
                        	        count+=1
                       		else:
	                                count=0
        	                if count==4:
                	                return 1
              	        j+=jStep
               		iStart+=iStartStep
                	jStart+=jStartStep
 	        return 0
 	
	def checkWin(self, pToken):
		count = 0
		for i in range (7):
			for j in range (7):
				if self.board[i][j]==pToken:
					count += 1
				else:
					count = 0
				if count==4:
					return 1
				count = 0
                if self.checkDiag(1,0,1,0,0,1,pToken):
                        return 1
                if self.checkDiag(-1,7,1,0,0,1,pToken):
                        return 1
                if self.checkDiag(1,0,-1,7,0,-1,pToken):
                        return 1
                if self.checkDiag(-1,7,-1,7,0,-1,pToken):
                        return 1

		return 0
			 		



	def updateBoard(self, position, token):
		row = 7
		pos = position-1
		while True:
			try:
				if self.board[row][pos]=='*':
                			self.board[row][pos]=token
					return 1
				else:
					row -= 1
			except:
				print 'Invalid move, try again'
				break
                return 0

        def printBoard(self):
                for index in range(len(self.board)):
                       print self.board[index], "\n"
                return
