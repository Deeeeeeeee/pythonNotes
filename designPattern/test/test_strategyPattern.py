import unittest
from designPattern.strategyPattern import *


class MyTestCase(unittest.TestCase):
    '''
    def test_first_step(self):
        cashier_software = CashierSoftware()
        cashier_software.add_goods(price=5.0, amount=1)
        cashier_software.add_goods(price=9.9, amount=8)
        self.assertEqual(84.2, cashier_software.get_total_price())
    '''

    '''
    def test_second_step(self):
        cashier_software = CashierSoftware()
        cashier_software.add_goods_normal_charge(price=5.0, amount=2)
        cashier_software.add_goods_discount_charge(price=9.9, amount=5, rate=0.5)
        self.assertEqual(34.75, cashier_software.get_total_price())
    '''

    '''
    def test_third_step_normal(self):
        factory = ChargeRuleFactory()
        charge_rule = factory.create_charge_rule(factory.NORMAL_CHARGE)
        total_price = charge_rule.charge(price=5.0, amount=2)
        self.assertEqual(10, total_price)

    def test_third_step_discount(self):
        factory = ChargeRuleFactory()
        charge_rule = factory.create_charge_rule(factory.DISCOUNT_CHARGE)
        charge_rule.set_rate(0.8)
        total_price = charge_rule.charge(price=5.0, amount=2)
        self.assertEqual(8, total_price)

    def test_third_step_full_cut(self):
        factory = ChargeRuleFactory()
        charge_rule = factory.create_charge_rule(factory.FULL_CUT_CHARGE)
        charge_rule.set_full_cut(10, 3)
        total_price = charge_rule.charge(price=5.0, amount=2)
        self.assertEqual(7, total_price)
    '''

if __name__ == '__main__':
    unittest.main()
