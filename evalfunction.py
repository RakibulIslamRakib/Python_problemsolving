n=int(input())
lst=set(map(int,input().split()))
for i in range(int(input())):
    s = input()
    eval('lst.{0}({1})'.format(*s.split()+['']))
print(sum(lst))
