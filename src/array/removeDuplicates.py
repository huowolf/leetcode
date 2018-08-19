#从排序数组中删除重复项
#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#===============================================================================
# 给定数组 nums = [1,1,2], 
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
# 你不需要考虑数组中超出新长度后面的元素。
#===============================================================================
# 当我们遇到nums[j]≠nums[i] 时，跳过重复项的运行已经结束，
# 因此我们必须把它（nums[j]）的值复制到 nums[i + 1]。
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        #i快指针(用来遍历原列表)
        #j慢指针(新的数组下标表示）
        i,j=0,0
        while i<len(nums):
            #相邻两个数不同时，进行操作
            if nums[i]!=nums[j]:
                j=j+1
                #就地存储
                nums[j]=nums[i]
            
            i=i+1
        return j+1
    

if __name__ == '__main__':
    nums = [1,1,2]
    lenth = Solution().removeDuplicates(nums)
    print(lenth)
    for i in range(lenth):
        print(nums[i])
    