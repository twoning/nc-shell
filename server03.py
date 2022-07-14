# -*- coding: UTF-8 -*- #
"""
@filename:server03.py
@author:Ning
@time:2022-07-14
"""

import socket
import struct


def recv_data(sock, buf_size=1024):
    """解决粘包"""
    # 先接受命令执行结果的长度
    x = sock.recv(4)
    all_size = struct.unpack('i', x)[0]
    # 接收真实数据
    recv_size = 0
    data = b''
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
    server = socket.socket()
    server.bind(('127.0.0.1', 8888))
    server.listen(2)
    print("等待链接.....")
    conn, c_addr = server.accept()
    print(f"新建一个链接,链接管道为{conn}")
    print(f"当前客户端的地址为{c_addr}")
    while 1:
        try:
            data = input(f"请输入你要发送的内容>").strip()
            if not data:continue
            send_data(conn,data)
            if data == "q":
                break
            # 接收客户端发来的内容
            data = recv_data(conn)
            print(data.decode("utf-8"))
        except Exception:
            break
    conn.close()
    server.close()


if __name__ == '__main__':
    main()
