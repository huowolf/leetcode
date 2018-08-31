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
    
print(1 in l)

mylist=[0]*3
print(mylist)

mylist=[[0]*10 for i in range(10)]
print(mylist)

mylist=[1,5,1,6,8,5]
print(mylist.count(1))
print(mylist.count(5))
    
print(list(range(9)))

mylist=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(mylist[1][2])
print('-'*15)
for i in range(3):
    for j in range(3):
        print(mylist[j][i],end=" ")
print('\n'+'-'*15)
test = [[0 for i in range(3)] for j in range(4)]
print(test)

for i in range(0,9,3):
    for j in range(0,9,3):
        print(i,j)
    print('-------------------')
