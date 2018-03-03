import threading
import time


def listen():
	print('begin to  listen')
	time.sleep(5)
	print('end listening')

def play():
	print('begin to play')
	time.sleep(4)
	print('end playing')


t1=threading.Thread(target=listen)
t2=threading.Thread(target=play)
start_time=time.time()
#法1 并发


# t1.start()
# t2.start()
# t1.join()
# t2.join()
#2顺序
t1.start()
t1.join()
t2.start()
t2.join()

end_time=time.time()
duration=end_time-start_time
print('duration:',duration)#并发5.001286268234253#顺序9.001514673233032

"""
Python的GIL锁加在cpython解释器上，作用是：同一时刻，只能有一个线程被CPU执行
因此Python的多线程并发的效果只能体现在IO密集型任务上：在IO阻塞期间，CPU切换到下一个线程继续工作，不浪费CPU时间，虽然切换也会消耗时间，但相比等待IO的时间来说微不足道；但是对于计算密集型任务，CPU本身几乎没有等待时间，切换时间占比就很大了，所以跟一次性顺序执行到底没有区别
"""
