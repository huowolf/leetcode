#https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/26/
#两个数组的交集 II
#给定两个数组，编写一个函数来计算它们的交集
#===============================================================================
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#===============================================================================
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
#遍历其中一个数组，发现相同元素时添加到新列表中，同时删去另一个数组中的一个相同元素
        for i in nums1:
            for j in nums2:
                #删除相同元素后，同时跳出该趟搜索
                if i==j:
                    result.append(i)
                    nums2.remove(j)
                    break

        return result
  
    
nums1 = [1,2,2,1] 
nums2 = [2,2] 
l=Solution().intersect(nums1, nums2)
print(l)   

nums1 = [4,9,5]
nums2 = [9,4,9,8,4] 
l=Solution().intersect(nums1, nums2)
print(l)

        