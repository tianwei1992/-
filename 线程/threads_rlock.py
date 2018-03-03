""""
（2）递归锁-解决线程死锁-threading.R_Lock
不加锁会有什么问题？
如果程序运行到某一时刻，线程t1正处于阻塞A.acquire()，需要拿到A锁才能继续，但A锁此时被t2占据；而t2此时也处于阻塞，它需要拿到B锁才能解锁B.acquire()，但此时B锁正被t1占据……额，那这个时候程序就无法继续了。
这个问题的根源是：两个线程t1和t2各自占领了对方想要的那把锁，产生僵持。
解决办法就是：令全局只有1把锁，t2占了锁，t1就不能占。这样当前占锁的t2一定不会有需要从t1处获得另一把锁才能继续的情况，一定可以执行下去，直到r_lock.release()，把锁交出去。t1一定能够拿到这把锁，不会被卡死。

以下：会死锁的代码
run()里面t的流程是：1拿到A-2拿到B-3释放B-4释放A-5拿到B-6拿到A-7释放A-8释放B
在t1走到步骤4之后，t2会从步骤开始……然后t1在步骤5……卡主！

解决，全部换成r_lock=threading.RLock()
"""
import threading,time
class MyThread(threading.Thread):
	def __init__(self):
		super(MyThread,self).__init__()
	def run(self):
		lock_A.acquire()
		print(self.name+'get'+'lockA')

		time.sleep(1)
		lock_B.acquire()
		print(self.name + 'get' + 'lockB')
		time.sleep(1)
		lock_B.release()
		print(self.name + 'release' + 'lockB')
		lock_A.release()
		print(self.name + 'release' + 'lockA')
		lock_B.acquire()
		print(self.name + 'get' + 'lockB')
		time.sleep(3)
		lock_A.acquire()
		print(self.name+'get'+'lockA')
		time.sleep(2)
		lock_A.release()
		print(self.name + 'release' + 'lockA')
		lock_B.release()
		print(self.name + 'release' + 'lockB')

if __name__=='__main__':
	lock_A=threading.Lock()
	lock_B=threading.Lock()
	l=[]
	for i in range(5):
		t=MyThread()
		t.start()
		l.append(t)
	for t in l:
		t.join()




