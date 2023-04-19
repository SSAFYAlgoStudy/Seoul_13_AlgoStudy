import sys
import heapq
input = sys.stdin.readline

# 우선순위큐 두개를 선언하고 두개의 큐안에 있는 원소의 개수의 차가 1을 넘지 않도록 넣어준다.
# 먼저 넣기 시작한 큐에는 최대값을 pop하게하고 다른 큐에는 최소값을 pop하게 한다.
# 외침을 반복하면서 왼쪽 큐의 최대값이 오른쪽 큐의 최소값보다 커진다면 swap한다.
# 매번 수행한 값을 ans 리스트에 넣어주고 출력한다.

mid = []

N = int(input())

left, right = [], []
ans = []

for i in range(N):
    temp = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-temp, temp))
    else:
        heapq.heappush(right, (temp, temp))

    if right and left[0][1] > right[0][1]:
        min = heapq.heappop(right)[1]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))

    ans.append(left[0][1])

for a in ans:
    print(a)