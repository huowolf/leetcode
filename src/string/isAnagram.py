#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        t=list(t)
        for i in s:
            
            for j in range(len(t)-1, -1, -1):
                #检测本次循环并未发生匹配
                if j==0 and i!=t[j]:
                    return False
                if i==t[j]:
                    #进行了一次相同字母的匹配
                    t.pop(j)
                    break                 
        return True  

    def isAnagram2(self, s, t):
        return Counter(s) == Counter(t)
 
s = "anagram"
t = "nagaram"     
result=Solution().isAnagram(s, t)
print(result)
assert result==True

s = "rat"
t = "car"
result=Solution().isAnagram(s, t)
print(result)
assert result==False

s = "a"
t = "ab"
result=Solution().isAnagram(s, t)
print(result)
assert result==False
