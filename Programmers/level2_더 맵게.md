## 문제 

(날짜) 21-10-15 
(링크) https://programmers.co.kr/learn/courses/30/lessons/42626

<br>


## 코드 
```py
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] + scoville[1] == 0:
        return -1
    
    while(scoville[0] < K):
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2*2)
        answer += 1
        if len(scoville) == 1:
            break
    
    if scoville[0] < K:
        return -1
    
    return answer
```
<br>


## 설명
힙 구조를 이용하면 간단하게 풀리는 문제이다.  
힙 구조를 위해 heapq를 이용할 수 있다. 

<br>
힙은 최대/최소 그리고 상수번째 최대/최소값을 구하고 갱신할때 이용하기 좋다.