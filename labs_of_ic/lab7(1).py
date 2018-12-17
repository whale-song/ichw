import random
out = []

def qs(lst):
    '''quick sort list lst, return the sorted list'''
    global out
    minlist = []
    maxlist = []
    mid = []
    if len(lst) <= 1:
        out += lst
    else:
        for i in lst:
            if i < ((max(lst)+min(lst))/2):
                minlist.append(i)
            elif i > ((max(lst)+min(lst))/2):
                maxlist.append(i)
            else:
                mid.append(i)
        qs(minlist)
        out += mid
        qs(maxlist)
    return out

def testqs():
    lst = []

    for i in range(100):
        lst.append(random.randint(1,200))

    print(lst)
    sortedlst = qs(lst)
    assert(sorted(lst) == sortedlst)
    print('Test pass')

if __name__ == '__main__':
	testqs()