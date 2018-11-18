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
    
    def isAnagram3(self, s, t):
        if len(s)!=len(t):
            return False
        
    #不能解决重复字符不同的问题    
#         set1 = set(s)
#         set2 = set(t)
#         return not (set1-set2)
       
        result1 = result2 = 0
        for i in s:
            result1 += (ord(i)-ord('a'))
        for j in t:
            result2 += (ord(j)-ord('a'))
        
        set1 = set(s)
        set2 = set(t)
        return not (set1-set2) and  result1 == result2
        
 
s = "anagram"
t = "nagaram"     
result=Solution().isAnagram3(s, t)
print(result)
assert result==True

s = "rat"
t = "car"
result=Solution().isAnagram3(s, t)
print(result)
assert result==False

s = "a"
t = "ab"
result=Solution().isAnagram3(s, t)
print(result)
assert result==False

s = "aacc"
t = "ccac"
result=Solution().isAnagram3(s, t)
print(result)
assert result==False
