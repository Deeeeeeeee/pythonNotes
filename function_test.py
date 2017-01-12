# -*- coding: utf-8 -*-

print('---------------------------------')
print('function test -- 函数测试')
print('---------------------------------')

# 函数返回多个值
print('# 函数返回多个值')
import math
def move(x, y, step, angle = 0):
    mx = x + step * math.cos(angle)
    my = y - step * math.sin(angle)
    return mx, my

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
print('\n# 但其实这只是一种假象，Python函数返回的仍然是单一值：一个元组')
r = move(100, 100, 60, math.pi / 6)
print(r)
'''
# 返回值是一个tuple. 在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。。
'''
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

# 函数作为生成器
print('\n---------------------------------')
print('函数作为生成器')
print('---------------------------------')

# 普通函数打印斐波那契数列
print('# 普通函数打印斐波那契数列')
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'
fib(10)

print('\n# 函数生成器打印斐波那契数列，添加关键字yield')
# 函数生成器打印斐波那契数列，添加关键字yield
def _fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield (b)
        a, b = b, a+b
        n = n+1
    return 'done'
f = _fib(10)
for x in f:
    print(x)
'''
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
'''
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
print('\n# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：')
f = _fib(10)
while True:
    try:
        x = next(f)
        print('f:', x)
    except StopIteration as e:
        print('return value:', e.value)
        break

# 测试-杨辉三角，用生成器实现，打印如下输出：
print('\n# 测试-杨辉三角，用生成器实现，打印如下输出：')
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
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
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# range测试
print('\n# range测试')
l = [i for i in range(1, 1)]
print(l)

'''
# 凡是可作用于for循环的对象都是Iterable（可迭代）类型
# 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
'''
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# 高阶函数
print('\n---------------------------------')
print('高阶函数')
print('---------------------------------')

# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
print('# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数')
print('# |-5| + |6|:')
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

# 改进-可变参数
print('\n# 改进-可变参数')
def ChangableParameterFunction(x = [], *f):
    print([_f(_x) for _x in x for _f in f])
ChangableParameterFunction([1, 4, 9, 16], math.sqrt , abs)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#  map-reduce
print('\n---------------------------------')
print('map-reduce')
print('---------------------------------')

# map-reduce就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator
print('# map-reduce就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator\n# 输出[1,2,3,4]的平方:')
def f(x):
    return x*x
print(list(map(f, [1, 2, 3, 4])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print('\n# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上\n# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是\n# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)')

# 下面将单个数1,3,5,7,9变成13579
print('\n# 下面将连续单个数1,3,5,7,9变成13579')
from functools import reduce
def f(x, y):
    return x*10 + y
print(reduce(f, [1, 3, 5, 7, 9]))

# 改进-因为str也是序列，配合map写一个转换str为int的函数：
print('\n# 改进-因为str也是序列，配合map写一个转换str为int的函数：')
def f(x, y):
    return x*10 +y
def char2num(s):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d[s]
reduce(f, map(char2num, '13579'))

# 再改进-整理成一个函数：
print('\n# 再改进-整理成一个函数：')
def str2int(s):
    def f(x, y):
        return x * 10 + y
    def char2num(s):
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return d[s]
    return reduce(f, map(char2num, s))
print(str2int('13579'))

# 测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
print('\n# 测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字.\n# 输入：[\'adam\', \'LISA\', \'barT\']，输出：[\'Adam\', \'Lisa\', \'Bart\']')
def normalize(name):
    return name[0].upper() + name[1:].lower()
print(list(map(normalize, ['adam', 'LISA', 'barT'])))

# 测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
print('\n# 测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：')
def prod(l = []):
    def mul(x, y):
        return x * y
    return reduce(mul, l)
print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))

# 测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
print('\n# 测试-利用map和reduce编写一个str2float函数，把字符串\'123.456\'转换成浮点数123.456：')
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
print('(str)\'123.456\'--> (float)', str2float('123.456'))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# filter
print('\n---------------------------------')
print('filter')
print('---------------------------------')

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
print('# 和map()类似，filter()也接收一个函数和一个序列。\n# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。\n')

# 利用filter在一个list里面删除偶数，保留奇数
print('# 利用filter在一个list里面删除偶数，保留奇数')
def remainOdd(x):
    return x%2 == 1
print('[1, 2, 3, 4, 5, 6]-->', list(filter(remainOdd, [1, 2, 3, 4, 5, 6])))

print('# 测试-利用filter求素数')
# 利用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 5, 7, 9, 11, 13, 15, 17, 19, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 7, 11, 13, 17, 19, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# , ...
# 不断筛下去，就可以得到所有的素数。

# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 然后定义一个筛选函数：对于每一个x，能被n整除就筛掉，不能就留下
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    # it_0:[3, 5, 7, 9, 11, 13, 15, 17, 19, ...]
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列
        # it_1:[3(n), 5, 7, <9>, 11, 13, <15>, 17, 19, ...]
        # it_2:[3, 5(n), 7, <9>, 11, 13, <15>, 17, 19, <21>, 23, <25>, <27>, 29, ...]
        # ......
    return 'done'
# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

# 测试-由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
print('\n# 测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：')
output = filter(lambda x: x > 10 and str(x) == str(x)[::-1], range(1, 1000))
print(list(output))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

print('\n---------------------------------')
print('sorted')
print('---------------------------------')

# sorted()函数
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print('# sorted()函数\n# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：')
print(sorted([36, 5, -12, 9, -21], key=abs))

# 测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：
print('\n# 测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：')
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('L =',L)
def by_name(n):
    return n[0]
print(sorted(L, key=by_name))

# 再按成绩从高到低排序：
print('# 再按成绩从高到低排序：')
def by_score(s):
    return s[1]
print(sorted(L, key=by_score))