import sys
input= sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**7)

N , M = map(int,input().split())

graph = [ [] for _ in range(N) ]
dx = [-1,1,0,0]
dy=[0,0,-1,1]

q = deque([])
q.append([0,0,0])
result_cnt = [[ [0] * 2 for _ in range(M) ] for _ in range(N) ]  # 3차원 배열 result_cnt 생성 flag를 저장하기위해 만들어주고
result_cnt[0][0][0] = 1 #시작할 때 1 

for i in range(N):
    graph[i] = (list(map(int,input().rstrip())))

def bfs():

    while q:
        x , y , flag = q.popleft()  # xpos ,  ypos, 결과값

        if (x==N-1 and y==M-1):
            return result_cnt[x][y][flag]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<=-1 or nx >= N or ny <= -1 or ny>=M: # 맵밖으로 나가면 
                continue
            
            if graph[nx][ny] == 1 and flag == 0:  # 벽에 막혀있는데 아직 안부쉈으면
                result_cnt[nx][ny][1] += (result_cnt[x][y][0]+1) # 이전 결과값에서 1 증가시켜주고
                q.append([nx,ny,1])

            # if graph[nx][ny] == 1 and flag != 0: # 벽에 막혀있으며 부쉈으면 
            #     continue

            if graph[nx][ny] == 0 and result_cnt[nx][ny][flag] == 0: # 벽이 아니면서, 새로 방문하는 곳이면
                result_cnt[nx][ny][flag] = result_cnt[x][y][flag] + 1 # 거리를 1 증가시키며 q에 저장한다.
                q.append([nx,ny,flag])

    return -1  # 못돌면 -1출력한다.


print(bfs())