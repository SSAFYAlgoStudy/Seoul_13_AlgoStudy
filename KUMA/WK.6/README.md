# WK.6

# 캠프준비
* 115436KB 164ms

## 핵심 아이디어
* 원래 백트래킹 연습하고 싶어서 백트래킹 주제 문제들에서 제목만 보고 뽑은 문제였는데 의도한 백트래킹이랑 완전 다른 스타일의 문제였다..
* 심지어 문제 읽어보니 그냥 부분조합 구하고 가지치기 일찌감치 해주면 그게 와따일거 같아서 그렇게 풀었다.
* 너무 쉬워서 더 쓸말이 없다. 다음부턴 문제 제대로 골라야지
```python
# X <= max - min
N, L, R, X = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for subset in range(1 << N):
    res = []
    score = []
    scoreSum = 0
    gap = 0
    for i in range(N):
        if subset & (1 << i):
            res.append(i)
    for x in res:
        scoreSum += num[x]
        score.append(num[x])

    if not L <= scoreSum <= R:
        continue

    if max(score) - min(score) >= X:
        cnt += 1

print(cnt)
```

# 가운데를 말해요
* 131384KB 412ms

## 핵심 아이디어
* 예전에 풀어봤던 문제였다. 그 때 힙 한 개로 개고생을 해서 힙을 두개 써서 중간 값을 탐색하는 방식의 아이디어가 필요한게 바로 떠올랐다.
```python
# 왼쪽은 최대힙, 오른쪽은 최소힙
for i in range(n):
    num=int(input())

    # 크기가 같을 때 왼쪽에 삽입
    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap, -num)
    # 아니면 오른쪽에 삽입
    else:
        heapq.heappush(rightHeap, num)
    # 왼쪽의 최대값과 오른쪽의 최소값을 비교하고 값을 교체해줘야 하면 교체해준다
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftMax=heapq.heappop(leftHeap)
        rightMin=heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightMin)
        heapq.heappush(rightHeap, -leftMax)

    # 왼쪽의 최대값이 중간값 중 더 작은 값이 보장됐으니 출력
    print(-leftHeap[0])
```

# 미팅
* 130964KB 192ms

## 핵심 아이디어
* 처음에는 예전 다리설치 문제같이 풀어보려고 했는데 last index를 따로 저장해야하고 너무 조건이 많이 붙어서 포기했다
* 그다음엔 2차원 dp로 해보려고 했는데 이 문제는 특이하게 dp의 index를 줄 요소는 명확한데 주어진 정보인 성격이 어떻게 활용하는지 생각을 많이 해야 했다.
* A대학의 i번째 학생 Ai, B대학의 j번째 학생Bj가 악수할 때 만족도를 따로 배열을 만들어서 저장해주고 그 값을 dp작성에 이용했다.
```python
# A대학 학생 i번째, B대학 학생 j번째까지 선택했을 때 기준으로 dp작성
dp = [[0]*(M+1) for _ in range(N+1)]
satisfy = [[0]*M for _ in range(N)]

# Ai와 Bj가 만났을 때 만족도
for i in range(N):
    for j in range(M):
        satisfy[i][j] = char[A[i]][B[j]]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j-1] + satisfy[i-1][j-1], dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
```

# 프로그래머스 - sql
* 왜 틀리지 생각하다가 옆자리 수정이가 order by 빼먹었다고 말해줘서 알았다..
* 데이터를 못보니까 뭔가 막막하다, 처음부터 문제 잘 읽어야겠다.
```sql
SELECT USER_ID, NICKNAME, sum(price) as TOTAL_SALES
from used_goods_board join used_goods_user
on used_goods_board.writer_id = used_goods_user.user_id
where status='DONE'
group by writer_id
having sum(price) >= 700000
order by TOTAL_SALES;
```