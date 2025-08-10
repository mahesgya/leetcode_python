class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revNum = 0
        
        while x > revNum:
            revNum = revNum * 10 + (x % 10)
            x = x // 10
        
        return revNum == x or x == revNum // 10
        
solver = Solution()
result = solver.isPalindrome(10)
print(result)