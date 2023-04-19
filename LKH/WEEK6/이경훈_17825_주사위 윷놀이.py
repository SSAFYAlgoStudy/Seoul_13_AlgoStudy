import sys

input = sys.stdin.readline

# 시작부터 도착까지 각각 노드에 대해 다음 갈 수 있는 노드들을 구함
GRAPH = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12],
         [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23],
         [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]

# 임의의 노드에 대응되는 값
SCORE = [
  0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
  40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0
]

dice = list(map(int, input().split()))
answer = 0

# 완탐으로 모든 경우의 수 구하고 최대값 갱신
def backtracking(cnt, horse, sum_val):
  global answer
  if cnt == 10:
    answer = max(answer, sum_val)
    return

  # 4개의 말들에 대해 각각
  for i in range(4):
    x = horse[i]
    # 갈 수 있는 곳이 두곳이라면 무조건 1번 인덱스의 값으로 가야함
    if len(GRAPH[x]) == 2:
      nx = GRAPH[x][1]
    else:
      nx = GRAPH[x][0]
    
    # 이미 nx 자체가 갈 곳을 계산한 값이므로 dice[cnt]에서 1뺀 만큼만 더 가주면 됨
    for j in range(1, dice[cnt]):
      nx = GRAPH[nx][0]
      # 32는 끝이므로 더 갈 필요 없음
      if nx == 32:
        break
    # 만약 끝이거나 다른 말의 위치들과 다르다면
    if nx == 32 or nx not in horse:
      temp = horse[i]
      horse[i] = nx
      # dfs진행
      backtracking(cnt + 1, horse, sum_val + SCORE[nx])
      # 다른 말들 할때는 변경된 값을 원래대로 해줘야 함
      horse[i] = temp


backtracking(0, [0, 0, 0, 0], 0)
print(answer)