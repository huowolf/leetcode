#编写一个函数，其作用是将输入的字符串反转过来。
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
    
s="A man, a plan, a canal: Panama"
str=Solution().reverseString(s)
print(str)
assert str=="amanaP :lanac a ,nalp a ,nam A"
