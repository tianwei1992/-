"""
3、进程同步-同步锁
进程间也要共享资源！比如同时调用Pycharm的print()或者同时写一个文件，因此也存在某些操作必须上锁的必要性。

"""
from multiprocessing import Lock,Process
def f(l,i):
	if l.acquire():
		print(l)
		print(i)
	l.release()

if __name__=='__main__':
	lock=Lock()#创建了一把锁
	l=[]
	for i in range(5):
		p=Process(target=f,args=(lock,i))
		p.start()
		l.append(p)
	for p in l:
		p.join()