class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        num = -2
        count = 0
        answer = 0
        
        for x in nums:
            if x == num+1:
                count += 1
                num = x
            elif x == num:
                pass
            else:
                if count > answer :
                    answer = count
                count = 1
                num = x
                
        if count > answer :
            answer = count
        return answer
