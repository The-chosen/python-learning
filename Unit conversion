def main():
    print('UNITA OF LENGTH')
    print('{0:12}{1:12}{2:12}'.format('inches', 'furlongs', 'yards'))
    print('{0:12}{1:12}{2:12}'.format('rods', 'miles', 'fathoms'))
    print('{0:12}{1:12}{2:12}'.format('meters', 'kilometers', 'feet'))
    calculate(getinfo())


def getinfo():
    convertfrom = input('Units to convert from:')
    convertto = input('Units to convert to:')
    inlength = eval(input('Enter length in {0}:'.format(convertfrom)))
    return (convertfrom, convertto, inlength)


def calculate(tuple1):
    thedict = {'inch': 0.083333, 'furlong': 660 , 'yard': 3,
    'rod': 16.5, 'mile': 5280, 'fathom': 6,
    'meter': 3.28155, 'kilometer': 3281.5, 'feet': 1}
    output = tuple1[-1] * (thedict[tuple1[0]] / thedict[tuple1[1]])
    print('Length in' + tuple1[1] + ':{:.4f}'.format(output))


main()
