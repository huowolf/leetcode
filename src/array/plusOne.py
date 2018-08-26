#===============================================================================
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#===============================================================================
from hmac import digest
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last=len(digits)-1
        digits[last]=digits[last]+1
        if digits[last]>9:
            for i in range(last,-1,-1):
                if digits[i]==10:
                    #将当前位置0
                    digits[i]=0
                    #如果还未遍历到第一位，直接在前一位上加1
                    if i>0:
                        digits[i-1]=digits[i-1]+1
                    #如果遍历到第一位，在第一位之前补1
                    else:
                        digits.insert(0,1)
                #如果某一位进位之后不超过10,那么进位结束，退出循环
                else:
                    break

        return digits

if __name__ == '__main__':
    digits=[1,2,3]
    result = Solution().plusOne(digits)
    print(result)
    assert result==[1,2,4]
    
    digits=[9]
    result = Solution().plusOne(digits)
    print(result)
    assert result==[1,0]
    
    digits=[9,9,9]
    result = Solution().plusOne(digits)
    print(result)
    assert result==[1,0,0,0]