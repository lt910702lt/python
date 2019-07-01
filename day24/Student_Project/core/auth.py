import sys


def login():
    username = input('user :   ')
    password = input('password : ')
    print('登陆')
    with open('../db/userinfo', mode='r', encoding='utf-8') as f:
        for line in f:
            user, pwd, ident = line.split('|')
            if user == username and pwd == password:
                print('登陆成功')
                return username, ident


if __name__ == '__main__':
    login()
