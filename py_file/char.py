
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#char字符相关" data-toc-modified-id="char字符相关-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>char字符相关</a></div><div class="lev2 toc-item"><a href="#1.1-ord函数获取字符的整数表示" data-toc-modified-id="1.1-ord函数获取字符的整数表示-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>1.1 ord函数获取字符的整数表示</a></div><div class="lev2 toc-item"><a href="#1.2-chr函数转换编码为字符" data-toc-modified-id="1.2-chr函数转换编码为字符-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>1.2 chr函数转换编码为字符</a></div><div class="lev2 toc-item"><a href="#1.3-编码" data-toc-modified-id="1.3-编码-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>1.3 编码</a></div><div class="lev3 toc-item"><a href="#1.3.1-纯英文的str可以用ASCII编码为bytes" data-toc-modified-id="1.3.1-纯英文的str可以用ASCII编码为bytes-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>1.3.1 纯英文的str可以用ASCII编码为bytes</a></div><div class="lev3 toc-item"><a href="#1.3.2-含有中文的str可以用UTF-8编码为bytes" data-toc-modified-id="1.3.2-含有中文的str可以用UTF-8编码为bytes-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>1.3.2 含有中文的str可以用UTF-8编码为bytes</a></div><div class="lev3 toc-item"><a href="#1.3.3-如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法" data-toc-modified-id="1.3.3-如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法-133"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>1.3.3 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法</a></div><div class="lev2 toc-item"><a href="#1.4-格式化字符串" data-toc-modified-id="1.4-格式化字符串-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>1.4 格式化字符串</a></div><div class="lev3 toc-item"><a href="#1.4.1-在Python中，采用的格式化方式和C语言是一致的，用%实现" data-toc-modified-id="1.4.1-在Python中，采用的格式化方式和C语言是一致的，用%实现-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>1.4.1 在Python中，采用的格式化方式和C语言是一致的，用%实现</a></div><div class="lev3 toc-item"><a href="#1.4.2-格式化整数和浮点数还可以指定是否补0和整数与小数的位数：" data-toc-modified-id="1.4.2-格式化整数和浮点数还可以指定是否补0和整数与小数的位数：-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>1.4.2 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：</a></div>

# # char字符相关

# ## 1.1 ord函数获取字符的整数表示

# In[1]:

print(ord('a'))


# ## 1.2 chr函数转换编码为字符

# In[2]:

print(chr(65))
print(chr(20013))


# ## 1.3 编码
# > 
# * 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# * 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# * Python对bytes类型的数据用带b前缀的单引号或双引号表示：x = b'ABC'

# ### 1.3.1 纯英文的str可以用ASCII编码为bytes

# In[3]:

print('ABC'.encode('ascii'))


# ### 1.3.2 含有中文的str可以用UTF-8编码为bytes
# > * 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# In[4]:

print('中文'.encode('utf-8'))


# ### 1.3.3 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

# In[5]:

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# ## 1.4 格式化字符串

# ### 1.4.1 在Python中，采用的格式化方式和C语言是一致的，用%实现

# In[6]:

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))


# ### 1.4.2 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

# In[7]:

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

