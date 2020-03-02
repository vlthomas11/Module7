def make_list():
    """Takes inputs from user and makes them into a list"""
    alist = []
    counter = 0
    for i in range(3):
        inp = get_input()
        inpint = int(inp)
        alist.insert(counter,inpint)
        counter += 1
    return alist


def get_input():
    """Gets one input from user and returns it"""
    a = input('enter a number ')
    return a


if __name__ == '__main__':
    make_list()
