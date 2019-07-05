def next_number(li):
    if len(li) == 0:
        return 1
    for j in range(1, len(li) + 1):
        if j not in li:
            return j
    return len(li)


def reverse(lst):
    n = len(lst)
    for i in range(int(n / 2)):
        temp = lst[i]
        lst[i] = lst[n - i - 1]
        lst[n - i - 1] = temp


def pretty_print_matrix(m):
    for i in range(len(m)):
        k = m[i]
        for j in range(len(k)):
            print(str(m[i][j]), " ", end=" ")
        print()
    print("-------------------------------")


def create_matrix(k):
    rez = []
    for i in range(k):
        rez.append([])
        for j in range(k):
            rez[i].append(1)
    return rez


def create_list():
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst = [x for x in range(1, 11)]
    # lst = [x for x in range(1, 5)] + [5, 6, 7, 8, 9, 10]
    return lst


def row_column_equal(lst_2d):
    for i in range(len(lst_2d)):
        for j in range(len(lst_2d)):
            n = 0
            for k in range(len(lst_2d)):
                if lst_2d[i][k] == lst_2d[k][j]:
                    n = n + 1
                else:
                    break
            if n == len(lst_2d):
                return True
    return False


def tic_tac_toe(ttt):
    for i in range(len(ttt)):
        px = 0
        p0 = 0
        px2 = 0
        p02 = 0
        px3 = 0
        p03 = 0
        px4 = 0
        p04 = 0
        for j in range(len(ttt)):
            if ttt[i][j] == 'X':
                px = px + 1
            elif ttt[i][j] == '0':
                p0 = p0 + 1
            if ttt[j][i] == 'X':
                px2 = px2 + 1
            elif ttt[j][i] == '0':
                p02 = p02 + 1
            if ttt[j][j] == 'X':
                px3 = px3 + 1
            elif ttt[j][j] == '0':
                p03 = p03 + 1
            if ttt[j][len(ttt) - j - 1] == 'X':
                px4 = px4 + 1
            elif ttt[j][len(ttt) - j - 1] == '0':
                p04 = p04 + 1
        if px == len(ttt) | px2 == len(ttt) | px3 == len(ttt) | px4 == len(ttt):
            return 'X'
        elif p0 == len(ttt) | p02 == len(ttt) | p03 == len(ttt) | p04 == len(ttt):
            return '0'
        else:
            return ' '


def main():
    ttt = [['0', '0', 'X'],
           ['X', 'X', 'X'],
           ['X', ' ', '0']]
    print(tic_tac_toe(ttt))


if __name__ == '__main__':
    main()
