# 1+2+3+...+100 = ? 500 要求传参n
# 对功能的封装
# def total(n):
#     sum = 0
#     count = 1
#     while count <= int(n):
#         sum = sum + count
#         count += 1
#     return sum
#
#
# print(total(456))

# 判断n是奇数还是偶数
def ju(n):
    if n % 2 == 0:
        return "偶数"
    else:
        return "奇数"


print(ju(-3))
