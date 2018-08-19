#存在重复
# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#===============================================================================
# 输入: [1,2,3,1]
# 输出: true
#===============================================================================
from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c=Counter(nums)
        for i in c:
            if c[i]>1:
                return True
             
        return False
    

result=Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(result)