s='hello'
print(s[0])

x=123
print(str(x)+'1111')

x=-123
s=str(x)[1:]
print(s)

s="1,a"
for i in s:
    print(i.isalnum())
    
s='w'
print(s>'9')
s='a'
print(s<'1')

str="  aa"
for i in str:
    print(i== " ")