import socket
from threading import Thread

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 4999)

serverSock.bind(server_address)
print "Starting up on %s port %s" % server_address

serverSock.listen(2)

print 'Waiting for player 1'
connection1, client1 = serverSock.accept()
print 'Player 1 has connected'
connection1.send(chr(1))
player1name = connection1.recv(1024)

print 'Waiting for player 2'
connection2, client2 = serverSock.accept()
print 'Player 2 has connected'
connection2.send(chr(2))
player2name = connection2.recv(1024)

connection1.sendall(player2name)
connection2.sendall(player1name)

lastToken = 'O'
position = 1


while position != '8':
	if lastToken=='O':
		try:
			position=ord(connection1.recv(1))
			connection2.send(chr(position))
			lastToken='X'
			connection2.send(lastToken)
			print 'recieved ', position, ' from P1 ', player1name,'\t', client1
			if ord(connection1.recv(1))==1:
				print 'P1 has won'
				break
		except:
			print 'Player1 has disconnected, resetting'
			break		
	else:
		try:
			position=ord(connection2.recv(1))
			connection1.send(chr(position))
			lastToken='O'
			connection1.send(lastToken)
			print 'recieved ', position, ' from P2 ', player2name,'\t', client2
		except:
			print 'Player 2 has disconnected, resetting'
			break
serverSock.close()
