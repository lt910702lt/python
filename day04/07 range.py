# s = "刚才alex来看我了，然后走了"
# for c in s:
#     print(c)

#range()
# for i in range(10): #从0开始,到10结束
# #     print(i)

# for i in range(3, 7):   #从3开始，打印到7结束，不能到7
#     print(i)

# for i in range(3, 10, 2):   #从3到10，每2个取一个
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

#求1-2+3-4...+99-100=?
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
