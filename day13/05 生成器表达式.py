# g = (i for i in range(10))
# print(g)
# print(g.__next__()) #0
# for e in g:
#     print(e)

gen = ("马化腾我第%s次氪金了" % i for i in range(10))
for el in gen:
    print(el)
