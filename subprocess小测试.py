# -*- coding: UTF-8 -*- #
"""
@filename:subprocess小测试.py
@author:Ning
@time:2022-07-14
"""

import subprocess
'''
subprocess 模块允许我们启动一个新进程
并连接到它们的输入/输出/错误管道，从而获取返回值。 
'''

obj = subprocess.Popen("ipconfig",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#Popen方法是subprocess核心，子进程创建和管理都靠它处理
# Popen("shell命令参数",stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄)


res = obj.stdout.read()
print(res)
#将命令返回的内容原样输出
print(res.decode('gbk'))
#gbk解码之后再次输出

#如果shell命令执行错误，则输出stderr的内容
res_err = obj.stderr.read()
print(res_err)
