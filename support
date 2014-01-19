######## Supporting functions for the YoungTab Class and parition files ####
def add(a,b):
    return a+b
def lcm(n):
    """Returns the least common multiple of all numbers from 1 to n"""
    a = 1
    for i in range(1, n+1):
        a = ( a * i ) / fractions.gcd(a,i)
def increasing(List, strict=True):
    """Checks if a list of numbers is increasting. Returns true or false"""
    if strict:
        for i in xrange(len(List)):
            if i + 1 >= len(List):
                break
            if List[i] >= List[i+1]:
                return False
    if not strict:
        for i in xrange(len(List)):
            if i + 1 >= len(List):
                break
            if List[i] > List[i+1]:
                return False
    return True
def match(list1, list2):
    a = list1[:]
    b = list2[:]
    values = []
    while len(a) != 0:
         for i in b:
             if a[-1] < i:
                 k = (a[-1],i)
                 a.remove(a[-1])
                 b.remove(i)
                 values += [k]
                 break
    return values
def createtupnet(list1):
    list2 = []
    k = max(list1)
    for i in list1:
        list2 += [((i-1)%k,i%k,0,0)]
    return list2
def newtup(tupe1, tupe2):
    a, b, c, d = 0, 0, 0, 0
    if len(tupe1)!= len(tupe2):
        raise IndexError
    for i in xrange(len(tupe1)):
        if tupe1[1] != tupe2[0]:
            c , d = tupe2[0], tupe1[1]
            a, b = tupe2[0], tupe1[1]
        if tupe1[1] == tupe2[0]:
            c, d = tupe1[1], tupe1[1]
    return (a,b,c,d)

    
