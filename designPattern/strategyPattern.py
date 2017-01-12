#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# 策略模式：完成一件事情有多种实现方法（多种算法）时，可以考虑使用策略模式。比如，你去上学，可以选择骑自行车，坐公交，
          坐地铁，开车或者走路，这只取决于你一时的条件跟决定。
# 需求：做一个商场收银软件，营业员根据客户所购买商品的单价和数量，向客户收费。商场会有正常收费，打折，满减等不同收费策略。

# 第一步：编写一个方法完成统计客户总价。
# 第二步：增加打折算法。
# 第三步：用简单工厂模式实现收费的新策略：正常收费，打折收费，满减收费。（去除增加新算法时，改动其他算法的风险）
# 第四步：http://www.imooc.com/wiki/detail/id/137 学习策略模式结构，将策略模式与工厂模式结合完成需求。
'''


class ChargeRule(object):
    def charge(self, price, amount):
        pass


class NormalChargeRule(ChargeRule):
    def charge(self, price, amount):
        return price * amount


class DiscountChargeRule(ChargeRule):
    def __init__(self):
        self.__rate = 1.0

    def set_rate(self, rate):
        self.__rate = rate

    def charge(self, price, amount):
        return price * amount * self.__rate


class FullCutChargeRule(ChargeRule):
    def __init__(self):
        self.__full = 0.0
        self.__cut = 0.0

    def set_full_cut(self, full, cut):
        self.__full = full
        self.__cut = cut

    def charge(self, price, amount):
        total_price = price * amount
        if total_price >= self.__full:
            total_price -= self.__cut
        return total_price


class ChargeRuleFactory(object):
    NORMAL_CHARGE = "normal"
    DISCOUNT_CHARGE = "discount"
    FULL_CUT_CHARGE = "full_cut"

    charge_rules = {}
    charge_rules["normal"] = NormalChargeRule()
    charge_rules["discount"] = DiscountChargeRule()
    charge_rules["full_cut"] = FullCutChargeRule()

    def create_charge_rule(self, rule):
        charge_rule = self.charge_rules[rule]
        return charge_rule
