
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#1-function-test----函数测试" data-toc-modified-id="1-function-test----函数测试-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>1 function test -- 函数测试</a></div><div class="lev2 toc-item"><a href="#1.1-函数返回多个值" data-toc-modified-id="1.1-函数返回多个值-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>1.1 函数返回多个值</a></div><div class="lev2 toc-item"><a href="#1.2-函数作为生成器" data-toc-modified-id="1.2-函数作为生成器-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>1.2 函数作为生成器</a></div><div class="lev3 toc-item"><a href="#1.2.1-普通函数打印斐波那契数列" data-toc-modified-id="1.2.1-普通函数打印斐波那契数列-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>1.2.1 普通函数打印斐波那契数列</a></div><div class="lev3 toc-item"><a href="#1.2.2-函数生成器打印斐波那契数列，添加关键字yield" data-toc-modified-id="1.2.2-函数生成器打印斐波那契数列，添加关键字yield-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>1.2.2 函数生成器打印斐波那契数列，添加关键字yield</a></div><div class="lev3 toc-item"><a href="#1.2.3-捕获StopIteration错误，拿返回值" data-toc-modified-id="1.2.3-捕获StopIteration错误，拿返回值-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>1.2.3 捕获StopIteration错误，拿返回值</a></div><div class="lev3 toc-item"><a href="#1.2.4-测试-杨辉三角，用生成器实现，打印如下输出：" data-toc-modified-id="1.2.4-测试-杨辉三角，用生成器实现，打印如下输出：-124"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>1.2.4 测试-杨辉三角，用生成器实现，打印如下输出：</a></div><div class="lev2 toc-item"><a href="#1.3-高阶函数" data-toc-modified-id="1.3-高阶函数-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>1.3 高阶函数</a></div><div class="lev3 toc-item"><a href="#1.3.1-变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数" data-toc-modified-id="1.3.1-变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>1.3.1 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数</a></div><div class="lev3 toc-item"><a href="#1.3.2-改进-可变参数" data-toc-modified-id="1.3.2-改进-可变参数-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>1.3.2 改进-可变参数</a></div><div class="lev2 toc-item"><a href="#1.4-map-reduce" data-toc-modified-id="1.4-map-reduce-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>1.4 map-reduce</a></div><div class="lev3 toc-item"><a href="#1.4.1-map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator" data-toc-modified-id="1.4.1-map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>1.4.1 map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator</a></div><div class="lev3 toc-item"><a href="#1.4.2-reduce把一个函数作用在一个序列[x1,-x2,-x3,-...]上" data-toc-modified-id="1.4.2-reduce把一个函数作用在一个序列[x1,-x2,-x3,-...]上-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>1.4.2 reduce把一个函数作用在一个序列[x1, x2, x3, ...]上</a></div><div class="lev3 toc-item"><a href="#1.4.3-改进-因为str也是序列，配合map写一个转换str为int的函数：" data-toc-modified-id="1.4.3-改进-因为str也是序列，配合map写一个转换str为int的函数：-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>1.4.3 改进-因为str也是序列，配合map写一个转换str为int的函数：</a></div><div class="lev3 toc-item"><a href="#1.4.4-测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。" data-toc-modified-id="1.4.4-测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>1.4.4 测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。</a></div><div class="lev3 toc-item"><a href="#1.4.5-测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：" data-toc-modified-id="1.4.5-测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：-145"><span class="toc-item-num">1.4.5&nbsp;&nbsp;</span>1.4.5 测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：</a></div><div class="lev3 toc-item"><a href="#1.4.6-测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：" data-toc-modified-id="1.4.6-测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：-146"><span class="toc-item-num">1.4.6&nbsp;&nbsp;</span>1.4.6 测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：</a></div><div class="lev2 toc-item"><a href="#1.5-filter过滤器" data-toc-modified-id="1.5-filter过滤器-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>1.5 filter过滤器</a></div><div class="lev3 toc-item"><a href="#1.5.1-利用filter在一个list里面删除偶数，保留奇数" data-toc-modified-id="1.5.1-利用filter在一个list里面删除偶数，保留奇数-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>1.5.1 利用filter在一个list里面删除偶数，保留奇数</a></div><div class="lev3 toc-item"><a href="#1.5.2-测试-利用filter求素数" data-toc-modified-id="1.5.2-测试-利用filter求素数-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>1.5.2 测试-利用filter求素数</a></div><div class="lev3 toc-item"><a href="#1.5.3-测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：" data-toc-modified-id="1.5.3-测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>1.5.3 测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：</a></div><div class="lev2 toc-item"><a href="#1.6-sorted函数" data-toc-modified-id="1.6-sorted函数-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>1.6 sorted函数</a></div><div class="lev3 toc-item"><a href="#1.6.1-测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：" data-toc-modified-id="1.6.1-测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>1.6.1 测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：</a></div>

# # 1 function test -- 函数测试

# ## 1.1 函数返回多个值

# In[1]:

import math


# In[2]:

def move(x, y, step, angle = 0):
    mx = x + step * math.cos(angle)
    my = y - step * math.sin(angle)
    return mx, my


# In[3]:

x, y = move(100, 100, 60, math.pi/6)
print(x, y)


# 但其实这只是一种假象，Python函数返回的仍然是单一值,一个元组

# In[4]:

r = move(100, 100, 60, math.pi / 6)
print(r)


# > 
# * 返回值是一个tuple. 在语法上，返回一个tuple可以省略括号
# * 而多个变量可以同时接收一个tuple，按位置赋给对应的值
# * 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。。

# ## 1.2 函数作为生成器

# ### 1.2.1 普通函数打印斐波那契数列

# In[5]:

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'


# In[6]:

fib(10)


# ### 1.2.2 函数生成器打印斐波那契数列，添加关键字yield

# In[13]:

def _fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield (b) # yield
        a, b = b, a+b
        n = n+1
    return 'I\'m return value'


# In[14]:

f = _fib(10)


# In[15]:

for x in f:
    print(x)


# > 
# * 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# * generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# * 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# * 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
# * 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# * 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

# ### 1.2.3 捕获StopIteration错误，拿返回值

# In[16]:

f = _fib(10)


# In[17]:

while True:
    try:
        x = next(f)
        print('f:', x)
    except StopIteration as e:
        print('return value:', e.value)
        break


# ### 1.2.4 测试-杨辉三角，用生成器实现，打印如下输出：
# > 
# [1]
# >
# [1, 1]
# >
# [1, 2, 1]
# >
# [1, 3, 3, 1]
# >
# [1, 4, 6, 4, 1]
# >
# [1, 5, 10, 10, 5, 1]
# >
# [1, 6, 15, 20, 15, 6, 1]
# >
# [1, 7, 21, 35, 35, 21, 7, 1]
# >
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# >
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

# In[18]:

def triangles():
    L = [1]
    a = 1
    while True:
        if a == 1:
            yield L
        else:
            L = [L[i-1] + L[i] for i in range(1, a-1)]  # 如果range后面的参数小于等于前面的参数，则为空集
            L = [1] + L + [1]
            yield L
        a += 1


# In[19]:

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


# > 
# * 凡是可作用于for循环的对象都是Iterable（可迭代）类型
# * 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列
# * 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

# ## 1.3 高阶函数

# ### 1.3.1 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

# In[20]:

def add(x, y, f):
    return f(x) + f(y)


# In[22]:

print('|-5| + |6| = ', add(-5, 6, abs))


# ### 1.3.2 改进-可变参数

# In[23]:

def ChangableParameterFunction(x = [], *f):
    print([_f(_x) for _x in x for _f in f])


# In[24]:

ChangableParameterFunction([1, 4, 9, 16], math.sqrt , abs)


# ## 1.4 map-reduce

# ### 1.4.1 map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator

# In[25]:

def f(x):
    return x*x


# In[26]:

print(list(map(f, [1, 2, 3, 4])))


# ### 1.4.2 reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# * 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# In[27]:

from functools import reduce


# In[28]:

def f(x, y):
    return x*10 + y


# In[29]:

print(reduce(f, [1, 3, 5, 7, 9]))


# > 上面将单个数1,3,5,7,9变成13579

# ### 1.4.3 改进-因为str也是序列，配合map写一个转换str为int的函数：

# In[30]:

def f(x, y):
    return x*10 +y


# In[31]:

def char2num(s):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d[s]


# In[32]:

reduce(f, map(char2num, '13579'))


# * 再改进-整理成一个函数：

# In[33]:

def str2int(s):
    def f(x, y):
        return x * 10 + y
    def char2num(s):
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return d[s]
    return reduce(f, map(char2num, s))


# In[34]:

print(str2int('13579'))


# ### 1.4.4 测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

# In[35]:

def normalize(name):
    return name[0].upper() + name[1:].lower()


# In[36]:

print(list(map(normalize, ['adam', 'LISA', 'barT'])))


# ### 1.4.5 测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# In[37]:

def prod(l = []):
    def mul(x, y):
        return x * y
    return reduce(mul, l)


# In[38]:

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))


# ### 1.4.6 测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# In[39]:

def str2float(s):
    def char2num(s):
        cnt = 0
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return d[s]
    def turn2int(x, y):
        return x * 10 + y
    def turn2float(x, y):
        return x/10 + y
    return reduce(turn2int, map(char2num, s[:s.find('.')])) + reduce(turn2float, map(char2num, s[::-1][:s.find('.')])) / 10


# In[41]:

print(type(str2float('123.456')), str2float('123.456'))


# ## 1.5 filter过滤器
# * 和map()类似，filter()也接收一个函数和一个序列。
# * 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# ### 1.5.1 利用filter在一个list里面删除偶数，保留奇数

# In[42]:

def remainOdd(x):
    return x%2 == 1


# In[43]:

print('[1, 2, 3, 4, 5, 6]-->', list(filter(remainOdd, [1, 2, 3, 4, 5, 6])))


# ### 1.5.2 测试-利用filter求素数
# 
# > 
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# * 首先，列出从2开始的所有自然数，构造一个序列：2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# * 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：3, 5, 7, 9, 11, 13, 15, 17, 19, ...
# * 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：5, 7, 11, 13, 17, 19, ...
# * 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：, ...
# * 不断筛下去，就可以得到所有的素数。

# * 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：注意这是一个生成器，并且是一个无限序列。

# In[44]:

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# * 最后，定义一个生成器，不断返回下一个素数：这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

# In[46]:

def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    # it_0:[3, 5, 7, 9, 11, 13, 15, 17, 19, ...]
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(lambda x : x%n > 0, it)  # 构造新序列
        # it_1:[3(n), 5, 7, <9>, 11, 13, <15>, 17, 19, ...]
        # it_2:[3, 5(n), 7, <9>, 11, 13, <15>, 17, 19, <21>, 23, <25>, <27>, 29, ...]
        # ......
    return 'done'


# * 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# In[47]:

for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# ### 1.5.3 测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

# In[48]:

output = filter(lambda x: x > 10 and str(x) == str(x)[::-1], range(1, 1000))


# In[49]:

print(list(output))


# ## 1.6 sorted函数
# * sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

# In[50]:

print(sorted([36, 5, -12, 9, -21], key=abs))


# ### 1.6.1 测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：

# * 以名字排序

# In[51]:

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('L =',L)


# In[52]:

def by_name(n):
    return n[0]


# In[53]:

print(sorted(L, key=by_name))


# * 再按成绩从高到低排序：

# In[54]:

def by_score(s):
    return s[1]


# In[55]:

print(sorted(L, key=by_score))

