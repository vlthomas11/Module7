def average_scores(*args,**kwargs):
    total = 0
    tuplelength = len(args)
    count = 0
    for i in args:
        y = args[count]
        total = total + y
        count += 1

    avg = total/tuplelength
    name = kwargs['first_name'] + " " + kwargs['last_name']
    GPA = kwargs['GPA']
    course = kwargs['course']
    return "Result: " + "name = " + name + " gpa = " + str(GPA) + "course = " + course + " with current average " + str(avg)



if __name__ == '__main__':
    print(average_scores(4,3,2,4, first_name = 'Michelle', GPA = '3.5', course = 'Python',last_name = 'Ruse'))
