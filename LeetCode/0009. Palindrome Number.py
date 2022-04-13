class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        output = True
        for i in range(len(x)//2):
            if x[i] == x[len(x)-i-1]:
                pass
            else:
                output = False
                break
        return output
