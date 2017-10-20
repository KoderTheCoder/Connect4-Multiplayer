import socket
import board
from game import Game

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 4999)
print 'Connecting to server'
clientSock.connect(server_address)
print 'connected to Koders Game Server on  port 9999'

playerNum=ord(clientSock.recv(1))
game1 = Game(playerNum)

print 'Waiting for another player'
clientSock.send(game1.player.getName())

opponent = clientSock.recv(1024)
print 'Connected with ', opponent

lastToken = 'O'

while True:

	if lastToken!=game1.player.getToken():
		while True:
			move = game1.player.move()
			if game1.updateBoard(move,game1.player.getToken()):
				break
		clientSock.send(chr(move))

		if game1.checkWin(game1.player.getToken()):
			print 'You win!!'
			clientSock.send(chr(1))
			clientSock.close()
		else:
			clientSock.send(chr(0))

		lastToken = game1.player.getToken()

	else:
		print opponent,'s turn'
		position = ord(clientSock.recv(1))
		lastToken = clientSock.recv(1)
		game1.updateBoard(position, lastToken)
		if game1.checkWin(lastToken):
			game1.printBoard()
			print opponent, ' Wins... Shutting down now so you can reflect on this loss.'
			clientSock.send(chr(1))
			clientSock.close()
			wait = input('Press any button to continue')
		else:
			clientSock.send(chr(0))
	game1.printBoard()

print 'Something went wrong, Disconnecting...'
clientSock.close()



