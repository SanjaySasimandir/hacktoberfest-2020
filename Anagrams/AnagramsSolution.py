def removeCommon(a,b):
    for x in a:
        if x in b:
            a.remove(x)
            b.remove(x)
    for x in b:
        if x in a:
            b.remove(x)
            a.remove(x)
    return a,b
def commonCheck(a,b):
    for x in a:
        if x in b:
            return True
    return False
def makeAnagram(a, b):
    a=sorted(list(a))
    b=sorted(list(b))
    while(commonCheck(a,b)):
        a,b=removeCommon(a,b)
    return len(a)+len(b)
for _ in range(int(input())):
    print(makeAnagram(input(),input()))
