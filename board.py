class GameBoard:	
	
	def updateBoard(self, board, position, token):
		board[7][position-1]=token
		return

	def printBoard(self, board):
		for index in range(len(board)):
			print board[index], "\n"
		return
