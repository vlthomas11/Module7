def make_list():
    """Takes inputs from user and makes them into a list"""
    alist = []
    counter = 0
    while counter < 3:
        inp = int(get_input())
        alist.append(inp)
        counter = counter + 1
    return alist



def get_input():
    """Gets input from user"""
    a = input("enter a number ")
    return a

if __name__ == '__main__':
    make_list()
