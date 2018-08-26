l=[1,2,3,4]

#反向引用数组
print(l[-1])    #4
print(l[-2])    #3

#在数组头部插入元素
l.insert(0, 'new')
print(l)

#逆序遍历数组
for i in range(len(l)-1,-1,-1):
    print(l[i])
    
for i in l[::-1]:
    print(i)
    
N=len(l)
#l[N]=3
    
