#==============================================================================
# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#==============================================================================
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCount=OrderedDict()
        for c in s:
            if c in charCount:
                charCount[c]+=1
            else:
                charCount[c]=1
        
        
        for k,v in charCount.items():
            if v==1:
                for i in range(len(s)):
                    if s[i]==k:
                        return i
        return -1
        
         

s="leetcode"
index=Solution().firstUniqChar(s)
print(index)
assert index==0

s="loveleetcode"
index=Solution().firstUniqChar(s)
print(index)
assert index==2

