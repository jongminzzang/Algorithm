class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def get_water(a, b):
            x = abs(a[0]-b[0])
            y = min(a[1],b[1])
            return x*y
        
        
        high_to_low = []
        low_to_high = []
        
        t = 0
        for i,x in enumerate(height):
            if t < x:
                low_to_high.append((i,x))
                t = x
        
        t = 0
        l = len(height)
        for i,x in enumerate(height[::-1]):
            if t < x:
                high_to_low.append((l-1-i,x))
                t = x        

        
        p1 = 0
        p2 = 0
        answer = 0
        while p1 < len(low_to_high) and p2 < len(high_to_low):          
            answer = max(answer, get_water(low_to_high[p1], high_to_low[p2]))   
            if low_to_high[p1][0] > high_to_low[p2][0]:
                break 
            if low_to_high[p1][1] < high_to_low[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return answer
