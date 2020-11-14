import timeit


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(timeit.timeit('fib(25)', number=100, globals=globals()))
