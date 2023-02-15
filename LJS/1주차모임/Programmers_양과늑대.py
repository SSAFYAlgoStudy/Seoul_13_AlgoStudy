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

for index,i in enumerate(info):
    if i == 0:
        graph[index].append("sheep")
    else:
        graph[index].append("wolf")


def dfs(v):

    global sheep
    global wolf 
    global flag

    if graph[v][-1] == "sheep" and v not in sheep_check:
        
        sheep_check.append(v)
        sheep += 1
    if graph[v][-1] == "wolf" and v not in wolf_check:
        wolf_check.append(v)
        wolf += 1

    visited[v] = True
    for i in graph[v][:-1]:
        if not visited[i]:

            if graph[i][-1] == "wolf":  # 만약 다음 노드가 늑대인데 
                if sheep > wolf +1: #  그곳으로 가도 양이 더 많다면 가도 된다. 
                    flag = 0
                    visited[i] = True
                    dfs(i)
                else: #그렇지 않다면 되돌아가야한다.
                    flag += 1

                    if flag == 3: #만약 2번 돌았는데도 똑같이 반복하면 더이상 갈 곳이 없다.
                        exit()

                    return

            elif graph[i][-1] == "sheep": #양이면 그냥 가면 된다.
                flag = 0
                visited[i] = True
                dfs(i)



sheep_exit = info.count(0)
flag = 0 # 의미없는 반복이되면 종료
sheep = 0 # 양의 수
wolf = 0 #늑대의 수
sheep_check =[]
wolf_check  =[]

while True:
    
    visited = [False] * (N+1) # 방문이 안된상태로 순환
    dfs(0)

    if sheep == sheep_exit:
        print(sheep)
        break