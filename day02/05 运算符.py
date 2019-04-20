'''
#计算机常用的数据（次幂）
print(2**0)
print(2**1)
print(2**2)
print(2**3)
print(2**4)
print(2**5)
print(2**6)
print(2**7)
print(2**8)
print(2**9)
print(2**10)

#赋值运算
a = 10
a += 20     #a = a + 20
print(a)


print(True and True and False and True and False)


# x or y ，如果x==0，那么就是y，否则是x
print(1 or 2)   #1
print(2 or 3)   #2
print(0 or 3)   #3
print(0 or 4)   #4
print(0 or 1 or 3 or 0 or 5)    #结果是1
# x and y ，如果x==0，那么就是0，否则是y
print(1 and 2)  #2
print(2 and 0)  #0
print(0 and 3)  #0
print(0 and 4)  #0

print(1 or 2 and 3) #1，先算and，再算or
print(0 or 4 and 3 or 7 or 9 and 6) #print(0 or 3 or 7 or 6)=3
print(2 > 5 and 3) #false，false相当于0
print(2 < 1 and 4 > 6 or 3 and 4 > 5 or 6) #6，（false or false or 6）

'''



