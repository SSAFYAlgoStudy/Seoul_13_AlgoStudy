

<br><br><br>
### <span style="color:violet"> 1. G2 가운데를 말해요

  - <span style="color:SKYBLUE"> 접근방법 
     - 최대 10만개의 데이터를 계속 삽입하고 비교해야 하는데, 시간제한이 0.1초라 평범한 풀이는 되지 않을거라 생각했다.<BR>
  원하는 값은 딱 하나고, 최대힙과 최소힙을 나눠서 각각 데이터를 넣어주면, 그 가운데에 있는 값이 중간이 될 수 있다고 생각했다.
  
     - 최대힙 트리와 최소힙 트리의 사이즈의 균형을 유지하기 위해 번갈아 가며 넣었고, 최소힙 트리에 넣을 차례인데, 최대힙 트리의 가장 작은 값보다 그 값이 크면
  서로의 위치를 바꿔주는 것으로 문제를 해결했고, 최대힙의 첫 번 째 값이 최종적으로 중간값이 되게 자료구조를 만들었다. 


<br><br><br>
### <span style="color:violet"> 2. G5 캠프 준비

  - <span style="color:SKYBLUE"> 접근방법 
     - 메모리도 512mb , 시간제한은 2초인데, N 값이 10 단위여서 당연히 itertools를 돌리면 된다고 생각했다. <BR>
  2 ~ N 까지에 대한 combination list를 만들고, 해당 com_li의 최고난이도와 최소난이도의 차이가 X보다 클 때(문제의 조건) result를 1 증가시키면서
     - 모든 combination을 돌아 최종적으로 result를 출력했다. 
  


<br><br><br>
### <span style="color:violet"> 3. G3 미팅

  - <span style="color:SKYBLUE"> 접근방법 
     - 1000*1000 최대 백만개의 악수의 경우의 수가 생기는데, 조합을 돌리는 것은 당연히 시간초과가 나는 문제라고 생각했다. ( 1초 )  <BR><br>
     - 다른 접근이 필요하다고 생각하고 , dp를 생각하고 있었는데, LKH에게 dp라는 스포를 받았지만, 이미 아이디어를 생각하고 있던 상태라 괜찮았다.
  하지만 이 문제의 점화식을 도출하기 위한 방법이 정말 떠오르지 않았다. <br>
 
     - 보통 DP문제가 어떠한 경우의 수들 중에서 max를 구하는 것인데, 그 경우의 수가 최종적으로 3가지로 나뉘어진다고 생각했다.
     - ![image](https://user-images.githubusercontent.com/55376155/233304099-5abb5bf5-ade7-4737-aa89-e91a20ec184a.png)
    ![image](https://user-images.githubusercontent.com/55376155/233304166-8b612666-f9d7-4262-bbe8-9200e2b496f2.png)
    ![image](https://user-images.githubusercontent.com/55376155/233304590-7e0cc677-2925-4f30-bae3-1549a1d244a3.png)

     - 이를 점화식으로 표현 하였더니 답을 도출할 수 있었다. 
