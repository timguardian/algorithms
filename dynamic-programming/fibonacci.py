import timeit


def fib(n, cache=None):
    a = 1  # fib(i - 2)
    b = 1  # fib(i - 1)

    for i in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print(timeit.timeit('fib(100)', number=100, globals=globals()))
