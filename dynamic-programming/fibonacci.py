import timeit


def fib(n, cache=None):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    result = fib(n - 1, cache) + fib(n - 2, cache)

    cache[n] = result

    return result


if __name__ == "__main__":
    print(timeit.timeit('fib(100)', number=100, globals=globals()))
