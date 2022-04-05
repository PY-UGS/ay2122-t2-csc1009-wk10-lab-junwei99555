def moduleCodes(i):
    switcher = {
        'CSC1006':'Mathematics 2',
        'CSC1007':'Operating Systems',
        'CSC1008':'Data Structure and Algorithm',
        'CSC1009':'Object Oriented Programming',
        'CSC1010':'Computer Networks'
    }
    return switcher.get(i, 'Invalid Code')


print(moduleCodes(input('Enter module code: ')))