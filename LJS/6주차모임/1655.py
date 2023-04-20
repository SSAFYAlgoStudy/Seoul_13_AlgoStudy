import sys
input= sys.stdin.readline
import heapq

N = int(input())
left_heap = [] ## 최대힙 왼쪽트리
right_heap = [] ## 최소힙 오른쪽트리

for _ in range(N):
    num = int(input())

    if len(left_heap) == len(right_heap): # 길이가 같으면 왼쪽에 넣어준다. 두 힙의 개수를 유지해서 중간값을 구할 수 있게
        heapq.heappush(left_heap,-num) # 최대 힙 정렬 - 처리리
    else:
        heapq.heappush(right_heap ,num)
        
    if len(left_heap)!= 0 and len(right_heap) !=0 and -(left_heap[0]) > right_heap[0]: # leftheap보다 작은 값이면 각각의 첫 값을 바꿔줘야 중간값이 유지된다.
        right = heapq.heappop(right_heap)
        left = heapq.heappop(left_heap)

        heapq.heappush(left_heap,-right)
        heapq.heappush(right_heap,-left)
        
    #left의 첫 원소가 중간값이 된다.
    print(-(left_heap[0]))
