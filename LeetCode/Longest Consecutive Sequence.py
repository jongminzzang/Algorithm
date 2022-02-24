class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        num_set = list(set(nums))
        num_set.sort()
        
        cnt = 1
        output = 1
        prev = num_set[0]
        
        for i in range(1, len(num_set)):
            if num_set[i] - prev == 1:
                cnt += 1
            else:
                output = max(output, cnt)
                cnt = 1
            prev = num_set[i]
            
        output = max(output, cnt)
        return output
