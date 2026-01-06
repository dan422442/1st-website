from math import log10
from sys import exit
def p(n,s):
    return n*((s-2)*n-(s-4))//2

u=[]
for s in range(3,9):
    for n in range(1,200):
        if int(log10(p(n,s)))==3:
            u.append((s,n,p(n,s)))
for n1 in u:
    l=[n1]
    for n2 in [_ for _ in u if _[0] not in [_[0] for _ in l] and _[2]//100==l[-1][2]%100]:
        l.append(n2)
        for n3 in [_ for _ in u if _[0] not in [_[0] for _ in l] and (_[2]//100)==(l[-1][2]%100)]:
            l.append(n3)
            for n4 in [_ for _ in u if _[0] not in [_[0] for _ in l] and (_[2]//100)==(l[-1][2]%100)]:
                l.append(n4)
                for n5 in [_ for _ in u if _[0] not in [_[0] for _ in l] and (_[2]//100)==(l[-1][2]%100)]:
                    l.append(n5)
                    for n6 in [_ for _ in u if _[0] not in [_[0] for _ in l] and (_[2]//100)==(l[-1][2]%100)]:
                        l.append(n6)
                        if n6[2]%100==n1[2]//100:
                            print(sum([_[2] for _ in l]))
                            exit()
                        l.pop()
                    l.pop()
                l.pop()
            l.pop()
        l.pop()