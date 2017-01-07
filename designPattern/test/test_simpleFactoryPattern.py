import unittest
from designPattern.simpleFactoryPattern import OperationFactory


class MyTestCase(unittest.TestCase):
    def test_createPlusOperate(self):
        factory = OperationFactory()
        oper = factory.create_operate('+')
        oper.numberA = 1
        oper.numberB = 2
        result = oper.get_result()
        self.assertEquals(3, result)

    def test_createSubOperate(self):
        factory = OperationFactory()
        oper = factory.create_operate('-')
        oper.numberA = 1
        oper.numberB = 2
        result = oper.get_result()
        self.assertEquals(-1, result)

    def test_createMulOperate(self):
        factory = OperationFactory()
        oper = factory.create_operate('*')
        oper.numberA = 1
        oper.numberB = 2
        result = oper.get_result()
        self.assertEquals(2, result)

    def test_createDivOperate(self):
        factory = OperationFactory()
        oper = factory.create_operate('/')
        oper.numberA = 1
        oper.numberB = 2
        result = oper.get_result()
        self.assertEquals(0, result)

if __name__ == '__main__':
    unittest.main()
