from collections import deque

def count_r(s):
    r = 0
    for x in s:
        if x == '(':
            r += 1
    return r
    
def count_l(s):
    r = 0
    for x in s:
        if x == ')':
            r += 1
    return r
    
class Solution:
 
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        
        d = deque()
        d.append('(')
        while(d):
            t = d.popleft()
            
            if count_r(t) == n and count_l(t) == n:
                answer.append(t)
            elif count_r(t) == n:
                d.append(t + ')')
            elif count_r(t) == count_l(t):
                d.append(t + '(')
            elif count_r(t) > count_l(t):
                d.append(t + '(')
                d.append(t + ')')
        
        return answer
