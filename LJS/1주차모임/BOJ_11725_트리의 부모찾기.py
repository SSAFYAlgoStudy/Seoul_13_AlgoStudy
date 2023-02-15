import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = v
            

N = int(input())
graph = [ [] for _ in range( N+1 ) ]

for _ in range(N-1):
    a, b= map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)

visited= [False] * (N+1)
dfs(1)
for i in range(2,N+1):
    print(visited[i])