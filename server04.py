# -*- coding: UTF-8 -*- #
"""
@filename:server04.py
@author:Ning
@time:2022-07-14
"""


import socket
import struct
import subprocess




"""执行命令函数"""
def exec_cmd(command):
    obj = subprocess.Popen(command.decode("utf-8"),shell=True,stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# subprocess 模块允许我们启动一个新进程
# 并连接到它们的输入/输出/错误管道，从而获取返回值。
# Popen方法是subprocess核心，子进程创建和管理都靠它处理
# Popen("shell命令参数",stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄)

    stdout_res = obj.stdout.read() + obj.stderr.read()
    #输出结果无论正确与否都可以有输出回显
    return stdout_res


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
    if not data:return #如果没有数据则返回
    if type(data) == str:
        data = data.encode("utf-8")
    cmd_len = struct.pack('i', len(data))
    sock.send(cmd_len)
    # 发送命令
    sock.send(data)

def main():
    server = socket.socket()
    server.bind(('192.168.6.177', 8888))
    server.listen(5)
    print("等待链接.....")
    conn, address = server.accept()
    print(f"新建一个链接,链接管道为{conn}")
    print(f"当前客户端的地址为{address}")
    while 1:
        try:
            cmd = input((f'shell>')).strip()
            if not cmd:continue
            if cmd == "q":
                send_data(conn,cmd)
                break
            send_data(conn, cmd)
            # 接收客户端发来的内容
            data = recv_data(conn)
            print(data.decode("gbk").strip())
            #解码后原样输出
        except Exception:
            break
    conn.close()
    server.close()


if __name__ == '__main__':
    main()

