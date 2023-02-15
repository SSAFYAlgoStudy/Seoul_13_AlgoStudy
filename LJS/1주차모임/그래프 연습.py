import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)

# 루트노드에서 시작하면 우선 무조건 양이 있는곳으로 간다.  양 ++ 
# A섹션
# 양쪽 다 늑대면 바로 종료  
# 양이 있으면 계속 탐색하고,  양 ++  flag = 0
# 다음 노드에 늑대가 있어도 그 수를 합쳐도 양이 더 많으면 탐색한다.   늑대 ++  flag= 0

# 더이상 탐색할 수 없으면 반대편으로 간다.  flag ++ 
# A섹션 실행

# 더이상 탐색할 수 없으면 반대편으로 간다. flag ++
# 만약 더이상 탐색할 수 없는 행위가 2번 반복되면  flag >= 2 
# 더이상 양을 모을 수 없다.  break 
# 양의 값 출력 
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
N = len(info)
graph = [ [] for _ in range(N+1) ]
for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

print(graph[1][:-1])