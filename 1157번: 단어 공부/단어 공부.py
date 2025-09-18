L= list(str(input()))
L = ''.join(L).upper()
D = dict()
for a in L:
    D[a] = D.get(a,0)+1

M = max(list(D.values()))
i = 0
A = []
for k,v in D.items():
    if v == M:
        i+=1
        A.append(k)
    else:
        pass
    
if i>1:
    print('?')
else:
    print(A[0])