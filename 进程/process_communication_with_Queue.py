"""
进程的创建也有两种方法，不过直接
p=multiprocessing.Process(target=f,args=(q,))，不能再进程执行的时候打印自己的名字
"""

"""
import multiprocessing,time
def f(q):
	#print(q.get(block=False))队列为空的时候去get会报错    raise Empty  queue.Empty，blcok的值设为True会阻塞
	q.put('a')
	q.put('b')
	print(time.ctime())

if __name__=='__main__':
	q=multiprocessing.Queue()
	#q必须在主进程中创建，然后作为参数传入子进程中
	l=[]
	for i in range(3):
		p=multiprocessing.Process(target=f,args=(q,))
		p.start()
		l.append(p)
	for p in l:
		p.join()

	print(p.name,p.pid,p.is_alive())
	foo=q.get()
	print(foo)

为了在子进程中打印显示子进程的名字，换第2种方法啊：派生新类然后定义run方法

"""
import multiprocessing,time
class MyProcess(multiprocessing.Process):
	def __init__(self,i,q):
		super(MyProcess,self).__init__()
		self.q=q#用self.q来接收q，不过在run()中操作self.q其实还是操作q本身
		self.foo=i
	def run(self):
		print(self.name)
		print(time.ctime())
		self.q.put(self.name)=
		self.q.put(self.foo)

if __name__=='__main__':
	l=[]
	q=multiprocessing.Queue(9)#如果队列长度太小，put遇到队列已满会阻塞
	for i in range(3):
		p=MyProcess(i,q)#注意这里也要把q作为参数传入创建的子进程
		l.append(p)
		p.start()
	for p in l:
		p.join()

	print('在主进程中打印Queue……')
	while (not q.empty()):
		print(q.get())
