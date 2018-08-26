#移动零
#===============================================================================
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 1.必须在原数组上操作，不能拷贝额外的数组。
# 2.尽量减少操作次数。
#===============================================================================
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzero_num=0 #非零元素个数
        for i in nums:
            if i!=0:
                nums[nonzero_num]=i
                nonzero_num=nonzero_num+1
                        
            
        #补充0        
        start=nonzero_num
        for i in range(start,len(nums)):
            nums[i]=0
        
        return nums
 
 
nums=[0,1,0,3,12]       
result=Solution().moveZeroes(nums)
print(result)
assert result==[1,3,12,0,0]

nums=[1,0,0]       
result=Solution().moveZeroes(nums)
print(result)
assert result==[1,0,0]

nums=[0,1]       
result=Solution().moveZeroes(nums)
print(result)
assert result==[1,0]