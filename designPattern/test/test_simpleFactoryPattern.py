import unittest
from designPattern.simpleFactoryPattern import OperationFactory


class MyTestCase(unittest.TestCase):
    def test_createPlusOperate(self):
        factory = OperationFactory()
        operation = factory.create_operate('+')
        operation.numberA = 1
        operation.numberB = 2
        result = operation.get_result
        self.assertEquals(3, result)

    def test_createSubOperate(self):
        factory = OperationFactory()
        operation = factory.create_operate('-')
        operation.numberA = 1
        operation.numberB = 2
        result = operation.get_result
        self.assertEquals(-1, result)

    def test_createMulOperate(self):
        factory = OperationFactory()
        operation = factory.create_operate('*')
        operation.numberA = 1
        operation.numberB = 2
        result = operation.get_result
        self.assertEquals(2, result)

    def test_createDivOperate(self):
        factory = OperationFactory()
        operation = factory.create_operate('/')
        operation.numberA = 2
        operation.numberB = 2
        result = operation.get_result
        self.assertEquals(1, result)

if __name__ == '__main__':
    unittest.main()
