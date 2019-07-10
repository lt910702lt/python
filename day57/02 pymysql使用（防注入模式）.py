import pymysql

username = input('请输入用户名: ')
pwd = input('请输入密码: ')

conn = pymysql.connect(
    host='192.168.1.244',
    user='root',
    password='ABc.123456',
    port=3306,
    database='lt',
    charset='utf8'
)

cur = conn.cursor()

sql = "select * from userinfo where name=%s and password=%s"

print(sql)

resCount = cur.execute(sql, [username, pwd])

print(resCount)

if resCount:
    print('登陆成功！')
else:
    print('登陆失败!')

cur.close()
conn.close()
