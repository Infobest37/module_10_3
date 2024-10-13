from threading import Thread, Lock

x = 0
lock = Lock()
def thread1():
    global x
    for i in range(10_000_000):
        with lock:
            x = x + 1

def tread_tasks():
    global x
    for i in range(10_000_000):
        try:
            lock.acquire()
            x = x + 1
        finally:
            lock.release()



def main():
    global x
    x = 0
    t1 = Thread(target=thread1)
    t2 = Thread(target=thread1)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x)