def search_list(alist, value):
    alistsorted = sort_list(alist)
    if value in alist:
        return alistsorted.index(value)
    else:
        return -1


def sort_list(blist):
    sortedalist = sorted(blist)
    # return is used because I want to know what position the number is in based on numerical order
    return sortedalist


if __name__ == '__main__':
    print(search_list([22, 4, 19, 44, 32, 7, 99, 15], 22))
