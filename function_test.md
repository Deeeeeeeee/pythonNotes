
# Table of Contents
 <p><div class="lev1 toc-item"><a href="#1-function-test----函数测试" data-toc-modified-id="1-function-test----函数测试-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>1 function test -- 函数测试</a></div><div class="lev2 toc-item"><a href="#1.1-函数返回多个值" data-toc-modified-id="1.1-函数返回多个值-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>1.1 函数返回多个值</a></div><div class="lev2 toc-item"><a href="#1.2-函数作为生成器" data-toc-modified-id="1.2-函数作为生成器-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>1.2 函数作为生成器</a></div><div class="lev3 toc-item"><a href="#1.2.1-普通函数打印斐波那契数列" data-toc-modified-id="1.2.1-普通函数打印斐波那契数列-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>1.2.1 普通函数打印斐波那契数列</a></div><div class="lev3 toc-item"><a href="#1.2.2-函数生成器打印斐波那契数列，添加关键字yield" data-toc-modified-id="1.2.2-函数生成器打印斐波那契数列，添加关键字yield-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>1.2.2 函数生成器打印斐波那契数列，添加关键字yield</a></div><div class="lev3 toc-item"><a href="#1.2.3-捕获StopIteration错误，拿返回值" data-toc-modified-id="1.2.3-捕获StopIteration错误，拿返回值-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>1.2.3 捕获StopIteration错误，拿返回值</a></div><div class="lev3 toc-item"><a href="#1.2.4-测试-杨辉三角，用生成器实现，打印如下输出：" data-toc-modified-id="1.2.4-测试-杨辉三角，用生成器实现，打印如下输出：-124"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>1.2.4 测试-杨辉三角，用生成器实现，打印如下输出：</a></div><div class="lev2 toc-item"><a href="#1.3-高阶函数" data-toc-modified-id="1.3-高阶函数-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>1.3 高阶函数</a></div><div class="lev3 toc-item"><a href="#1.3.1-变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数" data-toc-modified-id="1.3.1-变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>1.3.1 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数</a></div><div class="lev3 toc-item"><a href="#1.3.2-改进-可变参数" data-toc-modified-id="1.3.2-改进-可变参数-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>1.3.2 改进-可变参数</a></div><div class="lev2 toc-item"><a href="#1.4-map-reduce" data-toc-modified-id="1.4-map-reduce-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>1.4 map-reduce</a></div><div class="lev3 toc-item"><a href="#1.4.1-map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator" data-toc-modified-id="1.4.1-map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>1.4.1 map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator</a></div><div class="lev3 toc-item"><a href="#1.4.2-reduce把一个函数作用在一个序列[x1,-x2,-x3,-...]上" data-toc-modified-id="1.4.2-reduce把一个函数作用在一个序列[x1,-x2,-x3,-...]上-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>1.4.2 reduce把一个函数作用在一个序列[x1, x2, x3, ...]上</a></div><div class="lev3 toc-item"><a href="#1.4.3-改进-因为str也是序列，配合map写一个转换str为int的函数：" data-toc-modified-id="1.4.3-改进-因为str也是序列，配合map写一个转换str为int的函数：-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>1.4.3 改进-因为str也是序列，配合map写一个转换str为int的函数：</a></div><div class="lev3 toc-item"><a href="#1.4.4-测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。" data-toc-modified-id="1.4.4-测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>1.4.4 测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。</a></div><div class="lev3 toc-item"><a href="#1.4.5-测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：" data-toc-modified-id="1.4.5-测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：-145"><span class="toc-item-num">1.4.5&nbsp;&nbsp;</span>1.4.5 测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：</a></div><div class="lev3 toc-item"><a href="#1.4.6-测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：" data-toc-modified-id="1.4.6-测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：-146"><span class="toc-item-num">1.4.6&nbsp;&nbsp;</span>1.4.6 测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：</a></div><div class="lev2 toc-item"><a href="#1.5-filter过滤器" data-toc-modified-id="1.5-filter过滤器-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>1.5 filter过滤器</a></div><div class="lev3 toc-item"><a href="#1.5.1-利用filter在一个list里面删除偶数，保留奇数" data-toc-modified-id="1.5.1-利用filter在一个list里面删除偶数，保留奇数-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>1.5.1 利用filter在一个list里面删除偶数，保留奇数</a></div><div class="lev3 toc-item"><a href="#1.5.2-测试-利用filter求素数" data-toc-modified-id="1.5.2-测试-利用filter求素数-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>1.5.2 测试-利用filter求素数</a></div><div class="lev3 toc-item"><a href="#1.5.3-测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：" data-toc-modified-id="1.5.3-测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>1.5.3 测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：</a></div><div class="lev2 toc-item"><a href="#1.6-sorted函数" data-toc-modified-id="1.6-sorted函数-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>1.6 sorted函数</a></div><div class="lev3 toc-item"><a href="#1.6.1-测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：" data-toc-modified-id="1.6.1-测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>1.6.1 测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：</a></div>

# 1 function test -- 函数测试

## 1.1 函数返回多个值


```python
import math
```


```python
def move(x, y, step, angle = 0):
    mx = x + step * math.cos(angle)
    my = y - step * math.sin(angle)
    return mx, my
```


```python
x, y = move(100, 100, 60, math.pi/6)
print(x, y)
```

    151.96152422706632 70.0
    

但其实这只是一种假象，Python函数返回的仍然是单一值,一个元组


```python
r = move(100, 100, 60, math.pi / 6)
print(r)
```

    (151.96152422706632, 70.0)
    

> 
* 返回值是一个tuple. 在语法上，返回一个tuple可以省略括号
* 而多个变量可以同时接收一个tuple，按位置赋给对应的值
* 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。。

## 1.2 函数作为生成器

### 1.2.1 普通函数打印斐波那契数列


```python
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'
```


```python
fib(10)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    




    'done'



### 1.2.2 函数生成器打印斐波那契数列，添加关键字yield


```python
def _fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield (b) # yield
        a, b = b, a+b
        n = n+1
    return 'I\'m return value'
```


```python
f = _fib(10)
```


```python
for x in f:
    print(x)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    

> 
* 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
* generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
* 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
* 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
* 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
* 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

### 1.2.3 捕获StopIteration错误，拿返回值


```python
f = _fib(10)
```


```python
while True:
    try:
        x = next(f)
        print('f:', x)
    except StopIteration as e:
        print('return value:', e.value)
        break
```

    f: 1
    f: 1
    f: 2
    f: 3
    f: 5
    f: 8
    f: 13
    f: 21
    f: 34
    f: 55
    return value: I'm return value
    

### 1.2.4 测试-杨辉三角，用生成器实现，打印如下输出：
> 
[1]
>
[1, 1]
>
[1, 2, 1]
>
[1, 3, 3, 1]
>
[1, 4, 6, 4, 1]
>
[1, 5, 10, 10, 5, 1]
>
[1, 6, 15, 20, 15, 6, 1]
>
[1, 7, 21, 35, 35, 21, 7, 1]
>
[1, 8, 28, 56, 70, 56, 28, 8, 1]
>
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


```python
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
```


```python
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
```

    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    

> 
* 凡是可作用于for循环的对象都是Iterable（可迭代）类型
* 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列
* 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

## 1.3 高阶函数

### 1.3.1 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数


```python
def add(x, y, f):
    return f(x) + f(y)
```


```python
print('|-5| + |6| = ', add(-5, 6, abs))
```

    |-5| + |6| =  11
    

### 1.3.2 改进-可变参数


```python
def ChangableParameterFunction(x = [], *f):
    print([_f(_x) for _x in x for _f in f])
```


```python
ChangableParameterFunction([1, 4, 9, 16], math.sqrt , abs)
```

    [1.0, 1, 2.0, 4, 3.0, 9, 4.0, 16]
    

## 1.4 map-reduce

### 1.4.1 map就像上面的可变参数实现那样，将函数作为参数传递，将函数作用在一个iterator如List上，返回一个iterator


```python
def f(x):
    return x*x
```


```python
print(list(map(f, [1, 2, 3, 4])))
```

    [1, 4, 9, 16]
    

### 1.4.2 reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
* 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


```python
from functools import reduce
```


```python
def f(x, y):
    return x*10 + y
```


```python
print(reduce(f, [1, 3, 5, 7, 9]))
```

    13579
    

> 上面将单个数1,3,5,7,9变成13579

### 1.4.3 改进-因为str也是序列，配合map写一个转换str为int的函数：


```python
def f(x, y):
    return x*10 +y
```


```python
def char2num(s):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d[s]
```


```python
reduce(f, map(char2num, '13579'))
```




    13579



* 再改进-整理成一个函数：


```python
def str2int(s):
    def f(x, y):
        return x * 10 + y
    def char2num(s):
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return d[s]
    return reduce(f, map(char2num, s))
```


```python
print(str2int('13579'))
```

    13579
    

### 1.4.4 测试-利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。


```python
def normalize(name):
    return name[0].upper() + name[1:].lower()
```


```python
print(list(map(normalize, ['adam', 'LISA', 'barT'])))
```

    ['Adam', 'Lisa', 'Bart']
    

### 1.4.5 测试-Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：


```python
def prod(l = []):
    def mul(x, y):
        return x * y
    return reduce(mul, l)
```


```python
print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
```

    3 * 5 * 7 * 9 =  945
    

### 1.4.6 测试-利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：


```python
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
```


```python
print(type(str2float('123.456')), str2float('123.456'))
```

    <class 'float'> 123.456
    

## 1.5 filter过滤器
* 和map()类似，filter()也接收一个函数和一个序列。
* 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

### 1.5.1 利用filter在一个list里面删除偶数，保留奇数


```python
def remainOdd(x):
    return x%2 == 1
```


```python
print('[1, 2, 3, 4, 5, 6]-->', list(filter(remainOdd, [1, 2, 3, 4, 5, 6])))
```

    [1, 2, 3, 4, 5, 6]--> [1, 3, 5]
    

### 1.5.2 测试-利用filter求素数

> 
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
* 首先，列出从2开始的所有自然数，构造一个序列：2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
* 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：3, 5, 7, 9, 11, 13, 15, 17, 19, ...
* 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：5, 7, 11, 13, 17, 19, ...
* 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：, ...
* 不断筛下去，就可以得到所有的素数。

* 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：注意这是一个生成器，并且是一个无限序列。


```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
```

* 最后，定义一个生成器，不断返回下一个素数：这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。


```python
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
```

* 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：


```python
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

    2
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    23
    25
    27
    29
    31
    33
    35
    37
    39
    41
    43
    45
    47
    49
    51
    53
    55
    57
    59
    61
    63
    65
    67
    69
    71
    73
    75
    77
    79
    81
    83
    85
    87
    89
    91
    93
    95
    97
    99
    101
    103
    105
    107
    109
    111
    113
    115
    117
    119
    121
    123
    125
    127
    129
    131
    133
    135
    137
    139
    141
    143
    145
    147
    149
    151
    153
    155
    157
    159
    161
    163
    165
    167
    169
    171
    173
    175
    177
    179
    181
    183
    185
    187
    189
    191
    193
    195
    197
    199
    201
    203
    205
    207
    209
    211
    213
    215
    217
    219
    221
    223
    225
    227
    229
    231
    233
    235
    237
    239
    241
    243
    245
    247
    249
    251
    253
    255
    257
    259
    261
    263
    265
    267
    269
    271
    273
    275
    277
    279
    281
    283
    285
    287
    289
    291
    293
    295
    297
    299
    301
    303
    305
    307
    309
    311
    313
    315
    317
    319
    321
    323
    325
    327
    329
    331
    333
    335
    337
    339
    341
    343
    345
    347
    349
    351
    353
    355
    357
    359
    361
    363
    365
    367
    369
    371
    373
    375
    377
    379
    381
    383
    385
    387
    389
    391
    393
    395
    397
    399
    401
    403
    405
    407
    409
    411
    413
    415
    417
    419
    421
    423
    425
    427
    429
    431
    433
    435
    437
    439
    441
    443
    445
    447
    449
    451
    453
    455
    457
    459
    461
    463
    465
    467
    469
    471
    473
    475
    477
    479
    481
    483
    485
    487
    489
    491
    493
    495
    497
    499
    501
    503
    505
    507
    509
    511
    513
    515
    517
    519
    521
    523
    525
    527
    529
    531
    533
    535
    537
    539
    541
    543
    545
    547
    549
    551
    553
    555
    557
    559
    561
    563
    565
    567
    569
    571
    573
    575
    577
    579
    581
    583
    585
    587
    589
    591
    593
    595
    597
    599
    601
    603
    605
    607
    609
    611
    613
    615
    617
    619
    621
    623
    625
    627
    629
    631
    633
    635
    637
    639
    641
    643
    645
    647
    649
    651
    653
    655
    657
    659
    661
    663
    665
    667
    669
    671
    673
    675
    677
    679
    681
    683
    685
    687
    689
    691
    693
    695
    697
    699
    701
    703
    705
    707
    709
    711
    713
    715
    717
    719
    721
    723
    725
    727
    729
    731
    733
    735
    737
    739
    741
    743
    745
    747
    749
    751
    753
    755
    757
    759
    761
    763
    765
    767
    769
    771
    773
    775
    777
    779
    781
    783
    785
    787
    789
    791
    793
    795
    797
    799
    801
    803
    805
    807
    809
    811
    813
    815
    817
    819
    821
    823
    825
    827
    829
    831
    833
    835
    837
    839
    841
    843
    845
    847
    849
    851
    853
    855
    857
    859
    861
    863
    865
    867
    869
    871
    873
    875
    877
    879
    881
    883
    885
    887
    889
    891
    893
    895
    897
    899
    901
    903
    905
    907
    909
    911
    913
    915
    917
    919
    921
    923
    925
    927
    929
    931
    933
    935
    937
    939
    941
    943
    945
    947
    949
    951
    953
    955
    957
    959
    961
    963
    965
    967
    969
    971
    973
    975
    977
    979
    981
    983
    985
    987
    989
    991
    993
    995
    997
    999
    

### 1.5.3 测试-回文数，回文数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：


```python
output = filter(lambda x: x > 10 and str(x) == str(x)[::-1], range(1, 1000))
```


```python
print(list(output))
```

    [11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]
    

## 1.6 sorted函数
* sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：


```python
print(sorted([36, 5, -12, 9, -21], key=abs))
```

    [5, 9, -12, -21, 36]
    

### 1.6.1 测试-假设我们用一组tuple表示学生名字和成绩，请用sorted()对下述列表分别按名字排序：

* 以名字排序


```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('L =',L)
```

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    


```python
def by_name(n):
    return n[0]
```


```python
print(sorted(L, key=by_name))
```

    [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
    

* 再按成绩从高到低排序：


```python
def by_score(s):
    return s[1]
```


```python
print(sorted(L, key=by_score))
```

    [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
    
