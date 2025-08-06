class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        baris = [""] * numRows
        baris_sekarang = 0
        langkah = 1
        
        for karakter in s:
            baris[baris_sekarang] += karakter
            
            if baris_sekarang == 0:
                langkah = 1
            elif baris_sekarang == numRows - 1:
                langkah = -1
                
            baris_sekarang += langkah
            
        return "".join(baris)


solver = Solution()
s1 = "PAYPALISHIRING"
numRows1 = 3
print(f"Input: s='{s1}', numRows={numRows1} -> Output: '{solver.convert(s1, numRows1)}'")

s2 = "PAYPALISHIRING"
numRows2 = 4
print(f"Input: s='{s2}', numRows={numRows2} -> Output: '{solver.convert(s2, numRows2)}'")