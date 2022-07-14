# -*- coding: UTF-8 -*- #
"""
@filename:client01.py
@author:Ning
@time:2022-07-14
"""

import socket
#引入套接字库
'''
网络上的两个程序通过一个双向的通信连接实现数据的交换，连接的一端称为一个socket，套接字
描述IP地址：端口，是一个通信链的句柄
实现不同虚拟机或计算机之间的通信，主机一般运行多个软件，同时提供几种服务，每种服务都打开一个socket
绑定到一个端口上，不同端口对应不同服务
socket库为OS的socket实现提供了python接口
'''



sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
'''
基于网络，TCP协议，默认不写也是这个
.socket(family , type) AF == Address Family
family指host种类，AF_UNIX: AP_LOCAL基于本地文件
                  AF_NETLINK: 基于Linux系统的套接字
                  AF_INET: internet protocol version 4
                  AR_INET6: internet protocol version 6
type指套接字类型：SOCKET_STREAM:流套接字，使用TCP socket
                  SOCK_DGRAM:数据报文套接字，使用UDP socket
                  SOCK_RAW:raw套接字
'''

sock.connect(('127.0.0.1',12348))
#将socket连接到定义的主机和端口上，通常用于客户端

sock.send(b'hello world')
'''
send方法发送数据报文，但是必须是bytes类型，所以需要b
send( )发送数据时必须先建立socket连接，不然会出现error
recv方法和send方法发送和接收消息，都是采用字符串的形式，send方法返回已发送的字符个数
调用recv时，必须制定一个整数控制本次调用所接受的最大数据量
'''

sock.close()
#关闭连接

