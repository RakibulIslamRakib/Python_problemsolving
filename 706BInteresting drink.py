from bisect import bisect_right
#bisect_right func have 2parameter. first one is the array and second one is a value. 
#This function return the location where the value should be insert while it is in shorted

n = int(input())
x = list(sorted(map(int, input().split())))
for _ in range(int(input())):
    print(bisect_right(x, int(input())))

