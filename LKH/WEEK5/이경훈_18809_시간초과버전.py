import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def chooseGround(cnt, idx, green, red, grounds):
  if green > G:
    return
  if red > R:
    return
  if (G-green) + (R-red) > len(grounds) - idx:
    return
  if cnt == R + G:
    # print(chosen_ground)
    bfs(chosen_ground)
    return

  if idx > len(grounds) - 1:
    return

  chosen_ground.append((grounds[idx], 0))
  chooseGround(cnt + 1, idx + 1, green + 1, red, grounds)
  chosen_ground.pop(-1)
  chosen_ground.append((grounds[idx], 1))
  chooseGround(cnt + 1, idx + 1, green, red + 1, grounds)
  chosen_ground.pop(-1)
  chooseGround(cnt, idx + 1, green, red, grounds)


def bfs(chosen_ground):
  global ans
  _ans = 0
  visited = [[0 for _ in range(M)] for _ in range(N)]
  q = deque()
  q.extend(chosen_ground)
  # print(q)

  for (x, y), _ in q:
    visited[x][y] = 1

  while (q):
    level = len(q)
    candi_set = set()
    candi_list = []
    # print(q)
    while (level > 0):
      level -= 1
      (x, y), c = q.popleft()
      # print('(x, y)', (x, y))
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if inside(nx, ny) and garden[nx][ny] != 0 and visited[nx][ny] == 0:
          candi_set.add(((nx, ny), c))
    candi_list = list(candi_set)
    candi_list.sort()

    i = 0
    # print('삭제전', candi_list)
    while (i < len(candi_list) - 1):
      if candi_list[i][0] == candi_list[i + 1][0]:
        _ans += 1
        (nx, ny), _ = candi_list[i]
        visited[nx][ny] = 1
        candi_list.pop(i)
        candi_list.pop(i)
      else:
        i += 1
    # print('삭제후', candi_list)

    q.extend(candi_list)
    for (nx, ny), c in candi_list:
      visited[nx][ny] = 1
  # print(_ans)

  ans = max(ans, _ans)


def inside(nx, ny):
  if -1 < nx < N and -1 < ny < M:
    return True
  else:
    return False


N, M, G, R = map(int, input().split())
garden = []
grounds = []
ans = 0

chosen_ground = []

for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(M):
    if temp[j] == 2:
      grounds.append((i, j))
  garden.append(temp)

chooseGround(0, 0, 0, 0, grounds)
print(ans)
