"""
协程的3种实现：
Python中协程的实现：

yield（最原始的方法）
√grennlet（模块）
gevent（模块）

gr1=greenlet(test1)
gr2=greenlet(test2)
然后在test1里面的一个位置切换到gr2，在test2里面的一个位置又切到gr1
gr2.switch()
gr1.switch()

……
不过问题是，如果有100次切换，全部手动写出来？
用gevent


"""

from greenlet import greenlet
def test1():
	print(12)
	gr2.switch()#4到这里又切去执行gr2
	print(34)
	#gr2.switch()#7又切到gr2



def test2():
	print(56)
	gr1.switch()#3此时切换去执行gr1
	print(18)
	gr1.switch()#6又切到gr1




gr1=greenlet(test1)
gr2=greenlet(test2)#1定义greenlet对象，将自己的函数test2封装在其中启动，就可以更好的运行
gr2.switch()#2先启动gr2