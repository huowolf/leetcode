#旋转数组
#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#===============================================================================
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#===============================================================================
from _collections import deque
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len=len(nums)
        #print(nums[nums_len-k:])
        #print(nums[:nums_len-k])
        nums[:]=nums[nums_len-k:]+nums[:nums_len-k]
              
        #=======================================================================
        # d=deque(nums)
        # d.rotate(k)
        # nums[:]=list(d)
        # for i in nums:
        #     print(i,end=' ')
        #=======================================================================

    #右移k位和右移K'=k%N的情形是一样的
    def rotate2(self, nums, k):
        N=len(nums)
        k=k%N
        #每次右移一位，循环k次
        while k>0:
            last_num=nums.pop()
            nums.insert(0,last_num)
#             temp=nums[N-1]
#             i=N-1
#             while i>=1:
#                 nums[i]=nums[i-1]
#                 i=i-1
#             nums[0]=temp
            k=k-1
     
#===============================================================================
# 经典方法，三次倒置数组中对应位置的元素;
# 原理：数组元素右移k个位置的结果是，原来在后面的k个元素跑到了数组前面，
# 原来在前面的length-k个元素跑到了数组的后面，并且前后两部分元素各自的顺序和移动前一致，
# 而倒置整个数组元素就是让后面k个元素跑到前面去，让前面length-k个元素跑到后面去，
# 但是倒置之后前后两部分元素的顺序跟移动之前不一样了，倒置了，所以要把两部分的元素倒置回来
#===============================================================================
    def reverse(self,begin,end,nums):
        while begin<end:
            t=nums[begin]
            nums[begin]=nums[end]
            nums[end]=t
            begin=begin+1
            end=end-1
                 
                
    def rotate3(self, nums, k):
        
        length=len(nums)
        k=k%length
        #逆序所有元素
        self.reverse(0, length-1, nums)
        #逆序前k个元素
        self.reverse(0, k-1, nums)
        #逆序后length-k个元素
        self.reverse(k, length-1, nums)

        
nums=[1,2,3,4,5,6,7]        
Solution().rotate3(nums, 3)
print(nums)
assert nums==[5,6,7,1,2,3,4]

nums=[-1,-100,3,99]
Solution().rotate3(nums,2)
print(nums)
assert nums==[3,99,-1,-100]

nums=[1,2]
Solution().rotate3(nums,3)
print(nums)
assert nums==[2,1]

