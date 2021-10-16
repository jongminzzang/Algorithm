## 문제 

(날짜) 21-10-15  
(링크) https://programmers.co.kr/learn/courses/30/lessons/43165

<br>


## 코드 
```py
global answer
answer = 0

def dfs(val, target, numbers):
    global answer 
    if len(numbers) == 1:
        if val + numbers[0] == target:
            answer += 1
        if val - numbers[0] == target:
            answer += 1
        return
            
    dfs(val+numbers[0], target, numbers[1:])
    dfs(val-numbers[0], target, numbers[1:])
    


def solution(numbers, target):
    dfs(0, target, numbers)
    global answer
    
    return answer
```
<br>


## 설명

완전탐색을 할 수 있어야 한다.  

다만 dfs와 bfs중에서 어떤것을 선택할지의 문제인데,  
이 경우 bfs로 해결하려고 할 경우 최대 2^20개의 큐가 쌓이게 됨으로 dfs로 하는 것이 간단하다.

dfs로 진행할 경우 스택의 깊이가 20까지밖에 진행되지 않으므로 무난히 진행될 수 있다.


