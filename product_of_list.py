import itertools
l=map(int,input().split())
x=map(int,input().split())
lst = list(itertools.product(l,x))
print(*lst)
