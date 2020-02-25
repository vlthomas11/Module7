def make_list():
    alist = []
    counter = 0
    while counter < 3:
        inp = int(get_input())
        alist.append(inp)
        counter = counter + 1


def get_input():
    pass
    # count = 0
    # a = 'i'
    # b = []
    # while count < 3:
    #     a = input("enter a number")
    #     count = count + 1
    #     b.append(a)
    # print(b)


if __name__ == '__main__':
    get_input()
