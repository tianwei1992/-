"""

（1）同步锁（互斥锁）-解决数据安全问题-threading.Lock
不加锁会有什么问题？
CPU处理第1个线程中途遇到IO阻塞,切换到第2个线程，此时本意是让第2个线程拿第1个处理之后结果作为输入，但由于第1个线程没有结束没有返回，因此第2个线程拿到的是处理之前的数据。
解决：在lock.acquire()和lock.release()中间的代码执行时，不发生线程切换

"""
import threading,time
num=100
def sub():
	global num
	lock.acquire()
	temp=num
	#先取值，然后在修改之前故意来个IO阻塞，期间好让CPU去执行其他线程
	#于是其他线程会错误地去到修改之前的初始值
	#time.sleep(1)
	time.sleep(0.00000001)
	num=temp-1
	lock.release()

if __name__=='__main__':
	lock=threading.Lock()
	l=[]
	for i in range(100):
		t=threading.Thread(target=sub)
		t.start()
		l.append(t)
	for t in l:
		t.join()
	print(num)
#本来期望得到0，实际的结果有很大出入
# time.sleep(0.00000001)时为98.time.sleep(2)时为99
#阻塞时间越长，期间下一个线程拿错的越多,这里不明显可能CPU的速度太快了……
#加锁lock=threading.Lock(),是在主线程里定义，然后lock.acquire()，lock.release()