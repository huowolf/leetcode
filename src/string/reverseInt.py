#给定一个 32 位有符号整数，将整数中的数字进行反转。
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        
        s=str(x)
        if s.endswith('0'):
            s=s[:-1]
        if x<0:
            s=s[1:]
        s=s[::-1]
        
        if x<0:
            s='-'+s
            
        r=int(s)
        if r>2**31-1 or r<-2**31:
            return 0       
        return r
x=123        
r=Solution().reverse(x)
print(r)
assert r==321

x=-123        
r=Solution().reverse(x)
print(r)
assert r==-321

x=120        
r=Solution().reverse(x)
print(r)
assert r==21

x=1534236469     
r=Solution().reverse(x)
print(r)
assert r==0