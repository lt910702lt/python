# dic = {'a': 'b', 'c': 'd'}
# # 把字典中的key:value互换
# new_dic = {dic[key]: key for key in dic}
# print(new_dic)

lst1 = ["alex", "wusir", "taibai", "ritian"]
lst2 = ['sb', "很色", "很白", "很牛"]
# new_dic = {key:value for key in lst1 for value in lst2}
dic = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(dic)
