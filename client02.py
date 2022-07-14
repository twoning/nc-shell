# -*- coding: UTF-8 -*- #
"""
@filename:client02.py
@author:Ning
@time:2022-07-14
"""
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('127.0.0.1',8888))

while 1:
    #循环提示用户输入内容
    data = input('请输入内容>>>').strip()
    #如果没有数据，则结束本次发送数据，开始下一次输入数据
    if not data:continue

    #有数据的话，将加密后的数据发送
    sock.send(data.encode())

    #将从socket接收到的数据进行解码并输出
    msg = sock.recv(10).decode()
    print(msg)
