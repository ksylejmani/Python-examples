from time import clock


def generate_values():
    yield 5
    yield "Temp"
    yield True
    yield 'e'


def evens_less_than(n):
    for i in range(2, n, 2):
        yield i


def compute_time():
    start = clock()
    for i in range(1000000):
        print(i)
    end = clock()
    print("Time elapsed: " + str(end - start))


def oscillate(a, b):
    for i in range(a, b, 1):
        yield i
        yield -i


def main():
    compute_time()


if __name__ == '__main__':
    main()
