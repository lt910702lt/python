# socket tcp  -- 只能与一个客户端连接
# socketserver tcp  -- 可以和多个客户端连接
import socketserver


# 首先要写一个类，必须继承socketserver的BaseRequestHandler
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #request就相当于一个conn
        # print(self.request.recv(1024).decode('utf-8'))
        while True:
            msg = self.request.recv(1024).decode('utf-8')
            print(msg)
            info = input('>>>')
            self.request.send(info.encode('utf-8'))

if __name__ == '__main__':
    # 调用创建的MyServer类
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    #永远的启一个服务
    server.serve_forever()