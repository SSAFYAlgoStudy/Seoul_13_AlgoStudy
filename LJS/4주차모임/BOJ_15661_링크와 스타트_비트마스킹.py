import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
for i in range(1, (1<<N)-1):

    team1 = []
    team2 = []

    team1_score = 0
    team2_score = 0

    for j in range(N):
        if (i&1<<j)==0:
            team1.append(j)
        else:
            team2.append(j)

    for k in team1:
        for t in team1:
            team1_score += graph[k][t]
    
    for k in team2:
        for t in team2:
            team2_score += graph[k][t]
    
    result = min(abs(team1_score-team2_score),result)

print(result)