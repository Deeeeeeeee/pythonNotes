#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_params(*params):
	print(params)

print_params("带一个*号的参数相当于一个元组(因为你将会看到逗号)，可接受多个参数","例如这样")

# 不提供任何元素，就是个空元组
print_params()

print('------------------------------------------------------')

def print_params_2(**kw):
	print(kw)

print_params_2(message='带两个*号的参数相当于一个字典', message2=666)