# coding=utf-8

"""
module/program document
"""

from queue import Queue
from threading import Thread


class producer(Thread):
	def __init__(self, q):
		super().__init__()
		self.q = q

	def run(self):
		print('producer begin to run……')
		self.count = 5
		while self.count > 0:
			if self.count == 1:
				self.count -= 1
				self.q.put(2)
			else:
				self.count -= 1
				self.q.put(1)
		print('producer finish')


class consumer(Thread):
	def __init__(self, q):
		super().__init__()
		self.q = q

	def run(self):
		print('consumer begin to run……')
		while True:
			print('while true')
			data = self.q.get()
			if data == 2:
				print("stop because data=", data)
				self.q.task_done()
				print('q.task_done')
				break
			else:
				print("data is good,data=", data)
				#self.q.task_done()#不能省略，因为q.join()需要直到所有任务都task_done才取消阻塞，所以每次get后需要调用task_done，


		print('consumer finish')


def main():
	qq = Queue()
	p = producer(qq)
	c = consumer(qq)
	p.setDaemon(True)
	c.setDaemon(True)
	p.start()
	c.start()
	print('stage 1')
	qq.join()
	print('stage 2')
	print("queue is complete")


if __name__ == '__main__':
	main()