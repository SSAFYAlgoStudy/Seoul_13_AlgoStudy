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