'''
Created on 2018年8月30日

@author: huowolf
'''
#===============================================================================
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#===============================================================================
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag=[]
        for i,num in enumerate(nums):
            pair=target-num
            for j in range(i+1,len(nums)):
                if nums[j]==pair:
                    flag.append(i)
                    flag.append(j)
                      
        return flag
    

nums=[2, 7, 11, 15]
target=9   
l=Solution().twoSum(nums, target)
print(l)
assert l==[0,1]

nums=[3,2,4]
target=6
l=Solution().twoSum(nums, target)
print(l)
assert l==[1,2]