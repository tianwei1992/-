"""

（3）Semaphore信号量-threading.Semaphere
最多允许同时有n个线程，多了会先把多的block住，直到有人release()。注意此时的acquire()和release()不再是线程对象t的方法，而semaphore对象自己的方法。
"""

import threading,time

class MyThread(threading.Thread):
	def __init__(self):
		super(MyThread,self).__init__()
	def run(self):
		if semaphore.acquire():
			print(self.name+':begin')
			time.sleep(4)
			print(self.name+":over")
			time.sleep(1)
			semaphore.release()

if __name__=='__main__':
	semaphore=threading.Semaphore(6)#虽然有100个t都start了，但是因为有判断if semaphore.acquire():，控制了最多同时有6个线程在并发执行,等有t执行到semaphore.release()以后，才放下一个
	l=[]
	for i in range(100):
		t=MyThread()
		t.start()
		l.append(t)
	for t in l:
		t.join()

