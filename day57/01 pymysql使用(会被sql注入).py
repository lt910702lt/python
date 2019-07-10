# 导入模块
import pymysql

username = input('请输入用户名: ')
pwd = input('请输入密码: ')

# 创建mysql链接
conn = pymysql.connect(
    host='192.168.1.244',
    user='root',
    password="ABc.123456",
    database='lt',
    port=3306,
    charset='utf8'
)

# 创建游标
cur = conn.cursor()

sql = "select * from userinfo where name= '%s' and password = '%s' " % (username, pwd)

# 变量拼接在[]里面防止sql注入
resCount = cur.execute(sql)

print(resCount)

if resCount:
    print('登陆成功!')
else:
    print('登陆失败！')


cur.close()
conn.close()

'''
注入方式一：alex' -- asdsadasdas
注入方式二：sdasdad' or 1=1 -- asdasdasda
'''