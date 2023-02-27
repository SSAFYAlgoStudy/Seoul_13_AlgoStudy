import sys
input = sys.stdin.readline
from collections import deque


def bfs() :
    
    q.append([0,0,K]) 
    visited[0][0][K] = 1 

    while q :
        x,y,flag = q.popleft()   # xpos ,  ypos, 결과값
        if (x==N-1 and y==M-1):
            return visited[x][y][flag]
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M :  # 맵밖으로 나가지 않으면 

                if flag > 0 and graph[nx][ny]==1 and visited[nx][ny][flag-1]==0:
                    visited[nx][ny][flag-1] = visited[x][y][flag]+1
                    q.append([nx,ny,flag-1])

                elif graph[nx][ny]==0 and visited[nx][ny][flag]==0:  # 벽이 아니면서, 새로 방문하는 곳이면
                    visited[nx][ny][flag] = visited[x][y][flag]+1  # 거리를 1 증가시키며 q에 저장한다.
                    q.append([nx,ny,flag]) 
    return -1

N, M , K= map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]  # 3차원 배열 result_cnt 생성 flag를 저장하기위해 만들어주고
q = deque([])
dx = [-1,1,0,0]
dy=[0,0,-1,1]

print(bfs())