def main():
    while True:
        try:
            n = eval(input('Enter the n:'))
            t = (matrix1, matrix2) = getmatrix(n)
            calculate(n, t[0], t[1])
            break
        except (SyntaxError, NameError):
            print('Please enter the right number!')


def getmatrix(n):
    # 获得矩阵1
    matrix1 = []
    for i in range(1, n + 1):
        line = []
        for j in range(1, n + 1):
            elements = eval(input('Enter element {0} of \
the line {1} of matrix1:'.format(j, i)))
            line.append(elements)
        matrix1.append(line)
    # 获得矩阵2
    matrix2 = []
    for i in range(1, n + 1):
        line = []
        for j in range(1, n + 1):
            elements = eval(input('Enter element {0} of \
the line {1} of matrix2:'.format(j, i)))
            line.append(elements)
        matrix2.append(line)
    print('Your matrix1:', matrix1)
    print('Your matrix2:', matrix2)
    return (matrix1, matrix2)


def calculate(n, m1, m2):
    newmatrix = []
    for i in range(n):
        newline = []
        for j in range(n):
            thesum = 0
            for k in range(n):
                thesum += m1[i][k] * m2[k][j]
            newline.append(thesum)
        newmatrix.append(newline)
    print('The answer of matrix1 * matrix2 is:', newmatrix)


main()
