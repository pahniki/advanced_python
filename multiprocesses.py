"""Homework 4. Multiprocessing.
Print numbers from queue in 2 processes.
First will print odd numbers, second - even.
"""

from multiprocessing import current_process
from multiprocessing import Lock
from multiprocessing import Process
from multiprocessing import Queue


def get_num(qu, acquire_lock, release_lock):
    while True:
        acquire_lock.acquire()

        if qu.empty():
            release_lock.release()
            break

        print(current_process().name, qu.get())

        release_lock.release()


if __name__ == '__main__':

    odd_lock = Lock()
    even_lock = Lock()

    qu = Queue()

    # Prepare lock and queue
    odd_lock.acquire()

    for item in range(0, 101):
        qu.put(item)

    print(qu.qsize())

    odd_p = Process(target=get_num, args=(qu, odd_lock, even_lock))
    even_p = Process(target=get_num, args=(qu, even_lock, odd_lock))

    odd_p.start()
    even_p.start()

    odd_p.join()
    even_p.join()

    print(qu.qsize())
