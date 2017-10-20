class Player:	

	def __init__(self, tokens):
		self.token = tokens
		self.name = raw_input("Please enter your name:")
	
	def move(self):
		position = input('Your move: ') 
		return position

	def getToken(self):
		return self.token
		

	def getName(self):
		return self.name
