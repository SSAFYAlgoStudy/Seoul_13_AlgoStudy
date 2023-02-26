## BOJ 나이순 정렬

- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가?
- [x] 시간복잡도를 계산 할 수 있는가?
- [x] 적절한 자료구조 활용하였는가?
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?

  - 핵심 IDEA
    - 리스트에 입력값들을 넣고 정렬해서 출력

-------------------------------------------------------------------------------

## BOJ 하노이 탑

- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가?
- [x] 시간복잡도를 계산 할 수 있는가?
- [x] 적절한 자료구조 활용하였는가?
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?
- 
  - 핵심 IDEA
    - 재귀함수를 이용함
    - n개의 탑을 이동시켜야 하는데 _from에서 temp를 보조로 이용해서 to로 옮김
  
-------------------------------------------------------------------------------

## 링크와 스타트

- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가? 
- [x] 시간복잡도를 계산 할 수 있는가? 
- [x] 적절한 자료구조 활용하였는가? 
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?
- 
  - 핵심 IDEA
    - N명을 을 두 팀으로 나누되, 각각의 팀은 한명 이상이어야 하므로 i명만큼 뽑아서 한 팀을 만들고 나머지 N-i명으로 한 팀을 만든다.
    - 이때, i는 N의 절반보다 1 클때까지만 한다. 절반을 넘게 되면 중복된 결과를 구하는 셈이다. 
      ex) 5개 팀을 2개 팀, 3개팀으로 나누는 것과 3개 팀, 2개 팀으로 나누는 것의 결과는 같다.

## 트리의 부모 찾기

- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가? 
- [x] 시간복잡도를 계산 할 수 있는가? 
- [x] 적절한 자료구조 활용하였는가? 
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?
- 
  - 핵심 IDEA
    - 인접리스트를 활용하여 bfs를 진행한다.

## 양과 늑대

- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가? 
- [x] 시간복잡도를 계산 할 수 있는가? 
- [x] 적절한 자료구조 활용하였는가? 
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?
- 
  - 핵심 IDEA
    - 인접리스트를 활용하여 dfs를 진행하되, 인자로 현 상태에서 방문할 수 있는 세트를 항상 받는다.