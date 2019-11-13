#_________________
#some useful funcs
#_________________

def printy(s):
    print('\n' + ' '*8  + '='*len(s) + '\n'+ ' '*8 + s + '\n' + ' '*8 + '='*len(s) + '\n')

def stringy(j):
    j = '\n' + j + '\n'
    return j

def dstringy(j):
    j = stringy(stringy(j))
    return j

def prints(j):
    print(stringy(j))

def print2s(j):
    print(dstringy(j))

def chappy(n):
    return 'Chapter' + str(n)

def pchan(x):
    printy(chappy(x))
