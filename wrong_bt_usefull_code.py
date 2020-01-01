from collections import OrderedDict
s = input()
unique_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst = []
for i in range(len(unique_string)):
    lst.append((s.count(unique_string[i]), unique_string[i]))
lst.sort(reverse=True)


a, b = lst[0]
c, d = lst[1]
e, f = lst[2]
pos1, pos2, pos3 = 0, 1, 2;
charlist = sorted([b, d, f])

if a == c and c == e:
    if charlist[0] == b and charlist[1] == f and charlist[2] == d:
        pos1 = 0; pos2 = 2; pos3 = 1
    elif charlist[0] == d and charlist[1] == b and charlist[2] == f:
        pos1 = 1; pos2 = 0; pos3 = 2
    elif charlist[0] == d and charlist[1] == f and charlist[2] == b:
        pos1 = 1; pos2 = 2; pos3 = 0
    elif charlist[0] == f and charlist[1] == d and charlist[2] == b:
        pos1 = 2; pos2 = 1; pos3 = 0
    elif charlist[0] == f and charlist[1] == b and charlist[2] == d:
        pos1 = 2; pos2 = 0; pos3 = 1

    x, y = lst[pos1]
    print(str(y)+' '+str(x))
    x, y = lst[pos2]
    print(str(y) + ' ' + str(x))
    x, y = lst[pos3]
    print(str(y) + ' ' + str(x))
    exit()

elif a == c and d < b:
    x = lst[0]
    lst[0] = lst[1]
    lst[1] = x
elif c == e and f < d:
    x = lst[1]
    lst[1] = lst[2]
    lst[2] = x

for a, b in lst[:3]:
    print(str(b)+' '+str(a))
