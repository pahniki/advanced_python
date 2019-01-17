"""Homework 3: Threading -> Lock"""

import logging
from threading import Lock
from threading import Thread

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class LockThread(Thread):
    """Thread for work with Lock"""

    locks = [Lock(), Lock()]

    def __init__(self, name):
        super().__init__()

        self.name = name

        self.order = (0, 1) if self.name == "even" else (1, 0)
        self.num_range = range(self.order[0], 101, 2)

        if self.name == "even":
            self.locks[1].acquire()

    def run(self):
        """Method representing the thread's activity."""

        for num in self.num_range:
            self.locks[self.order[0]].acquire()
            logging.info("{} {}".format(self.name, num))
            self.locks[self.order[1]].release()


if __name__ == '__main__':
    thr_list = list()

    thr_list.append(LockThread("even"))
    thr_list.append(LockThread("odd"))

    [t.start() for t in thr_list]
