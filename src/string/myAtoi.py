#请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#小数需要转化为整数，遇到小数点停止遍历即可（这是测试数据的要求）
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number=0;
        flag=1              #代表是正数还是负数
        meetnumber=False    #是否遇到过数字
        meetdot=False       #是否遇到过小数点
        nextbenumber=False  #正负号之后应该紧跟数字
        for i in str:
            if(i!=' '):
                if(i!='-' and i!='+' and i>'9' and i!='.'):
                    if(meetnumber==False):
                        return 0
                    else:
                        break    
                else:
                    if(i=='-'): 
                        if(nextbenumber and  not meetnumber):
                            return 0;
                        if(nextbenumber and  meetnumber):
                            break
                        nextbenumber=True
                        if(meetnumber):
                            break
                        flag=-1
                    elif(i=='+'):  
                        #如果再次遇到正负号(且没有遇到过数字)，则解析失败
                        if(nextbenumber and not meetnumber):
                            return 0;
                        #如果再次遇到正负号(且遇到过数字)，则停止解析
                        if(nextbenumber and  meetnumber):
                            break
                        nextbenumber=True
                        #如果在遇到数字以后再次遇到遇到正负号，则停止解析
                        if(meetnumber):
                            break
                        flag=1
                    elif(i=='.'):
                        meetdot = True
                    else:
                        if(meetdot == False):
                            number = number*10+int(i)
                            meetnumber = True
            else:
                #如果在遇到数字以后遇到空格，停止解析字符串
                if(meetnumber):
                    break
                #如果在遇到正负号以后遇到空格，则解析失败
                if(nextbenumber):
                    return 0
                           
        result= flag*number 
        if(result > 2 **31 -1):
            return  2 **31 -1     
        if(result < -2 **31):
            return  -2 **31    
        return result;            
                
        
str="42"        
r = Solution().myAtoi(str)
print(r)
assert r==42

str="   -42"      
r = Solution().myAtoi(str)
print(r)
assert r== -42

str="4193 with words"     
r = Solution().myAtoi(str)
print(r)
assert r==4193

str="words and 987"        
r = Solution().myAtoi(str)
print(r)
assert r==0

str="-91283472332"    
r = Solution().myAtoi(str)
print(r)
assert r== -2147483648

str="3.14159"    
r = Solution().myAtoi(str)
print(r)
assert r== 3

str="+-2"    
r = Solution().myAtoi(str)
print(r)
assert r== 0

str="  -0012a42" 
r = Solution().myAtoi(str)
print(r)
assert r== -12


str="   +0 123" 
r = Solution().myAtoi(str)
print(r)
assert r== 0


str="-   234" 
r = Solution().myAtoi(str)
print(r)
assert r== 0

str="0-1"
r = Solution().myAtoi(str)
print(r)
assert r== 0

str="-5-"
r = Solution().myAtoi(str)
print(r)
assert r== -5

str="-13+8"
r = Solution().myAtoi(str)
print(r)
assert r== -13