def fibonacci(n):
    if n <= 1:
        return n
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-1)+lucas(n-2)