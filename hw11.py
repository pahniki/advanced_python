"""HW11. Fibonacci"""

from time import time

from cython_pkg.cython_pkg.cython_fibo import cython_fibo
from ext_fibo import ext_fibo


def calc_time(func, n):
    start = time()
    result = func(n)
    print("Time: {}".format((time() - start) * 10 ** 3))

    return result


def python_fib(n):
    """Fibonacci on Python"""
    i = 0
    a, b = 0, 1
    if n < 2:
        return n
    while i < n:
        a, b = b, a + b
        i += 1
    return a


if __name__ == '__main__':
    N = 40

    print("Python")
    print(calc_time(python_fib, N))

    print("\nCython")
    print(calc_time(cython_fibo, N))

    print("\nExtension")
    print(calc_time(ext_fibo, N))
