import sys
input= sys.stdin.readline


# 처음 값 들을 0을 추가함으로써 초기값 설정 pass

N , M , C = map(int,input().split())
li = [[0]*(C+1)] + [ [0] + list(map(int,input().split())) for _ in range(C)] # C만큼의 만족도 + 1 인덱스 처리
dp = [ [0]*(M+1) for _ in range(N+1) ]
li_a = [0] + list(map(int,input().split())) #인덱스 처리
li_b = [0] + list(map(int,input().split())) #인덱스 처리

for i in range(1,N+1):
    for j in range(1,M+1): # A의 i학생이 안하는 경우, B의 j학생이 안하는 경우, A의 i 과 B의 j학생이 악수하는 경우 3가지
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + li[li_a[i]][li_b[j]])

# print(li)
# print(dp)
print(dp[N][M])

