"""Homework 3: Threading -> Timer"""

import logging
from threading import Timer
from time import sleep

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

even_start_num = 0
odd_start_num = 1


def timer_thr(name, start_num, sleep_time):
    """Function for Thread with Timer"""
    for num in range(start_num, 101, 2):
        logging.info("{} {}".format(name, num))
        sleep(sleep_time)


if __name__ == '__main__':
    sleep_time = 1

    thr_list = list()

    thr_list.append(
        Timer(sleep_time / 2, timer_thr,
              args=["even", even_start_num, sleep_time]))
    thr_list.append(
        Timer(sleep_time, timer_thr,
              args=["odd", odd_start_num, sleep_time]))

    [t.start() for t in thr_list]
