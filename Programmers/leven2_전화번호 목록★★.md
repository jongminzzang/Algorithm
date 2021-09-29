## 문제 

(날짜) 21-09-29  
(링크) https://programmers.co.kr/learn/courses/30/lessons/42577

<br>


## 코드 

첫번째 코드
- > 효율성 테스트 실패 (나머진 통과)
```py
def solution(phone_book):
    answer = True
    
    phone_book.sort(key =lambda x: len(x))
    
    
    for x in enumerate(phone_book):
        t = x[1]
        for y in  phone_book[x[0]+1:]:
            if y[0:len(t)] == t:
                answer = False
                break
        if answer == False: 
            break
    
    
    return answer
```

두번째 코드
- > 효율성 테스트 성공
- > 핵심 : X in dictionary?  의 시간복잡도는 O(1)이다!
```py
def solution(phone_book):
    answer = True
    
    phone_book.sort(key =lambda x: len(x))
    
    d = {}
    
    for x in phone_book:
        
        for i in range(1,len(x)):
            
            if x[0:i] in d:
                answer = False
                break

        if answer == False:
            break
        d[x] = 1
        
    
    return answer

```

세번째 코드
- > 
- > Trie 직접 구현
```py
code 
```


<br>


## 설명
처음에 떠오른 풀이는 트라이(Trie)였다.  

문제의 구분이 hash로 되어 있었지만  
사실 hashmap(dictionary)를 이용할 때 많은 양의 데이터가 있으면  
속도가 실제로 빠르지 않을 수 있다는 것을 배웠고, 실제로 경험도 해봤다.  
그래서 트라이로 하는 것이 맞겠다 생각했지만 떠오르는데로 다 해봤다.  

<br>

일단 첫번째 코드는 짧을 문자열을 본인보다 긴 문자열들과 모두 비교해보는 것이다.  
안 될줄 알았고 효율성 테스트에서 실패했다.  

<br>

두번째 코드가 hashmap을 이용한 것인데,  
긴 문자열에서 검색이 되는 짧은 문자열이 있는지 확인해 주는 것이다.  
hashmap에서 검색(is in hashmap)의 시간 복잡도는 O(1)이기 때문에, 문자열의 비교 O(n)보다 빠르다.   


<br>

세번째 코드는 trie를 이용한 것이다.  
사실 이 문제가 trie를 위한 문제라고 해도 될만큼 trie의 가장 기초적인 예시이다.











