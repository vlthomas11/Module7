
def search_array(a_array,item):
    a = sort_array(a_array)
    if item in a:
        return a.index(item)
    else:
        return -1


def sort_array(a_array):
    sortedarray = sorted(a_array)
    return sortedarray

if __name__ == '__main__':
    print(search_array([3,5,10,6,15],6))
