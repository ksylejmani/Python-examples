def generate_values():
    yield 5
    yield "Temp"
    yield True
    yield 'e'


def evens_less_than(n):
    for i in range(2, n, 2):
        yield i


def main():
    for i in evens_less_than(12):
        print(i, end=" ")
    print()


if __name__ == '__main__':
    main()
