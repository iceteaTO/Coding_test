#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10798                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: goymkim <boj.kr/u/goymkim>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10798                          #+#        #+#      #+#     #
#    Solved: 2025/09/18 10:08:07 by goymkim       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
# line = sys.stdin.readline()
# line = intpu(
N =5
# S = [list(input().split()) for _ in range(N)]
S =[]
for a in range(N):
    L = str(input())
    S.append(L)
M = max([len(i) for i in S])

t = []
for i in range(M):
    # l = []
    for n in range(5):
        try: 
            t.append(S[n][i])
            
        except:
            pass
    # t.append(l)
R = [s for a in t for s in a]
R = ''.join(R).replace('-','')
print(R)