#Ernesto del Puerto, [27/06/2022 20:02]
# Clase 13
# Ejercicio 3
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def init(self, threadID, name, counter):
        threading.Thread.init(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print ("Exiting " + self.name)
def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Pedro", 1)
thread2 = myThread(2, "Pablo", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")
    