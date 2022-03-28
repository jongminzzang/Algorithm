class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        l = 0
        r = n
        while True:
            c = (l+r)//2
            if isBadVersion(c):
                r = c
            else :
                l = c
            if r == l+1:
                break
        return r
