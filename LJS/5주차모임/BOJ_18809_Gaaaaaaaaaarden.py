import sys
input = sys.stdin.readline
import itertools
from itertools import combinations
from collections import deque

def is_okay(x,y,map): # bfs가 실행 가능한지 여부
    if x<=-1 or x>=N or y<=-1 or y>=M: # 벗어나면
        return False
    if visited[x][y] !=0: #방문한적 있으면
        return False
    if visited[x][y] == sys.maxsize: #꽃이면
        return False
    if map[x][y] !=1 and map[x][y] !=2: # 갈수있는 땅이 아니면 false
        return False
    return True

def BFS(green_map, red_map, map):
    q = deque([])
    cnt = 0

    for green in green_map: # 음수로 표시하고
        q.append((green[0], green[1], 'green'))
        visited[green[0]][green[1]] = -1
    for red in red_map: # 양수로 표시해서 추후에 더해서 그 값이 같거나 , abs 처리를 해서 같을때 꽃으로 처리하면 될듯?
        q.append((red[0], red[1], 'red'))
        visited[red[0]][red[1]] = 1

    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]
        color = now[2]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_okay(nx,ny,map):
                if visited[x][y] < 0: #초록색이 퍼지고 있는 곳이면 -1 해서 기록한다.
                    visited[nx][ny] = visited[x][y] - 1
                    q.append((nx, ny, color))
                elif 0<visited[x][y]<sys.maxsize: #빨간색
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, color))

            if  0 <= nx < N and 0 <= ny < M and map[nx][ny] != 0 and (abs(visited[nx][ny]+visited[x][y])-1) == 0: # 만약 범위안에 들어가고, 호수가 아니면서, 이 전의 꽃이 피는 시간
                # 에서 1만큼 증가한 값이 현재고, 그 절대값을 취한 값이 0이면 시간이 같다는 뜻
                visited[nx][ny] = sys.maxsize #꽃이 피고
                cnt += 1 #꽃의 개수 증가
    return cnt

N, M, G, R = map(int, input().split())  # 행, 열, 초록, 빨강
# 0은 호수 1은 배양x땅 2는 배양o땅
graph = [[0] *M for _ in range(N)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]
ground = []

for i in range(N):
    li = list(map(int,input().split()))
    for j in range(M):
        graph[i][j] = li[j]
        if graph[i][j] == 2:
            ground.append((i,j)) # 배양액이 들어갈 수 있는 지점

ground_set = set(ground) #set 형태로 바꿔서 차집합 사용
max_result = 0

for green in combinations(ground, G): #combination으로 g개만큼의 green땅을 뽑고
    noGreen_ground = list(ground_set - set(green)) # 빨강을 뽑을 ground를 차집합으로 구한다.
    g_ground = list(green)

    for red in combinations(noGreen_ground, R): # 초록이 빼진 땅에서 red를 combination 찾는다.
        visited = [[0] * M for _ in range(N)]
        r_ground = list(red)
        result = BFS(g_ground, r_ground, graph)
        max_result = max(result,max_result)

print(max_result)