import collections
n=int(input())
l=map(int,input().split())
shoes = collections.Counter(l)
earn=int(0)
for i in range(int(input())):
    size,price = map(int,input().split())
    if shoes[size]:
        earn+=price
        shoes[size]-=1
print(earn)
