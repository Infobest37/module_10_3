from threading import Thread, Lock

x = 0
lock = Lock()
def thread1():
    global x
    for i in range(10_000_000):
        # блокируем вот этот участок кода, для этого импортируем Lock- замок который блокирует участок кода для его
        # выполнения т.е. «Lock» создаёт «замок», который может закрыть и открыть поток.
        # Есть два варианта использования данного метода это первый
        # lock.acquire()
        # x = x + 1
        # lock.release()
        # Это второй
        with lock:
            x = x + 1



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