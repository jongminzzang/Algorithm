## 문제
21-09-28  
https://programmers.co.kr/learn/courses/30/lessons/42746  

<br>


## 코드
```py
def solution(numbers):
    answer = ''
    str_arr = []
    for x in numbers:
        str_arr.append(str(x))
    str_arr.sort(key = lambda x: x*3)

    for x in str_arr[::-1]:
        answer += x

    if answer[0] == '0':
        return '0'

    else:
        return answer
```

<br>

## 설명

<mark style='background-color: #dcffe4'>
어렵지 않으면서도 알고리즘에서 아이디어가 중요하다는 것을 알려준 문제 
</mark>

<br>
<br>

숫자를 문자열로써 다룰 때가 더 유리할 수도 있다는 생각을 갖게 해준 문제이다.  

전에 한번 풀어봐서 쉽게 했지만 처음에 이 풀이를 봤을 때는 매우 놀랐다.  

내가 처음에 풀었던 방식은 방정식을 이용하여 한자리수 두자리수 세자리수들의 순서를 정해주는 것이였는데,  
풀리긴 했지만 푸는데 생각보다 시간이 오래걸렸고 생각보다 남들이 쉽게 이해하지 못했다.  
