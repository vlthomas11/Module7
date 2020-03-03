import os as os

file_name = 'student_info.txt'


def write_to_file(tup):
    f = open(file_name, 'a+')
    for i in tup:
        f.writelines(i)
        f.writelines('\t')
    f.writelines('\n')
    f.close()


def get_student_info(**kwargs):
    name = kwargs['name']
    num_scores = int(input("how many scores would you like to enter for " + str(name) + "? "))
    counter = 0
    name_and_scores = [name]
    while counter < num_scores:
        score = input("please enter a score for " + str(name) + " ")
        counter += 1
        name_and_scores.append(score)

    tup = tuple(i for i in name_and_scores)

    write_to_file(tup)


def read_from_file():
    f = open(file_name, 'r')
    line1 = f.read()
    print(line1)
    f.close()


if __name__ == '__main__':
    get_student_info(name='Vickilee')
    get_student_info(name='Larry')
    get_student_info(name='Leona')
    get_student_info(name='Julia')
    read_from_file()
