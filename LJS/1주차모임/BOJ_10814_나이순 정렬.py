import sys
input= sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    age, name = map(str,input().rstrip().split())
    li.append((int(age),name))
li = sorted(li, key = lambda x:(x[0])) 
for i in li:
    print(*i)