# 设计模式

> #### 学习设计模式是为了使代码：可维护，可复用，可扩展，灵活性好

- 可维护：想怎么改就怎么改，改动的代码少
- 可复用：代码可以在多处地方调用
- 可扩展：增加新的东西方便
- 灵活性好：想怎么整就怎么整，整完还不影响功能


## 设计模式学习建议：

##### 参考资料：《大话设计模式》 --- 程杰

1. 根据 python 文件上方的注释来编写代码，最好根据步骤来，可以了解到这整一个过程。如 simpleFactoryPattern.py：

		# 简单工厂模式：用一个单独的类来实例化对象。给我一个信号（参数），我将为你生产出相应的对象。
		# 需求：增加一个操作，不影响其他操作，比如开方。
		# 一个计算器操作类，+ - * / 继承它，还有一个工厂类。工厂根据需求（信号）返回相应的对象。

2. 找到 ./designPattern/test/ 下相应的 python 测试文件，如 /test/test_simpleFactoryPattern.py:
		
		def test_createPlusOperate(self):
	        factory = OperationFactory()
	        operation = factory.create_operate('+')
	        operation.numberA = 1
	        operation.numberB = 2
	        result = operation.get_result
			self.assertEquals(3, result)

3. 最后，让你的代码通过测试

## 目录：

1. <font size=4>[*简单工厂模式(simpleFactoryPattern)*](https://github.com/Deeeeeeeee/pythonNotes/blob/dev_seal_de/designPattern/simpleFactoryPattern.py)</font>  
<font size=2>相应测试：</font>[test_simpleFactoryPattern](https://github.com/Deeeeeeeee/pythonNotes/blob/dev_seal_de/designPattern/test/test_simpleFactoryPattern.py)