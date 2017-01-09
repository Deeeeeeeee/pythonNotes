import unittest
from designPattern.strategyPattern import *


class MyTestCase(unittest.TestCase):
    def test_first_step(self):
        total_price = add_goods(5.0, 1)
        total_price = add_goods(9.9, 8)
        self.assertEqual(84.2, total_price)

    def test_get_total_price(self):
        print(get_total_price())

if __name__ == '__main__':
    unittest.main()
