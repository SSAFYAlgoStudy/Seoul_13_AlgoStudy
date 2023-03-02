import sys
input =sys.stdin.readline

N = int(input()) # 추의 개수
dp = [0] * 40001 # 추의 무게를 확인할 dp 배열
dp[0] = 1

chu_li = list(map(int,input().split())) #추의 무게
M = int(input()) # 확인할 추의 개수
check_li = list(map(int,input().split())) # 확인할 추의 무게

for i in chu_li:
    temp_li = set()
    for j in range(40001):
        if dp[j] == 1:
            if i+j<=40001:
                temp_li.add(i+j)
            if i-j>=0:
                temp_li.add(i-j)
            if j-i>=0:
                temp_li.add(j-i)
    
    # print(temp_li)
    for check in temp_li:
        dp[check] = 1


result = []
for i in check_li:
    if dp[i] == 1:
        result.append("Y")
    else:
        result.append("N")
print(" ".join(map(str,result)))