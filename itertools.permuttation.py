#from itertools import permutations
 #print permutations(['1','2','3'])
#itertools.permutations object at 0x02A45210>
#print list(permutations(['1','2','3']))
#[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
#print list(permutations(['1','2','3'],2))
#[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
#print list(permutations('abc',3))
#[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


#EX: 
from itertools import permutations
S,n=input().split()
S,n = sorted(S),int(n)
l = list(permutations(S,n))
for i in l:
    print(''.join(i))
  
#input:  HACK 2
#output:
#AC
#AH
#AK
#CA
#CH
#CK
#HA
#HC
#HK
#KA
#KC
#KH
