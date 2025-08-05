class Solution(object):
    def longestPalindrome(self, s):
        palindrome_terpanjang = ""
        for i in range(len(s)):
            #cek ganjil
            palindrome_ganjil = self.cek_dari_center(s, i, i)
            if len(palindrome_ganjil) > len(palindrome_terpanjang):
                palindrome_terpanjang = palindrome_ganjil
            
            #cek genap
            palindrome_genap = self.cek_dari_center(s, i, i + 1)
            if len(palindrome_genap) > len(palindrome_terpanjang):
                palindrome_terpanjang = palindrome_genap
                
        return palindrome_terpanjang
            
    def cek_dari_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        

        return s[left + 1: right]
    
solution = Solution()
result = solution.longestPalindrome("babad")
print(result)
        