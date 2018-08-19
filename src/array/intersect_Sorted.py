#https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/26/
#两个数组的交集 II
#给定两个数组，编写一个函数来计算它们的交集
#===============================================================================
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#===============================================================================
class Solution:
    #如果两个数组都已经排序
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        len1,len2=len(nums1),len(nums2)
        i,j=0,0
        #双指针法
        while i<len1 and j<len2:
            if nums1[i]<nums2[j]:
                i=i+1
            elif nums1[i]>nums2[j]:
                j=j+1
            else:
                result.append(nums1[i])
                i=i+1
                j=j+1
                
        return result
  
    
nums1 = [1,2,2,1] 
nums2 = [2,2] 
nums1.sort()
nums2.sort()
print('nums1:',nums1)
print('nums2:',nums2)
l=Solution().intersect(nums1, nums2)
print(l)  
print('-----------') 

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1.sort()
nums2.sort()
print('nums1:',nums1)
print('nums2:',nums2)
l=Solution().intersect(nums1, nums2)
print(l)

        