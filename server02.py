# -*- coding: UTF-8 -*- #
"""
@filename:server02.py
@author:Ning
@time:2022-07-14
"""
'''
版本2虽然相对于版本1增加了自定义的消息内容，并且增加了循环，但是
在消息发送时会死循环，并且出现粘包现象，这是由于接收方与发送方的
窗口大小不一致，且TCP机制定义了会保存数据合成一个TCP段再发送出去，
所以需要改进
'''

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('127.0.0.1',8888))

sock.listen(5)

print("等待客户端连接......")
client,address = sock.accept()

print(f"建立了一个管道：{client}",)
# 将accept获取到的客户端socket信息输出
print(f"客户端的地址：{address}")
#将accept获取到的客户端IP地址输出

while 1:
    try:
        #5.接收数据
        msg = client.recv(10).decode()
        if not msg:break
        print(f"客户端消息：{msg}")
        client.send(msg.upper().encode())
    except Exception:
        break

client.close()
sock.close()
