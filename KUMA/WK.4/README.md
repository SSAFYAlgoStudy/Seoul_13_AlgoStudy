# WK.4

# 링크와 스타트 (비트마스킹)
* 115416KB 1788ms -> 기존 3000ms 남짓

### 핵심 알고리즘
* 원래의 부분집합을 구하는 과정을 비트마스킹을 통해 진행했다.
* 비트가 마스킹 되어 있으면 teamA에, 안 되어 있으면 teamB에 넣었다. 공집합을 제외하려고 범위의 처음과 끝의 사이즈를 1씩 줄여주었다.
    ```python
    for subset in range(1, (1 << n) - 1):
        teamA = []
        teamB = []
        for i in range(n):
            if subset & (1 << i):
                teamA.append(i)
            else:
                teamB.append(i)
    ```
### comments

* `[0] [1, 2, 3, 4]` 와 `[1, 2, 3, 4] [0]` 의 경우를 두번 처리하는 걸 어떻게 해야될 지는 모르겠다. 이번 주 다른 문제인 게리 맨더링도 마찬가지
* 점수를 산출 하는 부분은 그냥 완탐해서 팀원 목록에서 점수를 모두 더해주고 각 값이 두번씩 더해지므로 반으로 나눠주고 출력했다. 이 부분도 좀 더 세련되게 할 수 있나..?   



# 게리 맨더링 (비트마스킹)
* 116864KB 192ms

### 핵심 알고리즘
* 이 문제도 마찬가지로 공집합을 제외한 부분집합을 구했다.
    ```python
    for subset in range(1, (1 << N) - 1):
        ter1 = []
        ter2 = []

        for i in range(N):
            if subset & (1 << i):
                ter1.append(i);
            else:
                ter2.append(i);
    ```
* 하지만 골드답게 이후 인접 여부를 추려내야 하는 과정이 더해졌는데 이 부분은 BFS로 구현했다.
    ```python
    def checkAdj(point, ter):
        dq = deque()
        dq.append(point)
        visited[point] = True

        while(dq):
            cur = dq.pop()

            for i in adjList[cur]:
                if i in ter and not visited[i]:
                    dq.append(i)
                    visited[i] = True
    ```

### comments
* 위의 두 알고리즘을 적절하게 사용하는 과정에서 코드가 아름답지 못하다. 좀 더 세련되게 짤 방법이 있을까?   


# 번외: 벌꿀 채취 (비트마스킹)
* 27,600kb 156ms

### 핵심 알고리즘
* 조합을 통해 M만큼 사이즈를 재기 시작할 좌표를 고르는 과정이 행과 열 각각 NC2, N-M+1C1 었다.
    ```java
    public static void combination(int cnt, int start) {
        if (cnt == 2) {
            for (int i = 0; i < N - M + 1; i++) {
                for (int j = 0; j < N - M + 1; j++) {
                    int sum = getHoney(selected[0], i) + getHoney(selected[1], j);
                    maxProfit = Math.max(maxProfit, sum);
                }
            }
            return;
        }
        for (int i = start; i < N; i++) {
            selected[cnt] = i;
            combination(cnt + 1, i + 1);
        }
    }
    ```
* 이후 정해진 좌표에서 가로로 M만큼 사이즈를 지정해서 그 `사이즈 내에서 부분조합을 통해 채취할 벌꿀통을 정해야 하는데 이 때 비트마스킹을 사용`했기 때문에 리드미에 추가해 보았다.
    ```java
    public static int getHoney(int x, int y) {
            ArrayList<Integer> cand = new ArrayList<>();
            int max = 0;
    
            for (int i = y; i < y + M; i++) {
                cand.add(map[x][i]);
            }
    
            // 현재 지점 기준 주어진 범위 M 내에서 가장 많은 꿀을 채취 하는 경우를 따져본다.
            for (int subset = 0; subset < (1 << M); subset++) {
                ArrayList<Integer> select = new ArrayList<>();
                int sum = 0;
                int profit = 0;
    
                for (int i = 0; i < M; i++) {
                    if ((subset & (1 << i)) != 0) {
                        int cur = cand.get(i);
                        sum += cur;
                        profit += (int) Math.pow(cur, 2);
    
                        if(sum > C) profit = 0;
                    }
                }
                max = Math.max(max, profit);
            }
            return max;
        }
    ```