class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        l = 0
        r = len(nums)-1
        
        while True:
            c = (l+r)//2
            if nums[c] == target:
                answer = c
                break
            elif nums[c] > target:
                r = c-1
            elif nums[c] < target:
                l = c+1
            if l > r:
                break
                
        return answer 
