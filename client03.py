# -*- coding: UTF-8 -*- #
"""
@filename:client03.py
@author:Ning
@time:2022-07-14
"""

import socket
import struct
'''
struct模块可以把一个类型转换为固定长度的bytes
解决粘包思路：
通过struck模块将需要发送的内容的长度进行打包，打包成一个4字节长度的数据发送到对端，
对端只要取出前4个字节，然后对这四个字节的数据进行解包，
拿到你要发送的内容的长度，然后通过这个长度来继续接收我们实际要发送的内容。
'''

def recv_data(sock,buf_size=1024):
    """解决粘包"""
    #先接收命令执行结果的长度
    x = sock.recv(4)
    all_size = struct.unpack('i',x)[0]
    #将服务器传递过来的整体data大小数值赋值给all——size
    '''
    struct.unpack方法，先接收对端发送的四个字节，然后通过unpack将该四字节转换为
    对应格式的元组
    x --- pad byte          c --- char          b --- signed char
    B --- unsigned char     h --- short         H --- unsigned short
    i --- int               I --- unsigned int  l --- long
    L --- unsigned long     q --- long long     Q --- unsigned long long
    f --- float             d --- double        s = char[] (string)
    p = char[]              P void * integer          
    #接收真实的数据
    '''
    recv_size = 0
    #接收数据大小
    data = b''
    '''
    如果当前可接收的数据大小还未到对面最大值的数据大小，则继续接收并输出
    '''
    while recv_size < all_size:
        data += sock.recv(buf_size)
        recv_size += buf_size
    return data
def send_data(sock, data):
    """发送数据也解决粘包问题"""
    if type(data) == str:
        data = data.encode("utf-8")
    # 新增发送命令的粘包解决方案
    # 计算命令长度 , 打包发送
    cmd_len = struct.pack('i', len(data))
    sock.send(cmd_len)
    # 发送命令
    sock.send(data)


def main():
    client = socket.socket()
    client.connect(('127.0.0.1',8888))
    while 1:
        try:
            msg = recv_data(client)
            if msg == b"q":break
            #加入判断，如果返回消息为q，则终止循环，退出聊天
            print(msg.decode("utf-8"))
            #发送内容
            msg = input(f"请输入你要回复的内容>>>").strip()
            send_data(client,msg)
        except Exception:
            break
    client.close()


if __name__ == '__main__':
    main()

