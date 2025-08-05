import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        lo = 0
        hi = m
        combinedLength = m + n

        while lo <= hi:
            partitionX = (lo + hi) // 2
            partitionY = (combinedLength + 1) // 2 - partitionX

            leftX = self.getMax(partitionX, nums1)
            rightX = self.getMin(partitionX, nums1)
            
            leftY = self.getMax(partitionY, nums2)
            rightY = self.getMin(partitionY, nums2)
            
            if(leftX <= rightY and leftY <= rightX):
                if(combinedLength % 2 == 0):
                    return (max(leftX, leftY) + min(rightX, rightY))/2.0
                else:
                    return float(max(leftX, leftY))
            elif leftX > rightY:
                hi = partitionX - 1
            else: 
                lo = partitionX + 1
                
        return -1
            
    def getMax(self, partition, nums = []):
        if(partition == 0):
            return -math.inf
        else: 
            return nums[partition - 1]
    
    def getMin(self, partition, nums = []):
        if(partition == len(nums)):
            return math.inf
        else:
            return nums[partition]
        
    def findMedianSortedArraysMoreEffective(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        lo = 0
        hi = m
        half_len = (m + n + 1) // 2

        while lo <= hi:
            partitionX = (lo + hi) // 2
            partitionY = half_len - partitionX

            leftX = nums1[partitionX - 1] if partitionX != 0 else -math.inf
            rightX = nums1[partitionX] if partitionX != m else math.inf
            
            leftY = nums2[partitionY - 1] if partitionY != 0 else -math.inf
            rightY = nums2[partitionY] if partitionY != n else math.inf
            
            if(leftX <= rightY and leftY <= rightX):
                if((m + n) % 2 == 0):
                    return (max(leftX, leftY) + min(rightX, rightY))/2.0
                else:
                    return float(max(leftX, leftY))
            elif leftX > rightY:
                hi = partitionX - 1
            else: 
                lo = partitionX + 1
                
        return -1

solution = Solution()
nums1 = [2]
nums2 = []
result = solution.findMedianSortedArraysMoreEffective(nums1, nums2)
print(result)