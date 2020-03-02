def average_scores(*args,**kwargs):
    total = 0
    tuplelength = len(args)
    count = 0
    result = "Result: "
    for i in args:
        y = args[count]
        total = total + y
        count += 1

    avg = total/tuplelength
    #name = kwargs['name']

    for key, value in kwargs.items():
        result = result + ("%s = %s" % (key,value)) + " "
    result = result + "with current average " + str(avg)
    return result


if __name__ == '__main__':
    print(average_scores(4,3,2,4, name = 'Michelle Ruse', GPA = '3.5', course = 'Python'))
