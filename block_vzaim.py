import threading
import time

lock1 =  threading.Lock()
lock2 = threading.Lock()

def tread_tasks1():
    lock1.acquire()
    print('tread_tasks1')
    time.sleep(1)
    lock2.acquire()
    print('tread_tasks1')
    lock2.release()
    lock1.release()

def tread_tasks2():
    lock2.acquire()
    print('tread_tasks2')
    time.sleep(1)
    lock1.acquire()
    print('tread_tasks2')
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=tread_tasks1)
t2 = threading.Thread(target=tread_tasks2)

t1.start()
t2.start()

t1.join()
t2.join()