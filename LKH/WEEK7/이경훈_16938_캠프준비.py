import sys

input = sys.stdin.readline

N, L, R, X = map(int, input().split())

quest = list(map(int, input().split()))
quest.sort()
cnt = 0

# 부분집합을 비트마스킹으로 구현
for i in range(1, 1 << N):
    sum = 0
    check = []
    # 각 비트를 확인해서
    for j in range(0, N):
	  # 만약 고르지 않은 문제라면 continue
        if (i & 1 << j) == 0:
            continue
        # 고른 문제를 check 리스트에 넣어주고
        check.append(j)
	  # 난이도를 더해줌
        sum += quest[j]
    # 난이도 조건
    if sum > R:
        continue

    if sum < L:
        continue
    # 가장 어려운 문제와 쉬운 문제의 난이도 차이
    if quest[check[-1]] - quest[check[0]] < X:
        continue
    cnt += 1
print(cnt)