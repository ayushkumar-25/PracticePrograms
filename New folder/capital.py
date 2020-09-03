import functools as f
i = [1,2,3,4,5]
l = [int(input())for _ in range(int(input()))]
n = (f.reduce(lambda x,y:x+y,l))
print(l)
print(list(n,1,2))
