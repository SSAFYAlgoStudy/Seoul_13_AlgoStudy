import sys
input =sys.stdin.readline
import itertools
N , L , R, X = map(int,input().split()) ##  문제개수, L<=합M=R , 가장어려운문제 ,가장쉬운문제 난이도차이
li = list(map(int,input().split())) ## 문제의 난이도
li.sort()
result = 0

for i in range(2,N+1):
    for comb in itertools.combinations(li,i):
        if L<=sum(comb)<=R and (max(comb)-min(comb))>=X:
            result += 1
print(result)