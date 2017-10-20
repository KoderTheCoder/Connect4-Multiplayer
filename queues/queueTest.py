from threading import Thread
import time

end = 0
def counting(number):
	global end
	while True:
		for i in range (10):
			print i*number, '*',number,'*\n'
			time.sleep(2)
		if end==number:
			break
		return

thread1 = Thread(target=counting, args=(1, ))
thread2 = Thread(target=counting, args=(2, ))

#thread1.setDaemon(true)

end = 1
end = 2

thread1.start()
thread2.start()




