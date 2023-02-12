n = int(input())
a = [list(map(int,input().split())) for _ in range(n)] # 팀의 능력치
res = [] #결과값들을 담는 배열

def getTeamScore(team):
    score = 0
    for e1 in team:
        for e2 in team:
            score+=a[e1][e2]
    return score

# 팀 나누기
for s in range(1,(1<<n) - 1): #최소 한명 이상이어야 하므로
    team1,team2 = [],[]
    #team1 ,team2 나누기
    for i in range(n):
        if s & 1<<i :team1.append(i)
        else:team2.append(i)

    #team1 team2 에 속한 팀점수의 합구하기
    team1Score , team2Score = getTeamScore(team1),getTeamScore(team2)
    res.append(abs(team1Score-team2Score))

#최소값 출력
print(min(res))
