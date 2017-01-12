#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list, tuple, dict and set -- 列表和元组
print('---------------------------------')
print('list, tuple, dict and set -- 列表和元组')
print('---------------------------------')


classmates = ['Michael', 'Bob', 'Tracy']
print('# print list classmate\nclassmate:', classmates)
print('there are %d member in classmates\n' % len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print('# 用索引来访问list中每一个位置的元素，记得索引是从0开始的')
print('NO.0:%s, NO.1:%s, NO.2:%s' % (classmates[0], classmates[1], classmates[2]))

# 用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个
print('\n# 用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个')
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾
print('\n# list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾，append(Adam)')
classmates.append('Adam')
print(classmates)

# 把元素插入到指定的位置，比如索引号为1的位置
print('\n# 把元素插入到指定的位置，比如索引号为1的位置，插入Jack')
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
print('\n# 要删除list末尾的元素，用pop()方法')
print('pop the last member \'%s\'' % classmates.pop())
print(classmates)

# 要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数
print('\n# 要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数')
i = 1
print('pop the NO.%d member \'%s\'' % (1+i, classmates.pop(i)))
print(classmates)

# 迭代
print('\n---------------------------------')
print('迭代')
print('---------------------------------')

# 迭代dict的key，因为dict的key存储方式不是顺序的，而是hash，所以输出并不是顺序的
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('print dict d:', d)

# key迭代
print('\n# key迭代，因为dict的key存储方式不是顺序的，而是hash，所以输出并不是顺序的')
for k in d:
    print(k, d[k])
# value迭代
print('\n# value迭代')
for v in d.values():
    print(v)
# key,value同时迭代
print('\n# key,value同时迭代')
for k, v in d.items():
    print(k, v)

# 列表生成式
print('\n---------------------------------')
print('列表生成式')
print('---------------------------------')

# 生成一个1~10的平方数list
print('# 生成一个1~10的平方数list')
print([x*x for x in range(1, 11)])

# 生成器
print('\n---------------------------------')
print('# 生成器')
print('---------------------------------')

print('create a generater g: g = (x * x for x in range(10))')
g = (x * x for x in range(10))

# 生成器可以被next()函数调用，不断返回下一个值
print('\n# 生成器可以被next()函数调用，不断返回下一个值')
print(next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g))

# 当next()调用完了，没有下一个值，就会终止。因为他也是可迭代对象，因此可以用for迭代
print('\n# 当next()调用完了，没有下一个值，就会终止。因为他也是可迭代对象，因此可以用for迭代')
g = (x * x for x in range(10))
for i in g:
    print(i)
'''
# 凡是可作用于for循环的对象都是Iterable（可迭代）类型
# 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
'''

# Python的for循环本质上就是通过不断调用next()函数实现的：
print('\n# Python的for循环本质上就是通过不断调用next()函数实现的：')
print('for x in [1, 2, 3, 4, 5]:')
print('    print(x)')
for x in [1, 2, 3, 4, 5]:
    print(x)

# 上式完全等价于
print('\n# 上式完全等价于:')
print('it = iter([1, 2, 3, 4, 5])  # 首先获得Iterator对象')
print('while True:  # 循环')
print('    try:')
print('x = next(it)  # 获得下一个值:\n        print(x)\n    except StopIteration:  # 遇到StopIteration就退出循环\n        break')
it = iter([1, 2, 3, 4, 5])  # 首先获得Iterator对象
while True:  # 循环
    try:
        x = next(it)  # 获得下一个值:
        print(x)
    except StopIteration:  # 遇到StopIteration就退出循环
        break