#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ord函数获取字符的整数表示
print(ord('a'))

# chr函数转换编码为字符
print(chr(65))
print(chr(20013))

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：x = b'ABC'
print('ABC'.encode('ascii'))     # 纯英文的str可以用ASCII编码为bytes
print('中文'.encode('utf-8'))    # 含有中文的str可以用UTF-8编码为bytes，含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化字符串
# 在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)