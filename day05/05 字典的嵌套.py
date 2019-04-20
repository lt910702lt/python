dic = {
    "name": "汪峰",
    "age": 58,
    "wife": {
        "name": "国际章",
        "salary": 180000,
        "age": 37
    },
    "children": [
        {"name": "老大", "age": 18},
        {"name": "老二", "age": 118}
    ]
}

#输出汪峰二儿子的年龄
print(dic["children"][1]["age"])

#汪峰媳妇的工资
print(dic["wife"]["salary"])


