#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        
        i=0
        j=len(s)-1
        while(i<j):
            while(not s[i].isalnum() and i<j):
                i=i+1
            while(not s[j].isalnum() and i<j):
                j=j-1    
            if(s[i].lower()!=s[j].lower()):
                return False
            else:
                i=i+1
                j=j-1    
        return True
                
                
 

s="A man, a plan, a canal: Panama" 
r=Solution().isPalindrome(s)
print(r)
assert r==True

s="race a car"
r=Solution().isPalindrome(s)
assert r==False
print(r)

