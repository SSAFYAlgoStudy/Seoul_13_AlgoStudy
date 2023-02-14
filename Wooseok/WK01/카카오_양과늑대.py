def solution(info, edges):
    res = [] #결과값담을 배열
    n = len(info)
    visited = [False]*(1 << n) #상태공간 정의 비트마스킹
    graph = [[] for _ in range(n)] #2진트리
    for parent,child in edges:
        graph[parent].append(child)

    def solve(state): #모든 서브 그래프 구하는 함수 , state = 모든 서브그래프를 표현한 비트마스크

        if visited[state]:return
        visited[state] = True
        sheep ,wolf = 0,0
        #현재 상태에서 양,늑대 개수 구하기
        for i in range(n):
            if state & 1 << i:
                if info[i] == 0 : sheep+=1
                else : wolf +=1

        if wolf >= sheep : return #기저조건

        res.append(sheep)

        #현재 선택된 노드에 대해서 자식 노드에 대해 재귀 호출하여 모든 subgraph들 구할 수 있음.
        for i in range(n):
            if state & 1 << i:
                for c in graph[i]:

                    nextState = state | 1 << c
                    solve(nextState)

    solve(1)

    answer = max(res)
    return answer
