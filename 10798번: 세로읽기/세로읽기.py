N =5
S =[]
for a in range(N):
    L = str(input())
    S.append(L)
M = max([len(i) for i in S])

t = []
for i in range(M):
    for n in range(5):
        try: 
            t.append(S[n][i])
            
        except:
            pass
R = [s for a in t for s in a]
R = ''.join(R).replace('-','')
print(R)