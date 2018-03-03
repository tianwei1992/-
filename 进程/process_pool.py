"""

"""

from multiprocessing import Pool,Process
import time,os

def f1(i):
	print('f1开始:',i,os.getpid())
	time.sleep(5)
	print('f1结束:', i,os.getpid())
	return i + 10

def f2(i):
	print('f2开始:',i,os.getpid())
	time.sleep(3)
	print('f2结束:', i,os.getpid())
	return


if __name__=='__main__':
	pool=Pool(2)
	for i in range(5):
		print(i)
		pool.apply_async(func=f1,args=(i,),callback=f2)
	pool.close()
	pool.join()#固定顺序
	print('The end')
""""
在这里pool的行为表现值得注意:
1、pool.apply_async()方法创建进程，但进程的start()应该hi在所有进程都创建完毕以后才开始的，比如这里console会打印"0 1 2 "之后才有第一个“f1开始: 0"

2、callback的函数会在func返回以后执行，且func的返回值作为callback的实参。但并不代表它会在func返回之后立刻执行。比如，前两个进程p1和p2的f1返回以后，可以看到
p1马上继续执行了f2，但是p2在排队。因为pool的大小设为2，此时另一个抢占资源的进程是p3。
由此可以得出结论，func之后的callback运行，是新开了一个进程，需要重新抢占资源.为了验证这个结论，可以在两个函数中分别打印os.getpid()进程号看看

"""