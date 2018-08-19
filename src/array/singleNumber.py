#https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/25/
#只出现一次的数字
#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#===============================================================================
# 输入: [2,2,1]
# 输出: 1
#===============================================================================
#这里如果用异或的思路的话，很简单。
#任何数异或它本身是0，所以两个相同的元素异或完以后为0
#所以将数组的元素依次异或，成对的都抵消了，只留下那个落单的元素
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in nums:
            result=result^i
        return result
    
    #传统做法，时间复杂度为(O(n))
    def singleNumber2(self, nums):
        numdict={}
        for i in nums:
            if i in numdict:
                numdict[i]+=1
            else:
                numdict[i]=1
        
        for k,v in numdict.items():
            if v==1:
                return k
    
nums=[2,2,1]
#r=Solution().singleNumber(nums)
r=Solution().singleNumber2(nums)
print(r)