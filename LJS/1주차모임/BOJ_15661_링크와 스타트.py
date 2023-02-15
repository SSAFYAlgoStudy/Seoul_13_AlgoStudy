import sys
input = sys.stdin.readline

import itertools
from itertools import combinations

	 
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]

row_li = [ 0 for _ in range(N)] #가로의 합 모두 저장
col_li = [ 0 for _ in range(N)] #세로의 합 모두 저장
sum_li = [ 0 for _ in range(N)] #전체의 합 저장

for index,i in enumerate(li): #예전에 numpy 써서 합을 구했던것같은데.. 비효율적이긴 한듯
    row_li[index] = sum(i)
    for index2,j in enumerate(i):
        col_li[index2] += j

    
for i in range(N):
    sum_li[i] = row_li[i] + col_li[i]

sumofsum = sum(sum_li)//2 # 중심을 잡을 값.  차이를 최소로 해야 하기 때문에 중간값을 설정한다.  ex) 100일경우 50이면  49,51.. 48,52 등으로 최소에 가깝게 세팅할수있다.
answer = 21000  #  20 * 20 * 100 // 2를 해도 20000이기때문에 21000이면 넉넉함

for i in range(1, N//2+1): 
    com_li = list(itertools.combinations((sum_li),i))  # sum_li로 가능한 조합들을 뽑아내서 
    for com_sum in com_li:
        answer= min(answer, abs(sumofsum-sum(com_sum))) # 최소값이 갱신되면 갱신한다.
        if answer == 0: # 차이가 0이 나오면 더 계산할필요없다.
            break
    if answer==0:
        break

print(answer)