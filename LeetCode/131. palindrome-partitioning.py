class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        if len(s) == 1:
            return [[s]]
        
        l = ['']
        while len(l[0]) < len(s)-1:
            t = l.pop(0)
            l.append(t+'0')
            l.append(t+'1')
            
        
        can = []
        temp = []
        for x in l:
            left = 0
            right = 0
            for i, k in enumerate(x):
                if k == '1':
                    right = i
                    temp.append(s[left:right+1])
                    left = i+1
            if right+1 != len(s):
                temp.append(s[left:])
            
            can.append(temp)
            temp = []
        
        
        answer = []
        for t in can:
            c = 0
            for x in t:
                if x != x[::-1]:
                    pass
                else: 
                    c += 1
            if c == len(t):   
                answer.append(t)
        return answer
