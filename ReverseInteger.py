class Solution(object):
    def reverse(self, x):
        MAX_INT = 2**31 - 1
        tanda = 1 if x >= 0 else - 1
        x = abs(x)
        x_hasil = 0
        
        while x != 0:
            digit = x % 10
            
            if x_hasil > MAX_INT // 10 or (x_hasil == MAX_INT // 10 and digit > 7):
                return 0
            
            x_hasil = x_hasil * 10 + digit
            
            x = x // 10
        
        return x_hasil * tanda
            

solution = Solution()
result = solution.reverse(321)
print(result)        