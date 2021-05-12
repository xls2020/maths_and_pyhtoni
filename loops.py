#使用嵌套循环输出2~100之间的素数：除了1和它本身以外不再有其他因数
l = []
i = 2
for i in range(2,100):#迭代2~100之间的数字
    j = 2
    for j in range(2,i):   #根据因子迭代
        if (i%j==0):   #确定第一个因子
            break     #跳出循环
    else:
        l.append(i)
print(l)

#求[a,b]之间的质数(即素数),除了1和它本身以外不再有其他因数
a = 1000
b = 10000
s = []
for num in range(a,b+1):
    snum = int(num*0.5+1)
    for i in range (2,snum):
        if num%i ==0:
            break
    else:
        s.append(num)
print(a,'到',b,'的质数有',s)
print(a,'到',b,'有',len(s),'个质数')