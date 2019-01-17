"""Homework 3: Threading -> Condition"""

import logging
from threading import Condition
from threading import Thread

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class ConditionThread(Thread):
    """Thread for work with Condition()"""

    cv = Condition()

    def __init__(self, name, timeout=1.0):
        super().__init__()

        self.name = name
        self.timeout = timeout

        self.num_range = range(0, 101, 2) if name == "even" \
            else range(1, 101, 2)

    def run(self):
        """Method representing the thread's activity."""
        with self.cv:
            for num in self.num_range:
                self.cv.wait(self.timeout)

                logging.info("{} {}".format(self.name, num))

                self.cv.notifyAll()


if __name__ == '__main__':
    timeout = 1

    thr_list = list()

    thr_list.append(ConditionThread("even", timeout=timeout))
    thr_list.append(ConditionThread("odd", timeout=timeout * 2))

    [t.start() for t in thr_list]
