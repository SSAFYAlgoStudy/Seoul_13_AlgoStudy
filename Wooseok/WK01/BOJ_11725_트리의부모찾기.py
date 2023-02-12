import sys
sys.setrecursionlimit(10**5)
n = int(input())
parent = [i for i in range(n+1)] #p[i] : i번 노드의 부모노드
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(node):
    visited[node] = True

    for child in graph[node]:
        if visited[child]:continue
        parent[child] = node
        dfs(child)

for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
for c in parent[2:]:
    print(c)