# WK.5

# Gaaaaaaaaaarden
* 131252KB 2036ms

## 핵심 아이디어
### 조합 구하는 부분
* 스터디때 말했던 것처럼 조건을 세개로 해서 부분집합을 구하고 기저조건에서 한 번 더 G, R 값을 모두 만족하는 지 필터링을 해줬음
* 이후 기저조건에서 BFS 호출
    ```python
    def subset(cnt, g, r):
        global res
        if cnt == size:
            if g == G and r == R:
                dq = deque()
                for i in range(size):
                    if select[i] != 'N':
                        dq.append((cand[i][0], cand[i][1], select[i]))
                res = max(res, bfs(dq))
            return
        else:
            if g < G:
                select.append('G')
                subset(cnt + 1, g + 1, r)
                select.pop()

            if r < R:
                select.append('R')
                subset(cnt + 1, g, r + 1)
                select.pop()

            select.append('N')
            subset(cnt + 1, g, r)
            select.pop()
    ```


### BFS 부분
* 이것도 오기가 생겨서 스터디때 말했던 것처럼 구해진 조합을 덱에 넣고 `모든 배양액이 뿌려진 부분이 같은 레벨에서 진행되게 BFS로 짰음`
* visited 배열에 초록 배양액이 뿌려진 경우 1을, 빨간 배양액이 뿌려진 경우는 -1을 초기값으로 넣어주고 이후 사방 탐색이 진행될 때 각각 전의 값에서 1을 더해주거나 빼주는 식으로 진행한다
* `다음 방문할 지점의 visited값`과 `현재 지점의 visited값 + 1`의 절대값이 같다면 꽃이 피는 것으로 설정
    ```python
    if (board[nx][ny] == 1 or board[nx][ny] == 2) and visited[nx][ny] != INF and visited[nx][ny] == 0 :
        if c == 'G':
            visited[nx][ny] = visited[cx][cy] + 1
            dq.append((nx, ny, c))
        elif c == 'R':
            visited[nx][ny] = visited[cx][cy] - 1
            dq.append((nx, ny, c))
    elif visited[nx][ny] * visited[cx][cy] < 0 and abs(visited[nx][ny]) == abs(visited[cx][cy]) + 1:
        visited[nx][ny] = INF
        cnt += 1
    ```

