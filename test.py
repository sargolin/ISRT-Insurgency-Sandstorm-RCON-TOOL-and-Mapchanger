import time, threading, concurrent.futures, multiprocessing

startTime = time.time()

x = 1

def testfunc():
    global x
    while x == 1:
        print(f"Running for the {x} time")
        time.sleep(1)


t1 = threading.Thread(target=testfunc)
t1.start()



print("What value should x take?")
y = input()
x = int(y)



print("Finished Script")
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))