n=int(input())
arr=[]
for i in range(1,n+1):
    arr.append(" "*(n-i)+"+"*(2*i-1)+" "*(n-i))
for i in range(n-1,0,-1):
    arr.append(" "*(n-i)+"+"*(2*i-1)+" "*(n-i))
for i in arr:
    print(*i)
