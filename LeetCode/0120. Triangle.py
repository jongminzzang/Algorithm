class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        len_t = len(triangle)
        dp = [[] for i in range(len_t)]
        
        for x in triangle[len_t-1]:
            dp[len_t-1].append(x)
        
        for i in range(len_t-1, 0, -1):
            for j in range(i):
                dp[i-1].append(min(dp[i][j], dp[i][j+1]) + triangle[i-1][j])
                
        return dp[0][0]
