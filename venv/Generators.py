def generate_values():
    yield 5
    yield "Temp"
    yield True
    yield 'e'


def main():
    values=generate_values()
    print(next(values))
    print(next(values))


if __name__ == '__main__':
    main()
