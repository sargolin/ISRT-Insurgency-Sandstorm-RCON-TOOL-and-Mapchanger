''' threading_count_seconds1.py
count seconds needed to complete a task
counter runs in the background
tested with Python27 and Python33  by  vegaseat  19sep2014
'''
import threading
import time
import sys
# make this work with Python2 or Python3
class queryIntervall(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1000 of a second
    '''
    def __init__(self, interval=1):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False
    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            # update count value
            self.value += self.interval
            print("Go")

    def peek(self):
        '''
        return the current value
        '''
        return self.value
    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value
# create the class instance
count = queryIntervall()
# start the count
count.start()
# test the counter with a key board response time
# or put your own code you want to background-time in here
# you can always peek at the current counter value
e = input("Press Enter")
e = input("Press Enter again")
# stop the count and get elapsed time
seconds = count.finish()
print("You took {} seconds between Enter actions".format(seconds))
