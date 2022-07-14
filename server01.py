# -*- coding: UTF-8 -*- #
"""
@filename:server01.py
@author:Ning
@time:2022-07-14
"""

import socket
#引入socket库

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('127.0.0.1',12348))
#服务器绑定socket地址，便于客户端connect连接

sock.listen(5)
'''
监听模式，监听外来的连接请求，让服务器开始监听客户端发来的连接请求
参数为最多连接数，至少为1，如果多链接则必须排队
连接数满则拒绝新的连接请求
'''

print("等待客户端连接......")
conn , client_address = sock.accept()
'''
accept方法可返回客户端连接之后的socket，带有客户端地址信息
返回类型为 双元素元组 ，形如（connection,address）,第一个元素是新的socket对象，第二个元素是客户的IP地址
accept方法在调用时，socket状态会阻塞，客户端请求连接时，建立连接并返回服务器
'''

print(f"建立了一个管道：{conn}",)
# 将accept获取到的客户端socket信息输出
print(f"客户端的地址：{client_address}")
#将accept获取到的客户端IP地址输出

msg = conn.recv(1024)
'''
recv方法从socket中接收数据，最多接收后面括号内的字符，如果溢出则会等待下一次输出
'''

print(f"客户端消息：{msg.decode()}")
# 由于传输时是bytes格式，所以在接收到之后需要进行解码
conn.close()
# 关闭管道连接，回收资源
sock.close()
# 关闭服务端sock对象