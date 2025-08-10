class Solution(object):
    def myAtoi(self, s):
        MAX_INT = 2**31 - 1
        MIN_INT = -(MAX_INT) - 1
        
        i, n = 0, len(s)
        
        #Skip spasi
        while i < n and s[i] == ' ':
            i += 1

        #Menentukan tanda negatif atau positif
        sign = 1
        isGetSign = 0

        while i < n and s[i] in ['+', '-']:
            if(s[i] == '-'):
                sign = -1
            if(isGetSign == 1):
                return 0
            isGetSign = 1
            i += 1
        
        #Menentukan angka
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num = num * sign
        
        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        return num
        
solver = Solution()
result1 = solver.myAtoi("42")
result2 = solver.myAtoi(" -42")
result3 = solver.myAtoi("1337c0d3")

print(result1)
print(result2)
print(result3)
        
        