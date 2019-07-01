# 权限管理：登陆、注册。。。
import json
from core.socket_client import MySocketClient


class Auth:
    def __init__(self):
        self.sk = MySocketClient()
        self.username = None

    def login(self):
        username = input('username : ')
        password = input('password : ')
        # 基于tcp的消息，需要判断不为空，否则会出现问题
        if username.strip() and password.strip():
            # 发送消息send,发送一个字典{'username':'alex','password':'123456'}
            ret_json = json.dumps()
            self.sk.mysend({'username': username, 'password': password})
