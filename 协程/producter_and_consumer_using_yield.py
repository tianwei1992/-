"""
协程的3种实现：
Python中协程的实现：

√yield（最原始的方法）
grennlet（模块）
gevent（模块）

这是用yiled实现生产者消费者模型，这个模型也可以用多线程+线程队列实现，不过有点区别，在于：

yiled实现的c和p之间没有中介，通过send和yiled直接收发数据，一边发另一边同一时间收到，不存在一边先放到队列里，另一边再去取，队列里可以堆起来这样……产品不能保存，即使消费

这样假如p的生产速度很快，也是要等c消费以后才能继续下一个

"""

import time

class Producer():
	def __init__(self,consumer_lst):
		self.consumer_lst=consumer_lst
	def produce(self):
		n=0
		for g in consumer_lst:
			g.__next__()#生成器必须先next运行到第一次yiled，才能用send发送，不然没有yleld接收
		while 1:
			for g in consumer_lst:
				print('p:正在生产……',n)
				time.sleep(0.5)#假装生产用时2s
				g.send(n)#生产好就立刻发给c
				n=n+1

class Consumer():
	def consume(self):
		print('c:准备好了')
		while True:
			goods=yield
			print('c:拿到货了……，吃',goods)
			time.sleep(2)#c就循环3个步骤：收到-吃掉-等待





if __name__=='__main__':

	consumer_lst=[]
	for i in range(5):
		c=Consumer()
		g=c.consume()
		consumer_lst.append(g)
		p = Producer(consumer_lst)
		p.produce()