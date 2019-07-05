def zero_sum(*nums):
    print(nums)
    s = 0
    for i in nums:
        s = s + i
    if s == 0:
        return True
    else:
        return False


def product(*args):
    print(args)
    p = 1
    for i in args:
        p = p * i
    return p


def main():
    a = {20, 19, 2, 10, 7}
    b = {x - 2 for x in a if x < 10}
    print(b)


if __name__ == '__main__':
    main()
