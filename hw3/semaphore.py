"""Homework 3: Threading -> Semaphore"""

import logging
from threading import Semaphore
from threading import Thread

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class SemaThread(Thread):
    """Thread for work with Semaphore()"""

    semaphores = [Semaphore(1), Semaphore(0)]

    def __init__(self, name):
        super().__init__()

        self.name = name

        self.order = (0, 1) if self.name == "even" else (1, 0)
        self.num_range = range(self.order[0], 101, 2)

    def run(self):
        """Method representing the thread's activity."""

        for num in self.num_range:
            self.semaphores[self.order[0]].acquire()
            logging.info("{} {}".format(self.name, num))
            self.semaphores[self.order[1]].release()


if __name__ == '__main__':
    thr_list = list()

    thr_list.append(SemaThread("even"))
    thr_list.append(SemaThread("odd"))

    [t.start() for t in thr_list]
