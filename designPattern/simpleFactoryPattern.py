#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 简单工厂模式：用一个单独的类来实例化对象。给我一个信号（参数），我将为你生产出相应的对象。
# 一个计算器操作类，+ - * / 继承它，一个工厂类。工厂根据需求（信号）返回相应的对象。


class Operation(object):
    def get_result(self):
        pass


class OperationAdd(Operation):
    def get_result(self):
        return self.numberA + self.numberB


class OperationSub(Operation):
    def get_result(self):
        return self.numberA - self.numberB


class OperationMul(Operation):
    def get_result(self):
        return self.numberA * self.numberB


class OperationDiv(Operation):
    @property
    def get_result(self):
        try:
            result = self.numberA / self.numberB
            return result
        except:
            print("error: divided by zero")
            return 0


class OperationFactory(object):
    operation = {}
    operation["+"] = OperationAdd()
    operation["-"] = OperationSub()
    operation["*"] = OperationMul()
    operation["/"] = OperationDiv()

    def create_operate(self, operate):
        oper = self.operation.get(operate)
        return oper
