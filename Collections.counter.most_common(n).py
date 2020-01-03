from collections import Counter
s = sorted(input())
lst = Counter(s).most_common(3)
for a,b in lst:
    print('{} {}'.format(a,b))
#it returns the most n element  pair (aharracter, count(charracter))    
