#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list and tuple, 列表和元组
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print('there are %d member in classmates' % len(classmates))

#用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0], classmates[1], classmates[2])

#用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#list是一个可变的有序表，所以，可以用append函数往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

#把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

#要删除list末尾的元素，用pop()方法
print('pop the last member \'%s\'' % classmates.pop())
print(classmates)
#要删除指定位置(索引号)的元素，用pop(i)方法，这时候是从头开始数
i = 1
print('pop the NO.%d member \'%s\'' % (1+i, classmates.pop(i)))
print(classmates)

