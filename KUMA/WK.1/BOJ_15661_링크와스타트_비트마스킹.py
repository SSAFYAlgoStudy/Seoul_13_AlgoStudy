import sys
input = sys.stdin.readline

n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]
visited = 0b00000000
base = 0b00000001
minGap = 2147000000

# 두 팀 능력치 합 차이 계산
def score():
    global minGap
    start = 0
    link = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if visited & (base << i) and visited & (base << j):
                start += status[i][j] + status[j][i]
            elif not visited & (base << i) and not visited & (base << j):
                link += status[i][j] + status[j][i]
    gap = abs(start - link)
    minGap = min(gap, minGap)

def teaming(cnt):
    global visited
    # 기저 조건 도달 시
    if cnt == n:
        score()
        return
    visited = visited | (base << cnt)
    teaming(cnt + 1)
    visited = visited ^ (base << cnt)
    teaming(cnt + 1)

teaming(0)

print(minGap)