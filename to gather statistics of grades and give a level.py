def main():
    tuple1 = calculate(getlist())
    print('Number of scores:', tuple1[0])
    print('Average score:', tuple1[1])
    print('Standard deviation of scores:', tuple1[2])
    print('GRADE DISTRIBUTION AFTER CURVING GRADES.')
    dic = tackledict(getlist(), tuple1[1], tuple1[2])
    for i in dic:
        print(i + ':', dic[i], end='   ')


def getlist():
    infile = open('grade.txt', 'r')
    list1 = [eval(i.rstrip()) for i in infile.readlines()]
    infile.close()
    return list1


def calculate(list1):
    number = len(list1)
    average = sum(list1) / number
    sdeviation1 = 0
    for grade in list1:
        sdeviation1 += (grade - average) ** 2
    sdeviation = (sdeviation1 / number) ** .5
    return (number, average, sdeviation)


main()
