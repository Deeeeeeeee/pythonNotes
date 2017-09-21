
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#list,-tuple,-dict-and-set----列表和元组" data-toc-modified-id="list,-tuple,-dict-and-set----列表和元组-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>list, tuple, dict and set -- 列表和元组</a></div><div class="lev2 toc-item"><a href="#1-list" data-toc-modified-id="1-list-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>1 list</a></div><div class="lev3 toc-item"><a href="#1.1-print-list-classmate,-and-get-the-length-of-it-by-using-len()" data-toc-modified-id="1.1-print-list-classmate,-and-get-the-length-of-it-by-using-len()-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>1.1 print list classmate, and get the length of it by using len()</a></div><div class="lev3 toc-item"><a href="#1.2-用索引来访问list中每一个位置的元素，记得索引是从0开始的" data-toc-modified-id="1.2-用索引来访问list中每一个位置的元素，记得索引是从0开始的-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>1.2 用索引来访问list中每一个位置的元素，记得索引是从0开始的</a></div><div class="lev3 toc-item"><a href="#1.3-用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个" data-toc-modified-id="1.3-用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>1.3 用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个</a></div><div class="lev3 toc-item"><a href="#1.4-list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾" data-toc-modified-id="1.4-list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾-114"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>1.4 list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾</a></div><div class="lev3 toc-item"><a href="#1.5-把元素插入到指定的位置，比如索引号为1的位置" data-toc-modified-id="1.5-把元素插入到指定的位置，比如索引号为1的位置-115"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>1.5 把元素插入到指定的位置，比如索引号为1的位置</a></div><div class="lev3 toc-item"><a href="#1.6-要删除list末尾的元素，用pop()方法" data-toc-modified-id="1.6-要删除list末尾的元素，用pop()方法-116"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>1.6 要删除list末尾的元素，用pop()方法</a></div><div class="lev3 toc-item"><a href="#1.7-要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数" data-toc-modified-id="1.7-要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数-117"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>1.7 要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数</a></div><div class="lev2 toc-item"><a href="#2-dict" data-toc-modified-id="2-dict-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>2 dict</a></div><div class="lev3 toc-item"><a href="#2.1-迭代" data-toc-modified-id="2.1-迭代-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>2.1 迭代</a></div><div class="lev4 toc-item"><a href="#2.1.1-key迭代，因为dict的key存储方式不是顺序的，而是hash，所以输出并不是顺序的" data-toc-modified-id="2.1.1-key迭代，因为dict的key存储方式不是顺序的，而是hash，所以输出并不是顺序的-1211"><span class="toc-item-num">1.2.1.1&nbsp;&nbsp;</span>2.1.1 key迭代，因为dict的key存储方式不是顺序的，而是hash，所以输出并不是顺序的</a></div><div class="lev4 toc-item"><a href="#2.1.2-value迭代" data-toc-modified-id="2.1.2-value迭代-1212"><span class="toc-item-num">1.2.1.2&nbsp;&nbsp;</span>2.1.2 value迭代</a></div><div class="lev4 toc-item"><a href="#2.1.3-key,value同时迭代" data-toc-modified-id="2.1.3-key,value同时迭代-1213"><span class="toc-item-num">1.2.1.3&nbsp;&nbsp;</span>2.1.3 key,value同时迭代</a></div><div class="lev2 toc-item"><a href="#3-列表生成式" data-toc-modified-id="3-列表生成式-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>3 列表生成式</a></div><div class="lev3 toc-item"><a href="#3.1-生成一个1~10的平方数list" data-toc-modified-id="3.1-生成一个1~10的平方数list-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>3.1 生成一个1~10的平方数list</a></div><div class="lev2 toc-item"><a href="#4-生成器" data-toc-modified-id="4-生成器-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>4 生成器</a></div><div class="lev3 toc-item"><a href="#4.1-create-a-generater-g:-g-=-(x-*-x-for-x-in-range(10))" data-toc-modified-id="4.1-create-a-generater-g:-g-=-(x-*-x-for-x-in-range(10))-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>4.1 create a generater g: g = (x * x for x in range(10))</a></div><div class="lev3 toc-item"><a href="#4.2-生成器可以被next()函数调用，不断返回下一个值" data-toc-modified-id="4.2-生成器可以被next()函数调用，不断返回下一个值-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>4.2 生成器可以被next()函数调用，不断返回下一个值</a></div><div class="lev3 toc-item"><a href="#4.3-当next()调用完了，没有下一个值，就会终止。" data-toc-modified-id="4.3-当next()调用完了，没有下一个值，就会终止。-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>4.3 当next()调用完了，没有下一个值，就会终止。</a></div><div class="lev3 toc-item"><a href="#4.4-因为他也是可迭代对象，因此可以用for迭代" data-toc-modified-id="4.4-因为他也是可迭代对象，因此可以用for迭代-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>4.4 因为他也是可迭代对象，因此可以用for迭代</a></div><div class="lev3 toc-item"><a href="#4.5-Python的for循环本质上就是通过不断调用next()函数实现的" data-toc-modified-id="4.5-Python的for循环本质上就是通过不断调用next()函数实现的-145"><span class="toc-item-num">1.4.5&nbsp;&nbsp;</span>4.5 Python的for循环本质上就是通过不断调用next()函数实现的</a></div>

# # list, tuple, dict and set -- 列表和元组

# ## 1 list

# ### 1.1 print list classmate, and get the length of it by using len()

# In[19]:

classmates = ['Michael', 'Bob', 'Tracy']


# In[20]:

print('classmate:', classmates)
print('there are %d member in classmates\n' % len(classmates))


# ### 1.2 用索引来访问list中每一个位置的元素，记得索引是从0开始的

# In[21]:

print('NO.0:%s, NO.1:%s, NO.2:%s' % (classmates[0], classmates[1], classmates[2]))


# ### 1.3 用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个

# In[22]:

print(classmates[-1])
print(classmates[-2])
print(classmates[-3])


# ### 1.4 list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾

# In[23]:

print('before append Adam: ', classmates)
classmates.append('Adam')
print('after append Adam: ',classmates)


# ### 1.5 把元素插入到指定的位置，比如索引号为1的位置

# In[24]:

print('before insert Jack to the [1] position: ', classmates)
classmates.insert(1, 'Jack')
print('after insert Jack to the [1] position: ', classmates)


# ### 1.6 要删除list末尾的元素，用pop()方法

# In[25]:

print('pop the last member \'%s\'' % classmates.pop())
print(classmates)


# ### 1.7 要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数

# In[26]:

i = 1
print('pop the NO.%d member \'%s\'' % (1+i, classmates.pop(i)))
print(classmates)


# ## 2 dict

# ### 2.1 迭代

# #### 2.1.1 key迭代，因为dict的key存储方式不是顺序的，而是hash，所以输出并不是顺序的

# In[30]:

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# In[31]:

print('print dict d:', d)


# In[32]:

for k in d:
    print(k, d[k])


# #### 2.1.2 value迭代

# In[33]:

for v in d.values():
    print(v)


# #### 2.1.3 key,value同时迭代

# In[34]:

for k, v in d.items():
    print(k, v)


# ##  3 列表生成式

# ### 3.1 生成一个1~10的平方数list

# In[35]:

print([x*x for x in range(1, 11)])


# ## 4 生成器

# ### 4.1 create a generater g: g = (x * x for x in range(10))

# In[36]:

g = (x * x for x in range(10))


# ### 4.2 生成器可以被next()函数调用，不断返回下一个值

# In[37]:

print(next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g))


# ### 4.3 当next()调用完了，没有下一个值，就会终止。

# In[39]:

for i in g:
    print(i)


# ### 4.4 因为他也是可迭代对象，因此可以用for迭代

# In[40]:

g = (x * x for x in range(10))


# In[41]:

for i in g:
    print(i)


# > 
# * 凡是可作用于for循环的对象都是Iterable（可迭代）类型
# * 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列
# * 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

# ### 4.5 Python的for循环本质上就是通过不断调用next()函数实现的

# In[42]:

for x in [1, 2, 3, 4, 5]:
    print(x)


# 上式完全等价于

# In[43]:

it = iter([1, 2, 3, 4, 5])  # 首先获得Iterator对象
while True:  # 循环
    try:
        x = next(it)  # 获得下一个值:
        print(x)
    except StopIteration:  # 遇到StopIteration就退出循环
        break

