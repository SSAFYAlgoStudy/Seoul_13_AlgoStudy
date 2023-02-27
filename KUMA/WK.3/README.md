# WK.3

# BOJ 14442 벽 부수고 이동하기2
* 339704KB 3512ms
- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가?
- [x] 시간복잡도를 계산 할 수 있는가?
- [x] 적절한 자료구조 활용하였는가?
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?

### 핵심 알고리즘 

* 처음 접근을 저번 주에 풀었던 벽 부수고 이동하기 문제랑 동일하게 했다.
* 다만 이번엔 한 번만 부수는 것이 아니라 K번까지 부술 수 있었기 때문에 visited배열에서 벽을 부순 횟수를 표시하는 부분을 0부터 K번까지 K+1 사이즈로 선언해줘야 했다.
* 테케가 잘 굴러가길래 1000 X 1000 X 10 도 역시 괜찮나? 하면서 제출하고 시간초과.
   
* 3차원이 아니면 벽을 부순 횟수를 표시할 방법이 마땅히 생각이 안 나서 질문게시판 들어가자마자 첫 글이 시간초과와 관련된 조언이었는데 파이썬이던 자바던 `다차원 배열 선언 시에 가장 큰 사이즈의 차원을 가장 오른쪽에 놓는 것이 메모리와 시간이 훨씬 덜 잡아먹는다`는 사실을 알았다.
* 파이썬 : https://eli.thegreenplace.net/2015/memory-layout-of-multi-dimensional-arrays
* 자바 : https://stackoverflow.com/questions/15339296/does-order-in-a-declaration-of-multidimensional-array-have-an-influence-on-used/15339442#15339442

* 이후 단순히 visited 배열 순서를 변경했다.
    ```python
    visited = [[[0]*(K+1) for _ in range(n)] for _ in range(m)]
    # 위에서 아래로
    visited = [[[0]*m for _ in range(n)] for _ in range(k+1)]
    ```

### comments
* 통과는 됐는데 시간이 3500에 메모리도 300메가 이상 먹었다.. 다른 방법이 있나?


# BOJ 2629 양팔저울
* 123864KB 144ms
- [x] N의 크기를 확인 하였는가?
- [x] 문제 제약사항을 확인 하였는가?
- [x] 시간복잡도를 계산 할 수 있는가?
- [x] 적절한 자료구조 활용하였는가?
- [x] 핵심 알고리즘을 구현할 수 있는가?
- [x] 문제를 풀었는가?

### 핵심 알고리즘
* 추를 하나씩 입력받으면서 2차원 boolean형 dp에 차례로 입력하고 가능한 조합(+, -)을 갱신해준다.
* dp는 해당 인덱스의 무게를 측정가능하면 True, 불가능하면 False
```python
dp = [[False]*(40001) for _ in range(n)]

# 첫번째 추 입력과 i번째 추의 무게 자체를 입력해주는 부분
dp[0][weights[0]] = True
for i in range(1, n):
    dp[i][weights[i]] = True
    # 가능한 조합(기존 가능한 무게와 새로운 추의 무게를 + 혹은 -)
    for j in range(1, len(dp[i-1])):
    if dp[i-1][j] == True:
        dp[i][j] = True;
        if j-weights[i] > 0:
            dp[i][j-weights[i]] = True
        if weights[i]-j > 0:
            dp[i][weights[i]-j] = True
        if j+weights[i] < len(dp[i]):
            dp[i][j+weights[i]] = True
```

* 입력 받은 구슬들의 무게를 dp 마지막 행에서 탐색해주고 결과를 출력
```python
for x in beads:
    if dp[-1][x] == True:
        print("Y ", end='')
    else:
        print("N ", end='')
```

### comments
* 비슷한 추 계열 문제들이 전부 추를 무제한 쓸 수 있다거나 합만 있어서 dp로 풀어야 할것 같은데 그 dp가 비슷한 문제들이 1차원 배열을 사용해서 그쪽으로 가닥을 잡았다.
* 쉬는 시간에 가만히 생각해보니 빼기가 더해져서 일반적인 dp문제처럼 한 방향으로 채워져 나가는 것이 아니라 뺀 조합을 다시 더하는 등 `전의 상태와 새로운 추를 조합한 결과를 저장할 공간이 새로 필요`했다. 
* 근데 40000 X 30 X 4의 dp 배열이 메모리나 시간을 초과시킬거라고 생각했다. 
* 그래서 1차원 배열로 해봤는데 2번 테케에서 새로운 추를 입력 받을 때 입력 받을 추에서 기존의 추의 무게를 뺄 수 없단걸 깨닫고(위에서 언급한 새로운 공간이 없다면 추를 중복으로 사용하게 됨)우석이 말 듣고 띵했던게 자바에선 당연하게 visited배열 같은걸 boolean형으로 선언하면서 파이썬에서 그냥 0, 1로 int형으로 하고 있던 걸 깨달았다.
* boolean형으로 dp 뜯어고치고 메모리 아슬아슬하게 세이프
