import sys
input= sys.stdin.readline

def subset(arr):
    T = len(arr)
    for i in range(1 << T):
        team_1, team_2 = [], []
        team_1_count, team_2_count = 0, 0
        for j in range(T):
            if i & (1 << j):
                team_1.append(arr[j])
                team_1_count += population[arr[j]]
        # 팀 1이 아닌 나머지 구간
        for k in range(1, N + 1):
            if k not in team_1:
                team_2.append(k)
                team_2_count += population[k]
        teams.append((team_1, team_2, abs(team_1_count - team_2_count)))


N = int(input())
population = [0] + list(map(int, input().split()))
nodes = [[]]
for _ in range(N):
    a = list(map(int, input().split()))
    b = a.pop(0)
    nodes.append(a)

teams = []
subset([i for i in range(1, N + 1)])
teams.sort(key=lambda x: x[2])  # 크기가 작은 순서대로 sorting 후
# print(teams)
for team_1, team_2, result in teams:
    # 연결이 제대로 되어있는지 확인하는 작업이 필요하다.
    final_stack_1 = []
    if len(team_1) == 1:
        pass
    else:
        if team_1:
            visited_1 = [0] * (N + 1)
            stack_1 = []
            stack_1.append(team_1[0])
            while stack_1:
                node = stack_1.pop()
                for h in nodes[node]:
                    if not visited_1[h] and h in team_1:
                        visited_1[h] = 1
                        stack_1.append(h)
                        final_stack_1.append(h)

        final_stack_1.sort()
        if final_stack_1 != team_1:  # 만약 안된다면 다음 방법으로 넘어간다.
            continue

    if len(team_2) == 1:
        print(result)
        exit()

    visited_2 = [0] * (N + 1)
    final_stack_2 = []
    stack_2 = []
    stack_2.append(team_2[0])

    while stack_2:
        node = stack_2.pop()
        for h in nodes[node]:
            if not visited_2[h] and h in team_2:
                visited_2[h] = 1
                stack_2.append(h)
                final_stack_2.append(h)
    final_stack_2.sort()
    if final_stack_2 == team_2:  # 만약 안된다면 다음 방법으로 넘어간다.
        print(result)
        exit()

print(-1)