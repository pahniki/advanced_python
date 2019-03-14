def cython_fibo(n):
    """Fibonacci on Cython"""
    i = 0
    a, b = 0, 1
    if n < 2:
        return [a, b][n]
    while i < n:
        a, b = b, a + b
        i += 1
    return a
