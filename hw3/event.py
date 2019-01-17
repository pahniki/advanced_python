"""Homework 3: Threading -> Event"""

import logging
from threading import Event
from threading import Thread

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class MyThread(Thread):
    """Base Thread for work with Event()"""

    def __init__(self, name, event):
        super().__init__()

        self.name = name

        self.event = event
        self.num_range = range(0, 101, 2) if name == "even" \
            else range(1, 101, 2)


class EvenThread(MyThread):
    """Thread class for Even numbers printing"""

    def __init__(self, name, event):
        super().__init__(name, event)

    def run(self):
        """Method representing the thread's activity."""
        for num in self.num_range:
            while self.event.is_set():
                pass
            logging.info("{} {}".format(self.name, num))
            self.event.set()


class OddThread(MyThread):
    """Thread class for Odd numbers printing"""

    def __init__(self, name, event):
        super().__init__(name, event)

    def run(self):
        """Method representing the thread's activity."""
        for num in self.num_range:
            self.event.wait()
            logging.info("{} {}".format(self.name, num))
            self.event.clear()


if __name__ == '__main__':
    eve = Event()
    eve.clear()

    thr_list = list()

    thr_list.append(EvenThread("even", eve))
    thr_list.append(OddThread("odd", eve))

    [t.start() for t in thr_list]
