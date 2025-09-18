#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9046                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: goymkim <boj.kr/u/goymkim>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9046                           #+#        #+#      #+#     #
#    Solved: 2025/09/17 16:31:08 by goymkim       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
for _ in range(n):
    L = [i for i in input().replace(" ","")]
    D = dict()
    for s in L:
        D[s] = D.get(s,0) +1
    M = max(D.values())
    Can = [ch for ch, cnt in D.items() if cnt == M]
    if len(Can)>1:
        print("?")
    else:
        print(Can[0])
        
   
    