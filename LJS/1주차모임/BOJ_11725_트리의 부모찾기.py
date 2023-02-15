import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(v): # visited index에 탐색을 시작한 부모노드를 저장
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = v
            

N = int(input())
graph = [ [] for _ in range( N+1 ) ]

for _ in range(N-1): #그래프에 정보를 집어 넣는다.
    a, b= map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)

visited= [False] * (N+1) #방문을 처리할 예정
dfs(1) # 루트 노드는 1로 정해져있다.

for i in range(2,N+1): #visited에 저장된 번호가 부모 노드이다.
    print(visited[i])